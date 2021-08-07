import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic_project.settings")

import django
django.setup()


#Fake data script:
import random
from basic_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ["search", "shopping", "news", "games", "social"]


def add_topic():
	t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
	t.save()
	return t


def populate(n = 5):

	for entry in range(n):
		#generating fake data:
		top = add_topic()
		fake_url = fakegen.url()
		fake_name = fakegen.company()
		fake_date = fakegen.date()

		#now inserting data in models:
		webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]
		accrec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]


if __name__ == "__main__":
	print("starting population script")
	populate(20)
	print("population complete")






