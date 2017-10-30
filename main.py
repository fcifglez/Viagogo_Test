#! /usr/bin/python

import os
import sys

from events import get_closest_events, X_MAX_COORDINATES, Y_MAX_COORDINATES


"""
Function set_input_coordinates().

:returns: a dict, with the coordinates the user has inserted in the terminal.
"""
def set_input_coordinates():
	
	try:
		x_val = int(raw_input("Enter coordinate 'x' in a range [-{0}, {0}]: "\
			.format(X_MAX_COORDINATES)))

		if (x_val < (X_MAX_COORDINATES*-1)) or (x_val > X_MAX_COORDINATES):
			print "ERROR: Coordinate 'x' is not in the range [-{0}, {0}]"\
				.format(X_MAX_COORDINATES)
			raw_input("\nPress Enter to continue.")
			return None

		y_val = int(raw_input("Enter coordinate 'y' in a range [-{0}, {0}]: "\
			.format(Y_MAX_COORDINATES)))

		if (y_val < (Y_MAX_COORDINATES*-1)) or (y_val > Y_MAX_COORDINATES):
			print "ERROR: Coordinate 'y' is not in the range [-{0}, {0}]"\
				.format(Y_MAX_COORDINATES)
			raw_input("\nPress Enter to continue.")
			return None
	except:
		print "ERROR: The coordinates must been a NUMBER."
		raw_input("\nPress Enter to continue.")
		return None

	return {'x_coord': x_val, 'y_coord': y_val}


coordinates = None
while coordinates == None:

	os.system('cls' if os.name == 'nt' else 'clear')

	print "############################################################"
	print "#####################      MENU      #######################"
	print "############################################################\n"
	print "Select an option: "
	print " 1. Insert coordinates. "
	print " 0. Exit program. "
	option = raw_input("-----> ")
	
	if option == '1':
		coordinates = set_input_coordinates()
	elif option == '0':
		os.system('cls' if os.name == 'nt' else 'clear')
		sys.exit()
	else:
		coordinates = None

# Get closest_events based in your location.
get_closest_events(coordinates['x_coord'], coordinates['y_coord'])
