from django.test import TestCase
from datetime import datetime


str_time = '2022-02-05'

obj = datetime.strptime(str_time, '%Y-%m-%d')


