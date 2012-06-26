MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=sorokin_test2.sorokin_test2.settings $(MANAGE) test accounts

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=sorokin_test2.sorokin_test2.settings $(MANAGE) runserver 0.0.0.0:8000
