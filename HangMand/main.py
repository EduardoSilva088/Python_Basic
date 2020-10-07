import random
import time

print("\nWelcome to Hangman game!")
name = input("Enter your name: ")
print("Hello", name + ". Good Luck!")

print("The game is about to start!\nLet's play Hangman!")

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global word_static
    words_to_guess = ("janeiro","fronteira","imagem","promessa","criancas","rima","professor","codigo")
    word = random.choice(words_to_guess)
    word_static = word
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do you want to play again? Y = Yes / N = No\n")
    while play_game.upper() not in ("Y","N"):
        play_game = input("Do you want to play again? Y = Yes / N = No ")
    if play_game.upper() == "Y":
        hangman()
    elif play_game.upper() == "N":
        print("Thanks for playing!")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5
    print("This is the Hangman Word: ",end="")
    for i in range(len(word)):
            print(display[i].upper()+" ",end="")
    guess = input( "| Enter your guess: ")
    guess = guess.strip()
    if (len(guess.strip()) == 0 or len(guess.strip()) >= 2) or guess <= "9":
        print("Invalid input, try again.")
        hangman()
    elif guess.lower() in word:
        already_guessed.extend([guess])
        for i in range(len(word)):
            if word[i] == guess.lower():
                word = word[:i] + "_" + word[i+1:]
                display = display[:i] + guess + display[i+1 :]
    elif guess in already_guessed:
        print("\nTry another letter.\n")

    else:
        count+=1

        if count == 1:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__    \n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 2:
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    / \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__    \n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 3:
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__     \n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 4:
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \ \n"
                  "  |       \n"
                  "__|__     \n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining.\n")
        elif count == 5:
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |       \n"
                  "__|__     \n")
            print("Wrong guess. You died!!\n")
            print("The word was: ",word_static.upper())
            play_loop()
    if word == "_" * length:
        print("Congrats! You have guessed the word correctly!")
        print("The word was: ",word_static.upper())
        play_loop()
    elif count != limit:
        hangman()

main()

hangman()
        


