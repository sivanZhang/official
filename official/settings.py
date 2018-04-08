"""
Django settings for official project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ey0$l0e3mkwr8cvy+!m+rmulv*0o=z(u$mfjx9#7g!n9x!=+$a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_WHITELIST = (
    '192.168.1.105:8000', '192.168.1.103:80','192.168.1.103', '127.0.0.1',  
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', 
    'piclab',
    'appuser',
    'product',
    'category',
    'sitecontent',
    'ckeditor',
    'ckeditor_uploader',
    'page',
    'book',
    'bussiness',
    'area',
    'dept',
    'subscribe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'official.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'official.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'official',
		'USER':'root',
        'PASSWORD':'sqlroot',
        'HOST':'localhost',
        'PORT':3306, 
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static1')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'appuser.AdaptorUser'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
)
CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_CONFIGS = {
    'default': { 
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Font','FontSize','Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',  
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'font',
            'autolink',
            'autoembed',
             
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}
AUTHENTICATION_BACKENDS=[
    'official.third_party_backend.PhoneBackend',
    'django.contrib.auth.backends.ModelBackend',
    #'official.user_backend.EmailBackend',
    #'official.third_party_backend.EmailBackend'
]
LOGIN_URL = '/users/login/'
PROJECTNAME = '一数科技'
EMAIL_SWITCH = True
SMTP_SERVER         ='smtp.exmail.qq.com' #SMTP server IP address
SMTP_SERVER_USER    ='shop@a-su.com.cn'  
SMTP_SERVER_PWD     ='Bjasu@2018'  
SMTP_FROM           = "postmaster"

SMS = {
    'SMS_SN' : "SDK-BBX-010-22746",
    'SMS_PWD' : "76D7DAAC410AF587F0DEEE4F5FA86795",
}
SMS_API = "http://sdk2.entinfo.cn:8061/mdsmssend.ashx?sn=SDK-BBX-010-22746&pwd=76D7DAAC410AF587F0DEEE4F5FA86795&mobile={0}&content={1}"


# 第三方用户登录信息
LOGIN_MASTER = "http://127.0.0.1:7000"
STORE_LOGIN = 'http://127.0.0.1:8000'
LOGIN_APPID = "3d7bf00b-1e76-4547-901f-53a8b1cfd330"
LOGIN_SECRET = "92e49c5e-1595-4d0a-a702-9d99c5bf8e81"
THIRD_LOGIN_URL = LOGIN_MASTER + "/users/login/?appid="+LOGIN_APPID+"&redirect_url="+STORE_LOGIN+"/users/login/"
THIRD_AUTH_URL = LOGIN_MASTER + "/users/oauth2/authorize/"


# 支付宝 正式环境
# 支付宝配置参数

ALIPAY_APPID = "2017020405508290"
ALIPAY_URL = "https://openapi.alipay.com/gateway.do"
ALI_PUBLIC_KEY = os.path.join(BASE_DIR, 'official', 'alipay_public.pem')
PRIVATE_KEY = os.path.join(BASE_DIR, 'official', 'app_private_key.pem')

PAYHOST = 'http://www.asucast.com/'
ALIPAY_RETURN_URL = PAYHOST + 'book/alipay_check_pay'
ALIPAY_NOTIFY_URL = PAYHOST + 'book/alipay_notify'
"""
# 支付宝测试-沙箱环境
# 支付宝配置参数
ALIPAY_APPID = "2016091000479829"
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"
ALI_PUBLIC_KEY = os.path.join(BASE_DIR, 'official', 'alipay_public.pem')
PRIVATE_KEY = os.path.join(BASE_DIR, 'official', 'app_private_key.pem')

PAYHOST = 'http://www.asu.com:8000/'
ALIPAY_RETURN_URL = PAYHOST + 'book/alipay_check_pay'
ALIPAY_NOTIFY_URL = PAYHOST + 'book/alipay_notify'
"""