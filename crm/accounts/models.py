from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from crm.accounts.menagers import CrmUserManager
from crm.helpers.validators import only_letters_validator


class CrmUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USER_MAX_LEN = 25

    username = models.CharField(
        max_length=USER_MAX_LEN,
        unique=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    object = CrmUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    ACCOUNT_MANAGER = 'Account manager'
    KEY_ACCOUNT_MANAGER = "Key account manager"
    SALES_DIRECTOR = 'Sales director'
    CEO = 'CEO'

    POSITION = [(x, x) for x in (ACCOUNT_MANAGER, KEY_ACCOUNT_MANAGER, SALES_DIRECTOR, CEO)]
    POSITION_MAX_LEN = max(len(x) for _, x in POSITION)
    # IMAGE_FILE_MAX_SIZE = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )

    email = models.EmailField(
    )

    position = models.CharField(
        max_length=POSITION_MAX_LEN,
        choices=POSITION
    )

    image = models.URLField(
        blank=True,
        null=True
    )

    user = models.OneToOneField(
        CrmUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
