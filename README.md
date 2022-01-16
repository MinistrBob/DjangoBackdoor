# DjangoBackdoor
Application for the organization of the backdoor in the software complex for developers

## For developer
### Update requirements (on Windows)
```
pip freeze | Out-File -Encoding UTF8 requirements.txt
```
### ENV
```python
SECRET_KEY = os.environ['DBD_SECRET_KEY']  # secret key for Django
DEBUG = os.environ['DBD_DEBUG_VALUE']  # TRUE, FALSE
ENVIRONMENT = os.environ['DBD_ENVIRONMENT']  # DEV, PROD
```
### Work with project
```commandline
# create project with scratch (done once)
django-admin startproject django_backdoor
mv django_backdoor src
cd src
python manage.py migrate
python manage.py runserver
python manage.py startapp ssh_client
python manage.py createsuperuser

# work with migrations
python manage.py makemigrations
python manage.py migrate
```