Pinax Project Symposion
========================

[![Join us on Slack](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


Pinax
--------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.


pinax-project-symposion
------------------------

`pinax-project-symposion` is a starter project demonstarting a minimal symposion instance.


Getting Started
-------------------

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.7.1
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-symposion/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py loaddata fixtures/*
    python manage.py runserver


Usage
-------

    django-admin.py startproject --extension=py,json --template=https://github.com/pinax/pinax-project-symposion/zipball/master <project_name>


Documentation
---------------

The pinax-project-symposion documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack channel and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Code of Conduct
------------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/.


Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at [@pinaxproject](https://twitter.com/pinaxproject) and check out our blog http://blog.pinaxproject.com.



