'''
    This project was meant to solve the issue of calculating travel prices for a
    trip excursion, it involves getting the name of the tour guide, telling the 
    programm how many people are going and from that number calculate the total knowing
    how much it costs for one person
'''

adult_price = 1990      # per person

guide = input("Enter the surname of the guide:")
number_people = int(input("Number of adults in the group:"))

total = number_people * adult_price

# display the name of the guide and total cost of the group for the trip
print("Tour Guide", guide)
print("Total Price for the Trip:", total)