# Viagogo Developer Test App

* Your program should randomly generate seed data.
* Your program should operate in a world that ranges from -10 to +10 (Y axis), and -10 to +10 (X axis).
* Your program should assume that each co-ordinate can hold a maximum of one event.
* Each event has a unique numeric identifier (e.g. 1, 2, 3).
* Each event has zero or more tickets.
* Each ticket has a non-zero price, expressed in USDollars.
* The distance between two points should be computed as the Manhattan distance.


## Assumptions

* World 	--->	Coordinates are integer values.
			--->	Coordinates	has same range positive to negative in same axis.


* Events 	--->	There is at least one event is the world coordinate is True.
			--->	There is an event also if there is zero tickets.



* Tickets	--->	There are random number of tickets from 0 to MAX_TICKETS
			--->	The Tickets prices are $1 to $MAX_TICKETS_PRICE. 
			---> 	Each ticekts has to have an ID.
