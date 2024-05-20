'''
    this is a recommendation system for a store which uses conditional statements
    and logical operators
'''

print("Hello :-), this are the categories of products we have, please choose one:")
print("1. Vegetables")
print("2. Fruits")
print("3. Meat")
print("4. Dairy")

choice = int(input("Please a category above to get recommendation:"))

if choice == 1:
    print("We recommend Brocolli")
elif choice == 2:
    print("We recommend Mango")
elif choice == 3:
    print("We recommend Beef Steak")
elif choice == 4:
    print("We recommend yogurt")
else: 
    print("Please a valid Category :-)")

print("Thanks for shopping with us, have a great day")
