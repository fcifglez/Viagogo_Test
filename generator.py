#! /usr/bin/python

import json
import sys

from random import getrandbits, random


# Open config file
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

# Set the config file values and check they have the appropriate values.
try:
	X_MAX_COORDINATES = int(config['World']['x_max_coordinate'])
	Y_MAX_COORDINATES = int(config['World']['y_max_coordinate'])

	MAX_EVENTS = int(config['Events']['max_per_coord'])
	MAX_EVENTS_TO_FIND = int(config['Events']['max_to_find'])

	MAX_TICKETS = int(config['Tickets']['max_per_event'])
	MAX_TICKETS_PRICE = int(config['Tickets']['max_price'])

except:
	print "\nERROR: The config file has no NUMBER values.\n"
	sys.exit()


"""
Function generate_wolrd().

:returns: a World dict, which has the the Events data of each coordinate.
"""
def generate_world():

	# Init World with True and False (Events or no Events)
	# Coordinates const multiple by 2 because has also negative coordinates.
	world = [[bool(getrandbits(1)) for x in range(X_MAX_COORDINATES * 2)] \
				for y in range(Y_MAX_COORDINATES * 2)]

	# Init Event IDs
	event_id_count = 1

	# Generate World data
	for x in range(len(world)):
		for y in range(len(world[x])):
			if world[x][y]:
				world[x][y] = __generate_event(event_id_count)
				event_id_count += len(world[x][y]['Events'])
			else:
				world[x][y] = {'Events': 'No Events.'}

	return { 'World': world }


"""
Function __generate_event().

:param event_id_count: Event counter to assing his ID.
:returns: a Events dict, which has the data of each event. (ID and Tickets) 
"""
def __generate_event(event_id_count):

	# At least one event if world coordinates are True
	n_events = int( (random() * MAX_EVENTS) + 1 )

	# Generate Events data
	events = []
	for e in range(n_events):
		event = {'event_id': event_id_count, 'tickets' : __generate_tickets()}
		event_id_count += 1
		events.append(event)

	return {'Events': events}


"""
Function __generate_tickets().

:returns: a Tickets dict, which has the data of each ticket. (ID and price) 
"""
def __generate_tickets():
	
	# Generate Tickets data
	tickets = [{'ticket_id': t, \
				'price': int((random() * MAX_TICKETS_PRICE) + 1) } \
				for t in range( int((random() * MAX_TICKETS) + 1) ) ]

	# Sort ticket by price, cheapest first.
	tickets = sorted(tickets, key=lambda ticket: ticket['price'])
	
	return tickets
