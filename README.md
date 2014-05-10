=====================================
Django projectname context processor
=====================================

Usage
================================================================================

Add settings TEMPLATE_CONTEXT_PROCESSORS  
-----------------------------------------

Add django_projectname context processor to CONTEXT_PROCESSORS.
    
    from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
        TEMPLATE_CONTEXT_PROCESSORS = TCP + (
      .
      .
      'libs.django_projectname.context_processors.project_name'
      .
    )
- set to PROJECT_NAME to settings.py
  PROJECT_NAME = "Please set your Porject Name"

- use {{project_name}} template tag to your template!
  Welcome to {{project_name}}!!
