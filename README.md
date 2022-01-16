# DjangoBackdoor
Application for the organization of the backdoor in the software complex for developers

## For developer
### Update requirements (on Windows)
```
pip freeze | Out-File -Encoding UTF8 requirements.txt
```
### Create project
```commandline
django-admin startproject django_backdoor
mv django_backdoor src
cd src
python manage.py migrate
python manage.py runserver
python manage.py startapp ssh_client
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```