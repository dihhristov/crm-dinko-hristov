from django.core.exceptions import ValidationError

VALIDATION_ONLY_LETTERS_ERROR_MESSAGE = 'Value must contain only letters'
VALIDATION_ONLY_DIGITS_ERROR_MESSAGE = 'Value must contain only digits'


def only_letters_validator(value):
    if not value.isalpha:
        raise ValidationError(VALIDATION_ONLY_LETTERS_ERROR_MESSAGE)


def only_digits_validator(value):
    if not value.isdigit:
        raise ValidationError(VALIDATION_ONLY_DIGITS_ERROR_MESSAGE)

#
# def file_max_size_in_mb_validator(max_size):
#     def validate(value):
#         filesize = value.file.size
#         if filesize > max_size * 1024 * 1024:
#             raise ValidationError('Max file size is %sMB.' % str(max_size))
#
#     return validate
