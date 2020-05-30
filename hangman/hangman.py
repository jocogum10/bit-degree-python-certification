import random

def hangman():
    word = random.choice(['dog', 'cat', 'elephant', 'horse', 'tiger'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print('Enter a valid letter: ')
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left. ")
                print("  --------  ")
            elif turns == 8:
                print("8 turns left. ")
                print("  --------  ")
                print("      0     ")
            elif turns == 7:
                print("7 turns left. ")
                print("  --------  ")
                print("      0     ")
                print("      |     ")
            elif turns == 6:
                print("6 turns left. ")
                print("  --------  ")
                print("      0     ")
                print("      |     ")
                print("       \\    ")
            elif turns == 5:
                print("5 turns left. ")
                print("  --------  ")
                print("      0     ")
                print("      |     ")
                print("     / \\    ")
            elif turns == 4:
                print("4 turns left. ")
                print("  --------  ")
                print("     \\0     ")
                print("      |     ")
                print("     / \\    ")
            elif turns == 3:
                print("3 turns left. ")
                print("  --------  ")
                print("     \\0/    ")
                print("      |     ")
                print("     / \    ")
            elif turns == 2:
                print("2 turns left. ")
                print("  --------  ")
                print("     \\0/ |  ")
                print("      |     ")
                print("     / \\    ")
            elif turns == 1:
                print("1 turn left. ")
                print("  --------  ")
                print("     \\0/_|  ")
                print("      |     ")
                print("     / \\    ")
            else:
                print("Game over. ")
                print("  --------  ")
                print("      0__|  ")
                print("     /|\\    ")
                print("     / \\    ")
                break

name = input("Enter your name: ")
print("Welcome " + name +  "!")
print("---------------------")

print("Try to guess the word in less than 10 tries.")

hangman()