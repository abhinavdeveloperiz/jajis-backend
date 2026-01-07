
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v9t#=pguwv4v++8b!$iz5894-id@p_$i9fmj9%_(r$wk-_g5oe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'inspirezesttechnologiesprojectdemo.space', 
    'www.inspirezesttechnologiesprojectdemo.space',
    "jajis.up.railway.app",
    '127.0.0.1', 
    'localhost',  
]


CSRF_TRUSTED_ORIGINS = [
    "https://jajis.up.railway.app",
    
]



CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://jajis.onrender.com",
    "https://jajis.vercel.app/",
]



# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ]
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #corseheaders
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Note the correct capitalization
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Jajis_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Jajis_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'inspirez_jajis',
#         'USER': 'inspirez_jajis',
#         'PASSWORD': '@admin@2025',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }





# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/


LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "staticfiles"  
STATICFILES_DIRS = [
    BASE_DIR / "static",  
]


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'









JAZZMIN_SETTINGS = {
    "site_title": "Jaji's",
    "site_header": "Jajis Admin",
    "site_brand": "Jaji's",
    "welcome_sign": "Welcome to the Jaji's Admin Panel",
    "copyright": "Jaji's © 2025",
    "search_model": "auth.User",
    "show_ui_builder": True,
    "topmenu_links": [
        {"name": "Home", "url": "/", "permissions": ["auth.view_user"]},
        {"model": "auth.user"},
        {"app": "myapp"},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "myapp": "fas fa-graduation-cap",
    },
    "related_modal_active": True,
}



import os
from dotenv import load_dotenv

load_dotenv()

# Razorpay Configuration
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'jajisproject@gmail.com'
EMAIL_HOST_PASSWORD = 'vgwd nfyj jyla yyis'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

