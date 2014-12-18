pinax-project-symposion
=====================

a starter project demonstarting a minimal symposion instance


Usage:

    django-admin.py startproject --extension=py,json --template=https://github.com/pinax/pinax-project-symposion/zipball/master <project_name>

Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.7.1
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py loaddata fixtures/*
    ./manage.py runserver
