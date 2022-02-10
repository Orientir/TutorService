from django.utils.translation import pgettext_lazy


class UserEvents:
    """The different user event types."""

    # Account related events
    ACCOUNT_CREATED = "account_created"
    PASSWORD_RESET_LINK_SENT = "password_reset_link_sent"
    PASSWORD_RESET = "password_reset"
    PASSWORD_CHANGED = "password_changed"

    # Task related events - for students
    PLACED_OFFER = "placed_offer"  # created an offer
    EDITED_OFFER = "edited_offer"  # edited an offer
    CANCELLED_OFFER = "cancelled_offer"  # cancelled an offer

    # Task related events - for teachers
    APPLIED_OFFER = "applied_offer"  # teacher apply on offer
    SETTLED_NEW_PRICE = "settled_new_price"  # teacher set new price for offer
    CANCELLED_APPLY = "cancelled_apply"  # cancelled an apply

    # Task related events - for offer
    FROZEN_MONEY = "frozen_money"  # money is frozen on student`s pay card
    NOT_ENOUGH_MONEY = "not_enough_money"  # cancelled an offer - not enough money on pay card
    CANCELLED_PAYMENT = "cancelled_payment"  # payment was cancelLed in bank`s app (user do not confirm payment)
    PAYMENT_DONE = "payment_done" # payment was successful

    CHOICES = [
        (
            ACCOUNT_CREATED,
            pgettext_lazy(
                "Event from a user that got their account created",
                "The account account was created",
            ),
        ),
        (
            PASSWORD_RESET_LINK_SENT,
            pgettext_lazy(
                "Event from a user that got the password reset link sent by email",
                "Password reset link was sent to the customer",
            ),
        ),
        (
            PASSWORD_RESET,
            pgettext_lazy(
                "Event from a user that reset their password",
                "The account password was reset",
            ),
        ),
        (
            PASSWORD_CHANGED,
            pgettext_lazy(
                "Event from a user that change their password",
                "The account password was changed",
            ),
        ),
        (
            PLACED_OFFER,
            pgettext_lazy(
                "Event from a student that placed an offer", "An offer was placed"
            ),
        ),
        (
            EDITED_OFFER,
            pgettext_lazy(
                "Event from a student that edit an offer", "An offer was edited"
            ),
        ),
        (
            CANCELLED_OFFER,
            pgettext_lazy(
                "Event from a student that cancel an offer", "An offer was cancelled"
            ),
        ),
        (
            APPLIED_OFFER,
            pgettext_lazy(
                "Event from a teacher that apply an offer",
                "An offer was applied",
            ),
        ),
        (
            SETTLED_NEW_PRICE,
            pgettext_lazy(
                "Event from a teacher that set new price for offer",
                "A new price was settled",
            ),
        ),
        (
            CANCELLED_APPLY,
            pgettext_lazy(
                "Event from a teacher cancelled apply",
                "An apply was cancelled",
            ),
        ),
        (
            FROZEN_MONEY,
            pgettext_lazy(
                "Event from a bank that frozen money on pay card",
                "Money was frozen",
            ),
        ),
        (
            NOT_ENOUGH_MONEY,
            pgettext_lazy(
                "Event from a bank - not enough money for payment",
                "Not enough money for payment",
            ),
        ),
        (
            CANCELLED_PAYMENT,
            pgettext_lazy(
                "Event from a bank - user cancelled the payment",
                "Payment was cancelled with user",
            ),
        ),
        (
            PAYMENT_DONE,
            pgettext_lazy(
                "Event from a bank - payment was successful",
                "Payment was successful",
            ),
        ),
    ]