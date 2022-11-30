import random

lives = 6
# ammount of lives
hangman_list = ["apple","cherry","brasil","panda","world"]

word = random.choice(hangman_list)
print(f"this is the word: {word}")

print(f"current lives: {lives}")



#this section will break the word donw to just letters 
split_word = [*word]
print(split_word)

#this section will be for the player to guess the letters in the word
guess = input("guess the letter: ")
#while lives != 0:
for x in range(6):
  for element in split_word:
    if guess == element:
      print(f"good, this is the guess: {guess}")
      pass
    elif guess != element:
      return "try again, nerd"
    lives = lives - 1
  



# this section will count the number of letters in the chosen word
length_of_word = len(word)
print(f"this is the length of the word: {length_of_word}")

# this section is creating a list of underscores based on length
underscore_list = []
for element in split_word:
  underscore_list.append("_")
print(underscore_list)

