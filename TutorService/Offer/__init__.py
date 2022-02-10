from django.utils.translation import pgettext_lazy


class SubjectChoice:
    MATH = "mathematics"
    CHEMISTRY = "chemistry"
    PHYSICS = "physics"
    BIOLOGY = "biology"

    CHOICES = [
        (
            MATH,
            pgettext_lazy(
                "Subject in school",
                "Math",
            ),
        ),
        (
            CHEMISTRY,
            pgettext_lazy(
                "Subject in school",
                "Chemistry",
            ),
        ),
        (
            PHYSICS,
            pgettext_lazy(
                "Subject in school",
                "Physics",
            ),
        ),
        (
            BIOLOGY,
            pgettext_lazy(
                "Subject in school",
                "Biology",
            ),
        ),
    ]


class StatusOfferChoice:
    IN_SEARCH = "in_search"
    PAID = "paid"
    CANCELLED = "cancelled"

    CHOICES = [
        (
            IN_SEARCH,
            pgettext_lazy(
                "Offer in search of teacher",
                "In search",
            ),
        ),
        (
            PAID,
            pgettext_lazy(
                "Offer is paid",
                "Paid",
            ),
        ),
        (
            CANCELLED,
            pgettext_lazy(
                "Offer is cancelled",
                "Cancelled",
            ),
        ),
    ]


class GradeChoice:
    FIRST = "1"
    SECOND = "2"
    THIRD = "3"
    FOURTH = "4"
    FIFTH = "5"
    SIXTH = "6"
    SEVENTH = "7"
    EIGHTH = "8"
    NINTH = "9"
    TENTH = "10"
    ELEVENTH = "11"

    CHOICES = [
        (
            FIRST,
            pgettext_lazy(
                "Grade in school",
                "1",
            ),
        ),
        (
            SECOND,
            pgettext_lazy(
                "Grade in school",
                "2",
            ),
        ),
        (
            THIRD,
            pgettext_lazy(
                "Grade in school",
                "3",
            ),
        ),
        (
            FOURTH,
            pgettext_lazy(
                "Grade in school",
                "4",
            ),
        ),
        (
            FIFTH,
            pgettext_lazy(
                "Grade in school",
                "5",
            ),
        ),
        (
            SIXTH,
            pgettext_lazy(
                "Grade in school",
                "6",
            ),
        ),
        (
            SEVENTH,
            pgettext_lazy(
                "Grade in school",
                "7",
            ),
        ),
        (
            EIGHTH,
            pgettext_lazy(
                "Grade in school",
                "8",
            ),
        ),
        (
            NINTH,
            pgettext_lazy(
                "Grade in school",
                "9",
            ),
        ),
        (
            TENTH,
            pgettext_lazy(
                "Grade in school",
                "10",
            ),
        ),
        (
            ELEVENTH,
            pgettext_lazy(
                "Grade in school",
                "11",
            ),
        ),
    ]
