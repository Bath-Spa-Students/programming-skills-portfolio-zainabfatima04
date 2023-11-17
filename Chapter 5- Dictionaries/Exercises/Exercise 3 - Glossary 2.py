#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms to your glossary. 
#When you run your program again, these new words and meanings should automatically be included in the output.

#Create a glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A way to repeatedly execute a set of statements.'
}

#Loop through the dictionary and print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")

#Add five more Python terms to the glossary
programming_glossary.update({
    'module': 'A file containing Python code that can be imported and used in another program.',
    'tuple': 'An immutable ordered collection of elements.',
    'class': 'A blueprint for creating objects with common attributes and behaviors.',
    'inheritance': 'A mechanism to create a new class using properties of an existing class.',
    'exception': 'An event that occurs during the execution of a program that disrupts the normal flow.'
})

#Print the updated glossary using the same loop
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")