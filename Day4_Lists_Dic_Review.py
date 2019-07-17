import address_book
favorite_foods = ["Sushi", "Pizza", "Salmon", "Tamales dulces", "Yuca fries", "Apple pie", "Katsu curry", "Shrimp and grits", "Waffles"]
#1. Print the 3rd value of the list


#2. Print the first 4 values of the list



#3. Use range to print out all values in the list



#4. Here's a list of all of Alex's favorite foods. For each food in the list, print out a statement that says "I really love _____" and then fill in the blank with each.



# 5. Now for each food in that list, let's be specific about how MUCH Alex likes them.
# For example, print out "Alex's #1 favorite food is Sushi" and then "Alex's #2 favorite food is Pizza" and so on until you've made an ordered list.
# This can be done a number of different ways, but the easiest is probably by iterating over each index in the favorite_foods list using a function called "range". Try to find it in the documentation.




#Dictionaries!
# Here's a small dictionary of favorite books, each keyed to a different person.
favorite_books = {
  "diana": "Crime and Punishment",
  "sophie": "The Secret History",
  "cory": "Fahrenheit 451",
  "gabe": "The Hobbit",
  "danny": "Lonesome Dove",
  "dan": "Don Quixote",
  "katie": "10:04",
  "zara": "Rebecca",
  "david": "The Sun Also Rises",
  "alexandra": "Hyperbole and a Half",
  "martin": "The House on Mango Street",
  "jeff": "The Hitchhiker's Guide to the Galaxy"
}

# 6. Before we get started, lets adjust a few things. First off, Jeff just read a new book called "The Martian" and loved it. With just one line of code, change Jeff's favorite book to "The Martian"




# 7. We should also add Ronald to the list. His favorite book is "Lies my History Teacher Told Me."
#    Add that info to the dictionary as a new key-value pair.



# 8. Now let's start iterating. For each person in the dictionary, print out a statement that says "___'s favorite book is ____" and fill in the blanks with that person's name and that person's favorite book.






import address_book
# LEVEL 2: In the address_book.py file, there's a list called "contacts" with 100 dictionaries inside of it. Each dictionary representes a person, and has that person's name, phone number, email, the company they work for, and their address.
#    That means you could print the 7th person's email using this line of code:
#    print(address_book.contacts[6]["email"]) # Uncomment this to see if it works. (Remember, list indexing starts at zero, so we use the number 6 to access the 7th name).

# 9. Print out the name and phone number of the first person in the contacts list in the following format:
#    "_____ can be reached at ______" filling in the blanks with the person's name and phone number.




# 10. Print out the same information "_____ can be reached at ______" with names and phone numbers for all 100 of our contacts.








# 11. We're going to send a mass text to all our contacts, so we need everyone's phone number. Our texting program can do it in an instant if we put all the numbers into a list.
#    Create a list called phone_numbers, iterate over our contacts, and add each person's number to that list. Print out the list when you're done to check your work.







# 12. If we wanted to send an email that was only useful for college students and their professors, we could send that email ONLY to folks in our contacts whose email addresses end in ".edu".
#    Create a list called edu_emails and put every .edu email address from our contacts into that list. Print the list when you're done to check your work.
