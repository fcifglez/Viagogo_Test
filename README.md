# Viagogo Developer Test App

* Your program should randomly generate seed data.
* Your program should operate in a world that ranges from -10 to +10 (Y axis), and -10 to +10 (X axis).
* Your program should assume that each co-ordinate can hold a maximum of one event.
* Each event has a unique numeric identifier (e.g. 1, 2, 3).
* Each event has zero or more tickets.
* Each ticket has a non-zero price, expressed in USDollars.
* The distance between two points should be computed as the Manhattan distance.

## How to execute

* You need to have Python 2.7 or bigger installed.

* To execute the program, write in the terminal:
```
python main.py
```

*  Follow the instructions the terminal will give you.

## How might you change your program if you needed to support multiple events at the
same location?

* Go to the 'config.json' file.
* Change the value 'max_per_coord' for the number of events you want.

## How would you change your program if you were working with a much larger world
size?

* Go to the 'config.json' file.
* Change the values 'x_max_coordinate' and 'y_max_coordinate' for the size you want.

## Assumptions

* World
  * Coordinates are integer values.
  * Coordinates	have the same range positive to negative in same axis.


* Events
  * There is an event also if there are zero tickets.


* Tickets
  * There are a random number of tickets from 0 to MAX_TICKETS
  * The Tickets prices are $1 to $MAX_TICKETS_PRICE. 
  * Each ticket has to have an ID.
