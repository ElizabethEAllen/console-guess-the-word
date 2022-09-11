# name = "alex"
# names = ["elizabeth", "ivan", "alex"]
# print(names)
# print("alex" not in names)
# names.append("misha")
# print(names)
import random
with open("words_en.txt") as file:
    data = file.read()
    words = data.split()
print("welcome to our game, guess the word.")
secret_word = random.choice(words)
name = input("what is your name? ")
lives = int(input("how many lives do you want? "))
user_letters = []
while lives > 0 :
    win = True
    letter = input(name + ", what letter do you think is in the secret word? ")
    if len(letter) > 1 :
        print("you can only write one letter at a time")
        continue
    if letter in user_letters :
        print("you've already guessed that letter")
        continue
    user_letters.append(letter)
    print(user_letters)
    for char in secret_word :
        if char in user_letters :
            print(char, end="  ")
        if char not in user_letters :
            print("*", end="  ")
            win = False
    print()
    if letter not in secret_word :
        lives -=1
        print("your letter was wrong. " + name + ", you have " + str(lives) + " lives left.")
        if lives == 0 :
            print(name + ", game over, the secret word was " + secret_word)
    if win == True :
        print(name + ", you win!")
        break
'''
Сделать программу "магического шара": составить список со строками "да", "нет", 
"не могу сейчас сказать". Приветствовать пользователя и вывести ему сообщение - 
"Задавай волнующий тебя вопрос, на который можно ответить "да" или "нет"". 
На вопросы, вводимые пользователем, надо случайным образом давать ответ.
'''