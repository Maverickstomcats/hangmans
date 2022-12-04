import random

# ammount of lives
lives = 6

# choosing a word for the user to find
hangman_list = ["apple","cherry","brasil","panda","world"]
word = random.choice(hangman_list)
print(f"this is the word: {word}")
print(f"current lives: {lives}")

#this section will break the word down to just letters 
split_word = [*word]
print(split_word)

# this section is creating a list of underscores based on length
underscore_list = []
for element in split_word:
  underscore_list.append("_")
print(underscore_list)

# this section will count the number of letters in the chosen word
length_of_word = len(word)
print(f"this is the length of the word: {length_of_word}")

# This code function is taken from https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/  
# this is code for finding all insatnces of a character in a word (list)
def get_index_positions_2(split_word, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    for i in range(len(split_word)):
        if split_word[i] == element:
            index_pos_list.append(i)
    return index_pos_list
# index_pos_list = get_index_positions_2(split_word, guess)
# print(f"Indexes of all occurrences of {guess} in the list are : {index_pos_list}")
# end of taken code

# actual guessing process (game)

guess = input("guess the letter: ")
index_pos_list = get_index_positions_2(split_word, guess)
print(f"Indexes of all occurrences of {guess} in the list are : {index_pos_list}")
while lives > 0: 
  for element in split_word:
    if guess != element in split_word:
      lives -= 1
      print(f"You now have {lives} lives left. Try again.")
    elif guess == element:
      print(f"good, this is the guess: {guess}")
    # index = ""
    # for guess in split_word:
      underscore_list.pop(index_pos_list[0])
      underscore_list.insert(index_pos_list[0], guess)
      print(underscore_list)


# note from angel 7:56 pm 12/3/22:
    # I tried to get code to find all the occurences of a certain guess. The code will return 
    # the indexes of a letter if it appears more than once in the split_word.
    # This way, when our code replaces the underscore_list with our guess, it will replace
    # all letters and not just one instance. 


  #However, this is getting too complex and I think i will get rid of the code some other day.

