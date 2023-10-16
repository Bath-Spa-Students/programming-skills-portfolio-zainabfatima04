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