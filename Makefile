MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=sorokin_test2.sorokin_test2.settings $(MANAGE) test accounts
	