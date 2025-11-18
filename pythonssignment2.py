 
integer_list = input(f'Enter a list of integers :')
sum_all_integer_list = sum(map(int, integer_list.split(',')))
print(f'Sum of all integers in the list : {sum_all_integer_list}')

fav_books = ("Deck the Halls", "Fathers of Nations", "Bonnie" , "Sins of the Fathers", "Wayward")
  
for book in fav_books:
    print(book)


persons_details = {}
persons_details['Name'] = input('Name: ')
persons_details['Age'] = input('Age: ')
persons_details['Favouritecolor'] = input('Favouritecolor: ')

print(persons_details)

set1_integers = set(map(int, input('Enter integers for set 1 (comma-separated): ').split(',')))
set2_integers = set(map(int, input('Enter integers for set 2 (comma-separated): ').split(',')))


common_integers = set1_integers.intersection(set2_integers)
print(f'Common integers: {common_integers}')

words = input('Enter words (comma-separated): ').split(',')

odd_char_words = [word.strip() for word in words if len(word.strip()) % 2 == 1]

print(f'Words with odd number of characters: {odd_char_words}')
