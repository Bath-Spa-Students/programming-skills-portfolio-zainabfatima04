#Turn your if-else chain from Exercise 5-4 into an if-elif else chain.
#•If the alien is green, print a message that the player earned 5 points.
#•If the alien is yellow, print a message that the player earned 10 points.
#•If the alien is red, print a message that the player earned 15 points.
#•Write three versions of this program, making sure each message is printed for the appropriate color alien.

#Version 1: Alien color is green (runs the if block)
alien_color = 'green'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    print("Player just earned 15 points for shooting the red alien.")

#Version 2: Alien color is yellow (runs the elif block)
alien_color = 'yellow'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    print("Player just earned 15 points for shooting the red alien.")

#Version 3: Alien color is red (runs the else block)
alien_color = 'red'

if alien_color == 'green':
    print("Player just earned 5 points for shooting the green alien.")
elif alien_color == 'yellow':
    print("Player just earned 10 points for shooting the yellow alien.")
else:
    print("Player just earned 15 points for shooting the red alien.")