from django.core.validators import RegexValidator

name_validator = RegexValidator(
        regex='^[a-zA-Z,]+$',
        message='Enter only alphabetical characters with or without commas.',
        code='invalid_name'
    )