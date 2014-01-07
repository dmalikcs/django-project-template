from fabric.api import local
import os
import sys
from fabric.contrib import django
sys.path.append(os.getcwd())
django.project("{{ project_name }}")


def setup():
    src_static = "%s/static/" % os.getcwd()
    dst_static = "%s/%s/%s" % (os.getcwd(), os.pardir, "static")
    src_media = "%s/media/" % os.getcwd()
    dst_media = "%s/%s/%s" % (os.getcwd(), os.pardir, "media")
    local("ln -s %s %s" % (src_static, dst_static))
    local("ln -s %s %s" % (src_media, dst_media))
