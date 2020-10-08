import os
from decouple import config
import django_heroku
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'rest_framework',
    'django_celery_beat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()

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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

CELERY_BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

USERS_URLS = ['https://google.qwiklabs.com/public_profiles/c487dd85-2719-4fe0-9101-19cf4ee0c294#', 'https://google.qwiklabs.com/public_profiles/9fa9a3a8-dc22-49f9-9a61-967144f37f91', 'https://www.qwiklabs.com/public_profiles/1c7a19a7-7c25-4ab0-8200-800c0bc6b71c', 'https://google.qwiklabs.com/public_profiles/83b39641-be6e-413c-9d72-2a71cb4437c8', 'https://google.qwiklabs.com/public_profiles/d28b585d-f6df-4759-ac32-084064718d01', 'https://www.qwiklabs.com/public_profiles/ff9d504e-4c62-46cd-81cf-d372303b0ff2', 'https://www.qwiklabs.com/public_profiles/d007fea7-bb7d-4417-b364-94fe6a60a2d5', 'https://www.qwiklabs.com/public_profiles/20b41646-dcd9-479a-be6d-c6777c6a490e', 'https://google.qwiklabs.com/public_profiles/85929087-9909-41fc-b638-18416fb4b3e6', 'https://www.qwiklabs.com/public_profiles/49bdf2c2-aee6-4476-9d74-72227c1aaaf6', 'https://www.qwiklabs.com/public_profiles/1b6db191-edae-4f5d-81e3-2d2027f6f775', 'https://www.qwiklabs.com/public_profiles/0675bf5f-1d1e-4b5e-aac5-7a2f36402055', 'https://google.qwiklabs.com/public_profiles/9ff91d0d-f1a9-4f63-bf5d-123e43893cc8', 'https://www.qwiklabs.com/public_profiles/b362c6dc-9258-4cba-9d97-d9b5af352fc0', 'https://www.qwiklabs.com/public_profiles/35fa1606-2e07-426f-968e-e02c650184ee', 'https://www.qwiklabs.com/public_profiles/687fa209-744b-4d72-b61c-1d50395fa0bd', 'https://www.qwiklabs.com/public_profiles/ee78d8f8-ac76-4c2e-bc98-dce3004bbf8f', 'https://www.qwiklabs.com/public_profiles/026b4361-eb46-4ffd-a479-025f14ed53d3', 'https://www.qwiklabs.com/public_profiles/654a21a9-2929-42ed-a108-839db183ca82', 'https://google.qwiklabs.com/public_profiles/c3879a2c-0561-48d9-bf88-69c002c097d8', 'https://www.qwiklabs.com/public_profiles/6089ee97-e445-4c11-8839-2bb4448265b6', 'https://www.qwiklabs.com/public_profiles/c8a7127c-d9af-447b-b565-39c7c86feffa', 'https://www.qwiklabs.com/public_profiles/11fae5f1-0559-44c0-8c39-3f9b2ee91d4b', 'https://www.qwiklabs.com/public_profiles/c52e188f-200f-41af-8027-3ad8a783841a', 'https://qwiklabs.com/public_profiles/bb1dc92c-ceb1-493b-9955-b9400d60f933', 'https://google.qwiklabs.com/public_profiles/7675efd5-0c00-4b9c-8a38-94c87e0a8449', 'https://www.qwiklabs.com/public_profiles/17433411-974e-464c-aa59-28eca1b1544a', 'https://google.qwiklabs.com/public_profiles/e5e4ee2e-8a9e-44f7-9f9e-1338fb583bd7', 'https://www.qwiklabs.com/public_profiles/33285675-85b3-4a51-b117-ec77edde6081', 'https://www.qwiklabs.com/public_profiles/0713b9b2-3fbb-4d3d-82ba-0207721abe23', 'https://www.qwiklabs.com/public_profiles/3f7a2170-1f8e-413f-b0c4-4e11356e3a8a', 'https://google.qwiklabs.com/public_profiles/18987658-58d2-4d3d-b5e0-a17e976f644b', 'https://www.qwiklabs.com/public_profiles/c7f586aa-652a-4655-8a8f-1d64d4dad2cc', 'https://google.qwiklabs.com/public_profiles/591e78ff-8310-447a-9db4-1ff0188fe004', 'https://www.qwiklabs.com/public_profiles/b552d926-90ec-43d4-bb1b-d1e6713c2baa', 'https://google.qwiklabs.com/public_profiles/36bc21c7-2263-4564-ab5a-abbdfca62a81', 'https://www.qwiklabs.com/public_profiles/3b9fa07e-c59e-44f1-b538-3d876c1e0c98', 'https://www.qwiklabs.com/public_profiles/44836bab-f428-44a3-ab67-65164cfe9bee', 'https://google.qwiklabs.com/public_profiles/36e83809-6027-4777-ac98-5c902800e95d', 'https://www.qwiklabs.com/public_profiles/4232374e-01b8-4e05-8a28-4f6d93869b26', 'https://google.qwiklabs.com/public_profiles/08c2e7c6-79d4-4c21-b2d7-c74bb31501a1', 'https://www.qwiklabs.com/public_profiles/62021504-b35f-427f-abae-07c175731422', 'https://www.qwiklabs.com/public_profiles/f4c1560c-7a61-43c2-81c4-2c3b20cc78c4', 'https://www.qwiklabs.com/public_profiles/c20eb093-6947-49b6-a5ee-723629d33ffb', 'https://www.qwiklabs.com/public_profiles/737622c5-b009-4c44-b543-f90d5ee6af64', 'https://www.qwiklabs.com/public_profiles/a97b7f9b-95ac-402c-b09a-f363569d0543', 'https://www.qwiklabs.com/public_profiles/027d7d12-d45d-46a0-a9ca-ae34ae0cc957', 'https://www.qwiklabs.com/public_profiles/0a0104cd-2b6e-4876-a4c9-9045f580a44a', 'https://google.qwiklabs.com/public_profiles/f3848e28-0ce8-4a28-9a55-4dbd2263ce8e', 'https://google.qwiklabs.com/public_profiles/ba7d284f-3401-45c7-a719-4bd909ec2417', 'https://google.qwiklabs.com/public_profiles/f429a0aa-0ee9-4eb7-b0f9-f0849186f2d1', 'https://www.qwiklabs.com/public_profiles/b5b76fa8-f4f5-47a3-b87f-92afb12acf7d', 'https://www.qwiklabs.com/public_profiles/f6a88f11-1f6e-4431-9a53-ea4be88ecc84', 'https://google.qwiklabs.com/public_profiles/c42a3ce7-cd13-484e-80c6-6d09235f3ae8', 'https://www.qwiklabs.com/public_profiles/36c3d86e-4d5f-42d3-ab70-74febe21ead1', 'https://www.qwiklabs.com/public_profiles/0e6d1e96-df7d-444a-b2fb-e89a714595a8', 'https://www.qwiklabs.com/public_profiles/df43e4b2-104f-403a-a218-ddb306535df7', 'https://www.qwiklabs.com/public_profiles/d16e869f-6294-4040-adfe-bd7069a24420', 'https://www.qwiklabs.com/public_profiles/f24e30c4-b66e-4efd-baae-d1d6c2b2b0ac', 'https://www.qwiklabs.com/public_profiles/98e9a09e-0e97-404c-ab94-9dda9a268c67', 'https://google.qwiklabs.com/public_profiles/44f798c8-43f4-4ef7-bd0e-68dba479d271', 'https://www.qwiklabs.com/public_profiles/95cccd1a-e6d3-4612-83e3-c5c616359281', 'https://google.qwiklabs.com/public_profiles/efd1b99f-54ea-4133-8276-ce4374481dc0', 'https://run.qwiklabs.com/public_profiles/a6ae06e5-ca6c-401f-b134-5ecc3ad3ede4', 'https://www.qwiklabs.com/public_profiles/2a80151b-78b7-44a1-ab1c-8bd9af47f3cf', 'https://google.qwiklabs.com/public_profiles/6ab3a6c9-42a8-415d-a030-93155d82b66e', 'https://www.qwiklabs.com/public_profiles/a0aec15a-9c2a-458f-ab72-bbd6e572f58f', 'https://www.qwiklabs.com/public_profiles/9e9706eb-067c-4ae3-a9d1-c5632a4096a8', 'https://www.qwiklabs.com/public_profiles/48477abc-d0e4-4088-b0c4-66f36fa3db1f', 'https://google.qwiklabs.com/public_profiles/b098ae3c-303f-428b-a629-f18def22f6e3', 'https://google.qwiklabs.com/public_profiles/5b4e62d2-ce6c-4f65-9033-126a3054e1f6', 'https://www.qwiklabs.com/public_profiles/2444205f-804f-4392-9833-19c6034ad817', 'https://www.qwiklabs.com/public_profiles/2978e9d5-c6eb-489b-bf6f-511eed47426d', 'https://www.qwiklabs.com/public_profiles/084c2e19-f7a8-4319-a840-5e3c7905bb25', 'https://www.qwiklabs.com/public_profiles/25e8e649-86a4-41b7-acdd-e8946e31e2d3', 'https://www.qwiklabs.com/public_profiles/e3dc24ab-6494-44d2-9d4b-9c62e55357ba', 'https://google.qwiklabs.com/public_profiles/38f2950e-e62a-40fb-a88a-930138375961', 'https://www.qwiklabs.com/public_profiles/ac2ce5ec-570b-496c-a6cf-f895b56fc509', 'https://www.qwiklabs.com/public_profiles/c27cc8a1-2b31-4d8f-97e9-7984b2a36d29', 'https://www.qwiklabs.com/public_profiles/c297a75f-2f5e-4eed-9efc-3d528a3568dc', 'https://google.qwiklabs.com/public_profiles/15ca84fe-bc0b-4802-a03c-598e514c6a2e', 'https://www.qwiklabs.com/public_profiles/847aabbf-a39b-4288-bd8b-b3f6e61cbaf7', 'https://www.qwiklabs.com/public_profiles/d93857cd-abe6-46a1-be7d-26a657a5968f', 'https://google.qwiklabs.com/public_profiles/49079ef6-f3fb-427d-891f-e2559a205dda', 'https://www.qwiklabs.com/public_profiles/563e3146-1a3e-4e63-ae1d-a2daa32e8657', 'https://www.qwiklabs.com/public_profiles/dfce1a20-1df5-41e0-b7eb-e42efa8553a1', 'https://google.qwiklabs.com/public_profiles/481f32c2-cf80-4059-959f-255d75e9b9a6', 'https://www.qwiklabs.com/public_profiles/3e47958e-22a7-44c4-8eb6-ef88d84fc770', 'https://google.qwiklabs.com/public_profiles/70e031bc-e82c-405d-98df-cdf7ece30bd1', 'https://www.qwiklabs.com/public_profiles/77def105-33bb-4005-9cd6-bb20c417029a', 'https://www.qwiklabs.com/public_profiles/01dba269-4331-437b-b1fa-5c7907ac071a', 'https://www.qwiklabs.com/public_profiles/0c87a686-e1c5-436f-92f9-3c3a166b997a', 'https://google.qwiklabs.com/public_profiles/d95ef0e7-ba0d-48f3-8389-abf21432fb02', 'https://www.qwiklabs.com/public_profiles/62f45f1b-8a88-4f08-9958-4fe2dd62af0d', 'https://google.qwiklabs.com/public_profiles/bb870fb6-0a16-44a6-9ac1-960a56dfe0f9', 'https://google.qwiklabs.com/public_profiles/9c669717-104a-47ed-a925-a007a78da805', 'https://www.qwiklabs.com/public_profiles/8d945bdb-b31e-4060-adb1-dfcb2c4e0db3', 'https://www.qwiklabs.com/public_profiles/2605dea1-8236-4109-94ea-feb751fdbf39', 'https://www.qwiklabs.com/public_profiles/a8458aa5-2483-4443-b4a1-f164aaa49a23', 'https://www.qwiklabs.com/public_profiles/b7413437-1db4-460c-ad70-5f8a7fdda543', 'https://www.qwiklabs.com/public_profiles/dba5fa2d-a14b-4b87-80ae-dff178af6d40', 'https://www.qwiklabs.com/public_profiles/031a8431-fd20-41e4-b69f-10291d9a75db', 'https://www.qwiklabs.com/public_profiles/8670b7d6-458f-448a-8bdd-148bc448563d', 'https://www.qwiklabs.com/public_profiles/c9190b32-90cc-46cb-9a17-317a095f9843', 'https://www.qwiklabs.com/public_profiles/ad8a1cc6-9d5b-4fbe-9e24-2a6407ef4deb', 'https://www.qwiklabs.com/public_profiles/c7ed8298-6e2c-4b6a-9218-ab1fc3baff75', 'https://www.qwiklabs.com/public_profiles/41c7a527-661a-4629-996a-7b828e02f130', 'https://www.qwiklabs.com/public_profiles/07dec915-7a24-426a-9eee-eee53435850e', 'https://www.qwiklabs.com/public_profiles/024877ea-1544-47ce-bfd1-d14c611e48e3', 'https://www.qwiklabs.com/public_profiles/d5d21e56-11c5-4d7c-a36f-0c7e5f9795c7', 'https://google.qwiklabs.com/public_profiles/bac2eba4-202a-4024-8411-70bed222d05a', 'https://www.qwiklabs.com/public_profiles/b699681d-3e30-4433-b579-5ea8972d8164', 'https://www.qwiklabs.com/public_profiles/7c821c73-0069-4a00-84ce-be5717aebd80', 'https://google.qwiklabs.com/public_profiles/f37b436a-1c32-46cf-8bbd-74df71701f71', 'https://google.qwiklabs.com/public_profiles/d2c48ac6-f379-43c3-9ec0-f1a6fdedd2f4', 'https://www.qwiklabs.com/public_profiles/0ec6b8f4-817c-4e38-9dc5-0dcbaeb220de', 'https://google.qwiklabs.com/public_profiles/5d22e6ed-19ef-4ee4-8fcd-be889dcfca7c', 'https://google.qwiklabs.com/public_profiles/77218e9c-f3b0-47ee-90cc-1a6f5e950546', 'https://www.qwiklabs.com/public_profiles/59dff8df-ef63-4453-b905-b57613fbfa7c', 'https://www.qwiklabs.com/public_profiles/0166f5ba-3767-4925-91b9-80d46930b8f8', 'https://google.qwiklabs.com/public_profiles/278cbf04-7f44-45e7-8691-942ad0a5b382', 'https://google.qwiklabs.com/public_profiles/92350e04-d1cd-47ad-a08e-9de61f129ab6', 'https://www.qwiklabs.com/public_profiles/380db474-a817-4720-8d34-54da83d37d71', 'https://www.qwiklabs.com/public_profiles/17e137d2-915c-4232-aaeb-9b1970195ccb']



CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Cache-Control',
    'X-Requested-With',
]


CELERY_BEAT_SCHEDULE = {
    'generate-report': {
       'task': 'core.tasks.summary',
       'schedule': 1200.0,
    },

}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


django_heroku.settings(locals())
