#Tidy up the code to make it easier to understand.
#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
#Make sure you use each character combination, “\t” and “\n”, at least once.
#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

#Variable representing a person's name with whitespace characters
name = "\t    Marilyn Monroe\n"

#Print the name with whitespace around it
print("Original Name:")
print(f'"{name}"')

#Print the name using each stripping function
print("\nAfter Stripping:")
print(f'Left Stripped: "{name.lstrip()}"')
print(f'Right Stripped: "{name.rstrip()}"')
print(f'Stripped from both sides: "{name.strip()}"')