import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JOBPORTALPROJECT.settings')
import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *
faker = Faker()
icity = ['mumbai','banglore','chennai','bhopal','kolkata','hydrabad']
post = ['software-devloper','devloper','Senior-Assistant','Accounts-Officer','Superintendent']

def populate(n):
	for i in range(n):
		fcity = faker.word(ext_word_list = icity)
		fcompany = faker.company()
		fpost = faker.word(ext_word_list = post)
		femail = faker.email()
		faddress = faker.address()
		emp_rcd = CityJobs.objects.get_or_create(city = fcity,company = fcompany,designation = fpost,
												email = femail,address = faddress,slug = fcompany)

populate(10)
