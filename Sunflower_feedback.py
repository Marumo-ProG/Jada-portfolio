'''
    this project was meant to demonstrate how strings work in python by creating a 
    feedback project that allows the user to give feedback and the program will 
    look for certain words, cut some senetences out and also convert the feedback to all 
    lower case to find words well
'''

feedback = input("Please give us feedback on Sunflower complex:")

# getting the first letter in feedback
print("This is the first letter in feedback:", feedback[0])

# getting the length of the feedback to give the user with high feedback discounts
length = len(feedback)
print("Length of feedback:", length, "characters")

# converting the letter of feedback to lower case
feedback = feedback.lower()

# seraching for words like comfy and cozy in the feedback
search_cozy = feedback.find("cozy")
search_comfy = feedback.find("comfy")
search_menu = feedback.find("menu")
search_food = feedback.find("food")

# show the words we searched for
print("Cozy word:", search_cozy)
print("Comfy word:", search_comfy)
print("Menu word:", search_menu)
print("Food word:", search_food)

# cutting out the first sentence
full_stop = feedback.find(".")
sentence1 = feedback[0:full_stop+1]
print("first Sentence:", sentence1)