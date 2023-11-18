#A Python dictionary can be used to model an actual dictionary. 
#However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. 
#Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. 
#You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.    

#Create a glossary with programming words and their meanings
programming_glossary = {
    'variable': 'A container for storing data values.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A way to repeatedly execute a set of statements.'
}

#Print each word and its meaning with a newline between each pair
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")