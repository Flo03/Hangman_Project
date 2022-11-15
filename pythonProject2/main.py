import random
from list_of_words import word_list
from arts import stages, logo


chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.\n')

print(logo)
display = []
for letter in chosen_word:
    display += "_"

end = False
lives = 6


while not end:
    guess = input("Enter a letter: ")

    if guess in display:
        print(f"You already guess this letter: {guess}. ")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if "_" not in display:
        end = True
        print("You won the game")
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You loose a life :) \n")
        lives -= 1
        if lives == 0:
            end = True
            print("You lost the game. To bad you couldn't find it :(")
            print("\n")
            print(f"The word was {chosen_word}. \n Better luck next time")
    print(stages[lives])





















