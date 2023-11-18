#Think of at least five places in the world you’d like to visit. 
#• Store the locations in a list. 
#Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse() to change the order of your list. 
#Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. 
#Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. 
#Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse alphabetical order. 
#Print the list to show that its order has changed.

#Define a list of places to visit
places_to_visit = ["Tokyo", "Reykjavík", "Berlin", "Amsterdam", "Istanbul"]

#Print the list in its original order
print("Original order:", places_to_visit)

#Use sorted() to print the list in alphabetical order without modifying the actual list
print("Sorted in alphabetical order:", sorted(places_to_visit))

#Show that the original list is still in its original order
print("Original order after sorted():", places_to_visit)

#Use sorted() to print the list in reverse alphabetical order without changing the original order
print("Sorted in reverse alphabetical order:", sorted(places_to_visit, reverse=True))

#Show that the original list is still in its original order
print("Original order after sorted() in reverse:", places_to_visit)

#Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

#Use reverse() again to revert the order back to its original
places_to_visit.reverse()
print("Original order after reverse():", places_to_visit)

#Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Sorted order:", places_to_visit)

#Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse sorted order:", places_to_visit)