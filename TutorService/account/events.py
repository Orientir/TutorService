from typing import Optional

from django.contrib.auth.base_user import AbstractBaseUser

from ..offer.models import Offer
from . import UserEvents
from .models import UserEvent

UserType = AbstractBaseUser


def user_account_created_event(*, user: UserType) -> Optional[UserEvent]:
    return UserEvent.objects.create(user=user, type=UserEvents.ACCOUNT_CREATED)


def user_password_reset_link_sent_event(
    *, user_id: UserType
) -> Optional[UserEvent]:
    return UserEvent.objects.create(
        user_id=user_id, type=UserEvents.PASSWORD_RESET_LINK_SENT
    )


def user_password_reset_event(*, user: UserType) -> Optional[UserEvent]:
    return UserEvent.objects.create(user=user, type=UserEvents.PASSWORD_RESET)


def user_password_changed_event(*, user: UserType) -> Optional[UserEvent]:
    return UserEvent.objects.create(user=user, type=UserEvents.PASSWORD_CHANGED)


def student_placed_offer_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.PLACED_OFFER
    )

def student_edited_offer_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.EDITED_OFFER
    )

def student_cancelled_offer_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.CANCELLED_OFFER
    )

def teacher_applied_offer_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.APPLIED_OFFER
    )

def teacher_set_new_price_offer_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.SETTLED_NEW_PRICE
    )

def teacher_cancelled_apply_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.CANCELLED_APPLY
    )

def bank_frozen_money_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.FROZEN_MONEY
    )

def bank_not_enough_money_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.NOT_ENOUGH_MONEY
    )

def bank_reject_money_event(  # user do not confirm payment
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.CANCELLED_PAYMENT
    )

def bank_payment_done_event(
    *, user: UserType, offer: Offer
) -> Optional[UserEvent]:
    if user.is_anonymous:
        return None

    return UserEvent.objects.create(
        user=user, offer=offer, type=UserEvents.PAYMENT_DONE
    )
