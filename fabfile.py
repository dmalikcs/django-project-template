from fabric.api import local


def installapp(app_name=None, app_type=None):
    if app_type == 'tastypie':
        template = 'https://github.com/dmalikcs/django-tastypie-app-template/archive/master.zip'
    elif app_type == 'celery':
        template = 'https://github.com/dmalikcs/django-celery-app-template/archive/master.zip'
    else:
        template = 'https://github.com/dmalikcs/django-app-template/archive/master.zip'
    local("python manage.py startapp --template=%s %s" % (template, app_name, ))
