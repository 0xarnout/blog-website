from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-a=i$l+55rdifpe%w993b$qam*)%tczn6$^wvfr2&b+2bcp)7ex')

DEBUG = True

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'django_distill',
    'django_cachekiller',
    'core.apps.CoreConfig',
    'blog_app.apps.BlogAppConfig',
    'about.apps.AboutConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blog.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = 'media/'
STATIC_ROOT = BASE_DIR / 'static/'
STATIC_URL = 'static/'

CKEDITOR_5_UPLOAD_FILE_TYPES = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'webp', 'tiff']
CKEDITOR_5_FILE_STORAGE = 'blog.storages.CustomStorage'
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'outdent', 'indent', '|' 'bold', 'italic', 'link', 'underline', 'strikethrough',
            'subscript', 'superscript', '|',
            'codeBlock', 'sourceEditing', 'insertImage',
            'bulletedList', 'numberedList', 'todoList', 'WordCount'],
        'image': {
             'toolbar': ['imageTextAlternative'],
        },
        'codeBlock':{
            'languages':[
                {'language': 'plaintext', 'label': 'PLAINTEXT'},
                {'language': 'bash', 'label': 'BASH'},
                {'language': 'c', 'label': 'C'},
                {'language': 'cpp', 'label': 'C++'},
                {'language': 'csharp', 'label': 'C#'},
                {'language': 'css', 'label': 'CSS'},
                {'language': 'diff', 'label': 'DIFF'},
                {'language': 'go', 'label': 'GO'},
                {'language': 'graphql', 'label': 'GRAPHQL'},
                {'language': 'ini', 'label': 'INI'},
                {'language': 'java', 'label': 'JAVA'},
                {'language': 'javascript', 'label': 'JAVASCRIPT'},
                {'language': 'json', 'label': 'JSON'},
                {'language': 'kotlin', 'label': 'KOTLIN'},
                {'language': 'less', 'label': 'LESS'},
                {'language': 'lua', 'label': 'LUA'},
                {'language': 'makefile', 'label': 'MAKEFILE'},
                {'language': 'markdown', 'label': 'MARKDOWN'},
                {'language': 'objectivec', 'label': 'OBJECTIVE-C'},
                {'language': 'perl', 'label': 'PERL'},
                {'language': 'php', 'label': 'PHP'},
                {'language': 'php-template', 'label': 'PHP-TEMPLATE'},
                {'language': 'python', 'label': 'PYTHON'},
                {'language': 'python-repl', 'label': 'PYTHON-REPL'},
                {'language': 'r', 'label': 'R'},
                {'language': 'ruby', 'label': 'RUBY'},
                {'language': 'rust', 'label': 'RUST'},
                {'language': 'scss', 'label': 'SCSS'},
                {'language': 'shell', 'label': 'SHELL'},
                {'language': 'sql', 'label': 'SQL'},
                {'language': 'swift', 'label': 'SWIFT'},
                {'language': 'typescript', 'label': 'TYPESCRIPT'},
                {'language': 'vbnet', 'label': 'VBNET'},
                {'language': 'wasm', 'label': 'WASM'},
                {'language': 'xml', 'label': 'XML'},
                {'language': 'yaml', 'label': 'YAML'},
            ],
        },
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3','|',
            'bulletedList', 'numberedList',
        ],
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph'},
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3' }
            ]
        },
        "removePlugins": ["ImageResize"],
    },
}

DISTILL_SKIP_STATICFILES_DIRS = ['django_ckeditor_5']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
