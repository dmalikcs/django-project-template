from fabric.api import local


def installapp(app_name=None):
    template = 'https://github.com/dmalikcs/django-app-template/archive/master.zip'
    local("python manage.py startapp --template=%s  %s" % (template, app_name, ))
