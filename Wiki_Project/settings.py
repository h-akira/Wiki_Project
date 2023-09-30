"""
Django settings for Wiki_Project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from .settings_local import *
import os
import sys
from datetime import datetime

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# 独自ライブラリ
LIB_DIR = os.path.join(BASE_DIR, 'lib')
sys.path.append(LIB_DIR)

# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.forms',
  'django_boost',
  'Wiki.apps.WikiConfig',
  'accounts.apps.AccountsConfig',
  'mdeditor',
]

# MDEDITOR
X_FRAME_OPTIONS = 'SAMEORIGIN' 
MDEDITOR_CONFIGS = {
  'default': {
    'language': 'en',
    'height': 600,
    'toolbar': [
      "undo", "redo", "image", "|",
      "bold", "quote", "|",
      "h1", "h2", "h3", "h5", "h6", "|",
      "list-ul", "list-ol", "hr", "|",
      "||", "preview", "watch", "fullscreen"
    ],
    'lineWrapping': True,
  }
}

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Wiki_Project.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, "templates")],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'Wiki_Project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_local"),]
if not DEBUG:
  STATIC_ROOT = os.path.join(BASE_DIR,'static') 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# MARKDOWNX_MEDIA_PATH = datetime.now().strftime('markdownx/%Y/%m/%d')
# MARKDOWN_EXTENSIONS = [
#   'markdown.extensions.extra',  # テーブル，コードブロック等
#   'markdown.extensions.codehilite',  # コードハイライト
#   'markdown.extensions.toc',  # 目次
#   'markdown.extensions.nl2br',  # 改行
# 	'markdown.extensions.sane_lists',  # 箇条関係
# ]
## 追加する場合は以下のページから選択する．
## https://python-markdown.github.io/extensions/

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "Wiki:index"
LOGOUT_REDIRECT_URL = "Wiki:index"  

