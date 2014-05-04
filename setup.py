#-*- coding:utf-8 -*-
from distutils.core import setup

VERSION = "1.0.0"
AUTHOR = "salexkidd"
AUTHOR_EMAIL = "salexkidd@gmail.com"

short_description = 'django projectname'
long_description = 'django projectname'

classifiers = [
    'Development Status :: 3 - Alpha',
    "Topic :: Software Development :: Debuggers",
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2.7',
    "Framework :: Django",
]

setup(
    name             = "django-projectname",
    version          = VERSION,
    description      = short_description,
    long_description = long_description,
    author           = AUTHOR,
    author_email     = AUTHOR_EMAIL,
    url              = 'https://github.com/salexkidd/django_projectname',
    keywords         = 'django,projectname',
    license          = "BSD",
    packages         = ['django_projectname'],
    classifiers      = classifiers,
)
