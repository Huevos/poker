Poker hand evaluator

http://bokehman.satellites-xml.org/poker_calculator/

There are three packages here, each one with a working example file:

BruteForceSearch() runs an exhaustive search on multiple players and 
returns a 100% accurate result. (Note: Python is not known for its speed 
so exhaustive searches pre-flop where several million hands must be tested 
makes this method prohibitive. Post-flop where the numbers are lower -less 
than 1000- there is no noticable delay.) Tested on a 2010 Xeon E5620 this 
Python version managed 564185 evaluations per second, (1.78 usec per eval).

RunSimulation() runs a simulation of n number of hands on multiple players 
and returns a reasonably accurate result.

NameHand() takes an integer (returned by the evaluator) and converts it into 
a hand name. 
