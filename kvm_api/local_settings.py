DATABASES = {
'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'kvm',
        'USER': 'plusk01',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost',
)