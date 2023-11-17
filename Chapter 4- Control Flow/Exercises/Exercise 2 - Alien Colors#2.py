#Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•Write one version of this program that runs the if block and another that runs the else block.

#Version 1: Alien color is green (runs the if block)
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")

#Version 2: Alien color is not green (runs the else block)
alien_color = 'red'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the alien.")
else:
    print("Player just earned 10 points.")