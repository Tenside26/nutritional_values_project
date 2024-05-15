from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DOCKER_DB'),
        'USER': config('DOCKER_DB_USER'),
        'PASSWORD': config('DOCKER_DB_PASSWORD'),
        'HOST': config('DOCKER_DB_HOST'),
        'PORT': config('DOCKER_DB_PORT')
    }
}
