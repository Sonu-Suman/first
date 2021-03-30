# This is the first type of hangman game code
"""
import random

with open('C:/Users/suman/Microsoft VS Code/vscode/first/word.txt', 'r+') as f:
    f.readline()
    words = list(f)

word = random.choice(words).strip()

print(word)

if __name__ == "__main__":
    print("Welcome in Hangman game")
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    outguessed = []
    letter = input("enter your letter: ")
    count = 1 * len(word)
    while count != 0:
        if letter.upper() in outguessed:
            letter = " "
            print("This is letter is already guessed!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = "_"
        else:
            print(' '.join(guessed))
            if letter != " ":
                outguessed.append(letter.upper())
            letter = input("Enter your letter: ")

        if "_" not in guessed:
            print("You Won!")
            print("Your guess word is: ", ''.join(guessed))
            break
"""

# This is second type of hangman game code

import random

def choose_random_word():
    words=[]
    with open('C:/Users/suman/Microsoft VS Code/vscode/first/word.txt', 'r') as file:
        line = file.readline()
        while line:
            words.append(line.replace("\n","".strip()))
            line = file.readline()
    choice=words[random.randint(0,len(words)-1)]
    return choice


print("Welcome to Hangman!")
secret_word=choose_random_word()
dashes=list(secret_word)
display_list=[]
for i in dashes:
    display_list.append("_")
count=len(secret_word)
guesses=0
letter = 0
used_list=[]
while count != 0 and letter != "exit":
    print(" ".join(display_list))
    letter=input("Guess your letter: ")

    if letter.upper() in used_list:
        print("Oops! Already guessed that letter.")
    else:
        for i in range(0,len(secret_word)):
            if letter.upper() == secret_word[i]:
                display_list[i]=letter.upper()
                count -= 1
        guesses +=1
    used_list.append(letter.upper())

if letter == "exit":
    print("Thanks!")
else:
    print(" ".join(display_list))
    print("Good job! You figured that the word is "+secret_word+" after guessing %s letters!" % guesses)
