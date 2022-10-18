#开发配置
import os

from .base  import *#NOQA


BASE_DIR = BASE_DIR.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'dal',
    'dal_select2',
    'mainblog',
    'config',
    'comment',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'debug_toolbar',
    # 'pympler',
    # 'debug_toolbar_line_profiler',
]

MIDDLEWARE = [

    'mainblog.middleware.user_id.UserIDMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


#django_debug_tools
INTERNAL_IPS = ['*','127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
    # 'djdt_flamegraph.FlamegraphPanel',#仅单线程可用 python3 manage.py runserver 0.0.0.0:8000 --noreload --nothreading
    # 'pympler.panels.MemoryPanel',
    # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
]

# print(BASE_DIR)

# THEME = 'default'
THEME = 'bootstrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'themes',THEME,'templates')],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_test',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT':'3306',
        'PASSWORD': '8290680',
    }
}
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'all_static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'themes',THEME,'static'),
]

CKEDITOR_CONFIGS = {
    'default':{
        'toolbar':'full',
        'height':300,
        'width':1200,
        'tabSpace':4,
        'extraPlugins':'codesnippet',
    }

}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
CKEDITOR_UPLOAD_PATH = 'article_images'

#水印
DEFAULT_FILE_STORAGE = 'blog.storage.WatermarkStorage'