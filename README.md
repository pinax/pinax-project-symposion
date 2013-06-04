pinax-project-symposion
=====================

a starter project demonstarting a minimal symposion instance


Usage:

    django-admin.py startproject --extension=py,json --template=https://github.com/pinax/pinax-project-symposion/zipball/master <project_name>

Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.4.5
    django-admin.py startproject --extension=py,json --template=https://github.com/pinax/pinax-project-symposion/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py loaddata fixtures/*
    python manage.py runserver
