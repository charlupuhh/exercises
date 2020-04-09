from random_word import RandomWords

r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true").lower() #create word
while "-" in word: #make sure word doesn't have '-'
    word = r.get_random_word(hasDictionaryDef="true")
print(word)
gallows = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



guessed_wrong = 0
guessed_word = []
guessed_letters = []
game_over = False
word_range = (range(len(word)))
for i in word_range:
    guessed_word.append('_')

def gameCheck(): #check if the game is over
    global game_over
    if guessed_wrong == 6:
        print("You have too many incorrect guesses, the word was % s better luck next time"% word)
        game_over = True
        print(gallows[6])
    elif '_' not in guessed_word:
        print("You have guessed the word, congratulations!")
        print(word)
        game_over = True

print("Welcome to Hangman, you will have 6 guesses to try and guess the word. You may either guess a letter or the whole word")
print("Here is your starting board")

while game_over == False:
    print(gallows[guessed_wrong])
    print(str(guessed_wrong) + "/6 wrong")
    print(*guessed_word)
    print("So far you have guessed %s"% guessed_letters)
    print("What would you like to guess")
    guess = input().lower()
    if len(guess) == len(word):
        if guess == word:
            print("You have guessed the word, congratulations!")
        else:
            guessed_wrong += 1
            print("That was not the word")
    elif len(guess) != 1 & len(guess) != len(word):
        print("Please guess either a letter or a word(of the same length as the word), try again.")
    elif guess.isalpha() == False:
        print("Please guess a letter or word")
    elif guess in guessed_letters:
        print("You have already guessed that, please try again.")
    else:
        guessed_letters.append(guess)
        if guess not in word:
            guessed_wrong += 1
        else:
            for i in word_range:
                if guess == word[i]:
                    guessed_word[i] = guess
    gameCheck()
