from . base import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = ['localhost']

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    # 'django.contrib.postgres',
]

MIDDLEWARE += [

]

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'), 
#         'USER': config('DB_USER') , 
#         'PASSWORD': config('DB_PASSWORD') ,
#         'HOST': config('DB_HOST') , 
#         'PORT': '5432',
#     }
# }
#for heroku only


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = 'shaamareer0@gmail.com'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD = 'Madhoore123'
# EMAIL_PORT = 587

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# #cloudinary
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'kaabe',
#     'API_KEY': '158618637359113',
#     'API_SECRET': 'asEA80ABQNCZJsCzFVOJJDz4WIo'
# }


# #For heroku Specific 
# import dj_database_url 
# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

# import django_heroku
# django_heroku.settings(locals())

