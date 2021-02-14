import slack
import datetime
import os
from yaml import FullLoader, load as yamlLoad
from random import choice, randint
from titlecase import titlecase
from time import sleep

TOKEN = os.environ['SLACK_WORKSTATION_TOKEN']
CHANNEL = os.environ['SLACK_CHANNEL']

with open('exercises.yml') as f:
	exercises_raw = yamlLoad(f, Loader=FullLoader)

# Put into format ---
# {level: { exercise: {type: type} }}
exercises = { k: { x:{'type':type} for type,v in data.items() for x in v }  for k,data in exercises_raw.items()  }
'''
Equivalent Code
exercises = {}
for k,data in exercises_raw.items():
	exercises[k] = {}
	for type, v in data.items():
		for x in v:
			exercises[k][x] = {'type': type}

'''

# Load the rep / time data
with open('reps.yml') as f:
	reps = yamlLoad(f, Loader=FullLoader)

while True:

	# Get date information and perform checks
	day_of_week = datetime.date.today().weekday() # 0 is Monday, 6 is Sunday
	time = datetime.datetime.now().time()

	# Check it is a weekday
	if not day_of_week < 5:
		print("Not a weekday, sleeping for 6 hours")
		sleep(21600)
		continue

	# Chcck it is inside working hours
	if not (time > datetime.time(8) and time < datetime.time(18,00)):
		print("Outsode of working hours, sleeping for an hour")
		sleep(3600)
		continue

	# Get exercise data
	levels = list(exercises.keys())
	level = choice(levels)
	exercise = choice(list(exercises[level].keys()))

	# Get the number of reps / time of exercise
	type = exercises[level][exercise]['type']
	num = randint(reps[level][type]['min'], reps[level][type]['max'])

	messages = {
		'reps': f"Here's a {level} one, {num} {titlecase(exercise)}",
		'time': f"Here's a {level} one, {titlecase(exercise)} for {num} seconds"
	}

	# Create new slack client object
	client = slack.WebClient(token=TOKEN)

	print(f"Sending message - {messages[type]} ")
	# Send the message
	client.chat_postMessage(channel=CHANNEL, text=messages[type])

	# Get a random sleep till the next exercise
	# Between 20 and 40 minutes
	random_wait = randint(20, 40)
	print(f"Sleeping for {random_wait} minutes")
	sleep(random_wait * 60)
