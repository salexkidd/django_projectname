#-*- coding:utf-8 -*-
"""
project name valiable to settings.py
"""
from django.conf import settings

DEFAULT_PROJECT_NAME = "Django Project(Please set settings.PROJECT_NAME)"


def project_name(request, *args, **kwargs):
    """
    Set project_name to context
    """
    project_name = DEFAULT_PROJECT_NAME

    if hasattr(settings, "PROJECT_NAME"):
        project_name = settings.PROJECT_NAME

    return {'project_name': project_name}
