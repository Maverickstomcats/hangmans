import random
#process to choose word, lists, splitttign and guess
# ammount of lives
lives = 6

# choosing a word for the user to find
hangman_list = ["apple","cherry","brasil","panda","penaldo"]
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

# +++++++++++++++++++++++++++++actual guessing process (game)++++++++++++++++++++++++++

guess = input("guess the letter: ")
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

# while lives > 0: 
for element in split_word:
  if guess not in split_word:
    lives -= 1
    print(f"You now have {lives} lives left. Try again.")
  # elif guess == element:
  #   print(f"good, this is the guess: {guess}")
  # index = ""
  elif guess in split_word:
        # Find all occurences of user's guess in word
    occurences = findOccurrences(split_word, guess)
        # For each occurence, replace that dash in the string with the correct letter
    for index in occurences:
      hidden_word = split_word[:index] + guess + split_word[index + 1:]
    print(f"hidden_word")
        # Return the updated hidden_word
    print(f"good, this is the guess: {guess}")
    #TypeError: can only concate list (not"str" to list :(

