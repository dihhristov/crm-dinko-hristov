from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models

from crm.accounts.models import Profile
from crm.helpers.validators import only_letters_validator, only_digits_validator

CUSTOMER_NAME_MAX_LEN = 100

EIC_MAX_LEN = 13
EIC_MIN_LEN = 9

PRICE_MAX_LEN = 7
PRICE_MIN_LEN = 4


class Customers(models.Model):
    CITY_MAX_LEN = 30

    REPR_FIRST_NAME_MAX_LEN = 30
    REPR_FIRST_NAME_MIN_LEN = 2

    REPR_LAST_NAME_MAX_LEN = 30
    REPR_LAST_NAME_MIN_LEN = 2

    MOBILE_MAX_LEN = 10
    MOBILE_MIN_LEN = MOBILE_MAX_LEN

    DESCRIPTION_MAX_LEN = 250

    customer_name = models.CharField(
        max_length=CUSTOMER_NAME_MAX_LEN,
        unique=True,
    )
    eic = models.CharField(
        max_length=EIC_MAX_LEN,
        unique=True,
        validators=(MinLengthValidator(EIC_MIN_LEN),
                    only_digits_validator,
                    )

    )
    representative_first_name = models.CharField(
        max_length=REPR_FIRST_NAME_MAX_LEN,
        validators=(only_letters_validator,
                    MinLengthValidator(REPR_LAST_NAME_MIN_LEN),
                    )
    )

    representative_last_name = models.CharField(
        max_length=REPR_LAST_NAME_MAX_LEN,
        validators=(only_letters_validator,
                    MinLengthValidator(REPR_LAST_NAME_MIN_LEN),
                    )
    )
    city = models.CharField(
        max_length=CITY_MAX_LEN
    )
    address = models.TextField(
    )
    email = models.EmailField()

    mobile = models.CharField(
        max_length=MOBILE_MAX_LEN,
        validators=(
            MinLengthValidator(MOBILE_MIN_LEN),
        )
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LEN,
        blank=True,
        null=True,
    )

    account_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name

class Contracts(models.Model):
    ANNUAL_CONSUMPTION_MAX_LEN = 6

    contract_date = models.DateField()

    eic = models.CharField(
        max_length=EIC_MAX_LEN,
        validators=(
            MinLengthValidator(EIC_MIN_LEN),
            only_digits_validator,
        )
    )

    annual_consumption = models.CharField(
        max_length=ANNUAL_CONSUMPTION_MAX_LEN,
    )
    price = models.CharField(
        max_length=PRICE_MAX_LEN,
        validators=(
            MinLengthValidator(PRICE_MIN_LEN),
        )
    )

    contract_expiration = models.DateField()

    contract_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)


class Tasks(models.Model):
    MEETING = 'Meeting'
    CALL = 'Call'

    TASKS = [(x, x) for x in (MEETING, CALL)]

    COMPLETED = 'completed'
    IN_PROGRESS = 'in progress'
    NOT_STARTED = 'not started'

    TASK_STATE = [(x, x) for x in (COMPLETED, IN_PROGRESS, NOT_STARTED)]

    task_type = models.CharField(
        max_length=max(len(x) for _, x in TASKS),
        choices=TASKS,
    )

    creation_date = models.DateField(
        auto_now_add=True
    )

    task_state = models.CharField(
        max_length=max(len(x) for _, x in TASK_STATE),
        choices=TASK_STATE,
    )

    deadline = models.DateField()

    description = models.TextField()

    task_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)

class Offers(models.Model):
    OFFER_QUANTITY_MAX_LEN = 6

    offer_date = models.DateField(
        auto_now_add=True
    )

    offer_validity = models.DateField()

    offered_quantity = models.CharField(
        max_length=OFFER_QUANTITY_MAX_LEN,
    )
    offer_price = models.CharField(
        max_length=PRICE_MAX_LEN,
        validators=(MinLengthValidator(PRICE_MIN_LEN),
                    only_digits_validator,)
    )

    offer_owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)

