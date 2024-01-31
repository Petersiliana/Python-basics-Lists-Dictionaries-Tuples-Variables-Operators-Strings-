# 1. Create a list of names and print the second item.

list_of_names = ["Anna", "John", "Paul"]
print(list_of_names[1])

# 2. Create a list of sports and then replace the second item with another sport.

list_of_sports = ["tennis", "football", "handball"]
list_of_sports[1] = "jogging"
print(list_of_sports)

# 3. Create a list containing numbers and delete the fifth number from the array.

list_of_numbers = [2, 5, 8, 9, 34]
del list_of_numbers[4]
print(list_of_numbers)

# 4. Create two lists of numbers and merge them.

list_of_numbers_1 = [5, 7, 23]
list_of_numbers_2 = [7, 85, 23, 4, 6, 8]
merge_lists = list_of_numbers_1 + list_of_numbers_2
print(merge_lists)

# 5. Create a list of numbers and find the length, minimum, and maximum.

list_of_numbers_3 = [5, 8, 23, 65, 97]
print(max(list_of_numbers_3))
print(min(list_of_numbers_3))
print(len(list_of_numbers_3))

# 6. Create a dictionary of students and scores and print out a student’s score.

students = {'bob':5, 'anna':3, 'miriam':4}
print(students["anna"])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.

people = {'bob':34, 'anna':18, 'miriam':24}
del people['anna']
print(people)

# 8. Create a dictionary of names and ages and then print out all the keys and values

people_2 = {'bob':34, 'anna':18, 'miriam':24}
print(people_2.keys())
print(people_2.values())
# 9. Create a tuple of your favorite movies

movies = ("Inception", "Prestige", "Diuna", "Harry Potter")
print(movies)

# 10. Create a tuple and print all the items from the first to third.

items = ("first_item", "second_item", "third_item", "fourth_item")
print(items[0:3])