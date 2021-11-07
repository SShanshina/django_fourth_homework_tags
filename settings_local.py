SECRET_KEY = '.....'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_orm_news',
        'USER': 'django_orm_news',
        'PASSWORD': 'django-orm-news',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
