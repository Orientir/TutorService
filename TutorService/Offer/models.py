from django.db import models
from versatileimagefield.fields import VersatileImageField

from . import SubjectChoice, GradeChoice, StatusOfferChoice


class Offer(models.Model):
    student = models.ForeignKey('account.User', related_name="student_offers", on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('account.User', related_name="teacher_offers", on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    image = VersatileImageField(upload_to="offer-image", blank=True, null=True)
    price = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    start_lesson = models.DateTimeField()

    status = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in StatusOfferChoice.CHOICES
        ],
    )
    subject = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in SubjectChoice.CHOICES
        ],
    )
    grade = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in GradeChoice.CHOICES
        ],
    )