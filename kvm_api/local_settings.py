DATABASES = {
'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'kvm',
        'USER': 'kvm',
        'PASSWORD': 'kvm',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'kvm',
)