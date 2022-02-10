from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import pgettext_lazy
from phonenumber_field.modelfields import PhoneNumberField
from versatileimagefield.fields import VersatileImageField

from ..core.utils.json_serializer import CustomJsonEncoder
from . import UserEvents
from .validators import validate_possible_number


class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]

class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_teacher=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)

        user = self.model(
            email=email, is_active=is_active, is_teacher=is_teacher, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_superuser=True, **extra_fields
        )

    def students(self):
        return self.get_queryset().filter(is_teacher=False)

    def teachers(self):
        return self.get_queryset().filter(is_teacher=True)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    phone = PossiblePhoneNumberField(blank=True, default="")
    avatar = VersatileImageField(upload_to="user-avatars", blank=True, null=True)

    hide_personal_info = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        permissions = (
            ("manage_student", pgettext_lazy("Permission description", "Manage students.")),
            ("manage_teacher", pgettext_lazy("Permission description", "Manage teachers.")),
        )

    def get_full_name(self):
        if self.first_name or self.last_name:
            return ("%s %s" % (self.last_name, self.first_name)).strip()
        return self.email

    def get_short_name(self):
        return self.email

    def get_username(self):
        return self.username


class UserEvent(models.Model):
    """Model used to store events that happened during the user lifecycle."""

    date = models.DateTimeField(default=timezone.now, editable=False)
    type = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in UserEvents.CHOICES
        ],
    )

    offer = models.ForeignKey("offer.Offer", on_delete=models.SET_NULL, null=True)
    parameters = JSONField(blank=True, default=dict, encoder=CustomJsonEncoder)

    user = models.ForeignKey(User, related_name="events", on_delete=models.CASCADE)

    class Meta:
        ordering = ("date",)

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type!r}, user={self.user!r})"

