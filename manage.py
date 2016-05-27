#!/usr/bin/env python
import os
import sys


'''
///////
Manage.py is a commandline utility
that allows one to interact
with Django in various ways
///////
'''

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
