import random
from hangman_art import stages, logo
from hangman_words import word_list
from os import system

print(logo)
is_game_finished = False
lives = len(stages)-1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not is_game_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    system('clear')

    if guess in display:
        print(f"You've already guessed {guess}")

    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            is_game_finished = True
            print("You Lose!")

    if "_" not in display:
        is_game_finished = True
        print("You Win!")

    print(stages[lives])
