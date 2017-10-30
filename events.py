#! /usr/bin/python

from generator import generate_world, X_MAX_COORDINATES, Y_MAX_COORDINATES, \
						MAX_EVENTS_TO_FIND


"""
Function manhattan_distance().

:param x: x coordinate where the loop is working.
:param y: y coordinate where the loop is working.
:param x_coord: x coordinate the user inserted it in the terminal.
:param y_coord: y coordinate the user inserted it in the terminal.
:returns: the manhattan distance between two coordinates.
"""
def manhattan_distance(x, y, x_coord, y_coord):
	m_distance = abs((x)-(x_coord)) + abs((y)-(y_coord))
	return int(m_distance)


"""
Function fit_world_ranges().

:param val: the coordinate the user inserted in the terminal.
:param dist: the actual dist the loop is working on.
:param max_range: max the coordinate in the world.
:returns: a dict, with the coordinates fitted inside the world framework.
"""
def fit_world_ranges(val, dist, max_range):
	
	# Prepare start range
	start = val - dist
	if start < 0: 
		start = 0
	elif start > max_range:
		start = max_range
	
	# Prepare stop range
	stop = val + dist + 1
	if stop < 0: 
		stop = 0
	elif stop > max_range:
		stop = max_range

	return {'start': start, 'stop': stop}


"""
Function get_events_at_coord().

:param events: all the events there are in a specific coordinate.
:param counter: counter of how many events the program has found.
:param dist: the actual dist the loop is working on.
:returns: how many events have been found in a coordinate.
"""
def get_events_at_coord(events, counter, dist):

	for e in events:
		if counter >= 5: # This break here is in case there are more than two
			break		 # events per coordinate.

		print "Event {0} - ${1}, Distance {2}".format(\
				e['event_id'], e['tickets'][0]['price'], dist)
		counter += 1

	return counter


"""
Function get_closest_events().

:param x_coord: x coordinate the user inserted in the terminal.
:param y_coord: y coordinate the user inserted in the terminal.
:returns: print the closest events.
"""
def get_closest_events(x_coord, y_coord):

	# Generate random World
	w = generate_world()

	# Check from the smallest to the biggest area until it finds 5 events.
	dist = 0
	max_dist = (X_MAX_COORDINATES * 2) + (Y_MAX_COORDINATES * 2)
	event_counter = 0

	while ( dist <= max_dist and event_counter < MAX_EVENTS_TO_FIND ):
		x_range = fit_world_ranges(x_coord, dist, X_MAX_COORDINATES * 2)
		y_range = fit_world_ranges(y_coord, dist, Y_MAX_COORDINATES * 2)
		
		for x in range(x_range['start'], x_range['stop']):
			for y in range(y_range['start'], y_range['stop']):
				events = w['World'][x][y]['Events']
				manhattan_dist = manhattan_distance(x, y, x_coord, y_coord)

				if manhattan_dist == dist and events != 'No Events.'\
				 and event_counter < 5:
					# print "X: {0}. Y: {1}".format(x,y)
					event_counter = get_events_at_coord(events, \
						event_counter, dist)

		dist += 1
