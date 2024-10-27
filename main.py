import random as r
import time
import os

def memory_game_cards():
    arr = []
    score = 0
    noMistake = True

    while noMistake:
        num = r.choice(range(1, 52))
        arr.append(str(num))
        print("запомните последовательность: ")
        print(''.join(arr))
        time.sleep(5)
        os.system('cls')
        print("введите увиденную последовательность: ")
        userinput = input()
        if userinput == (''.join(arr)):
            print("отлично, продолжаем.")
            score += 1
        else:
            print("игра окончена, ваш счет: " + str(score))
            noMistake = False
    return score

def dungeon_game():
    print() 

def RPS():
    enemy = r.randint(0, 2)
    print("выбери \n1) камень \n2) ножницы\n3)бумага")
    choice = int(input())
    if ((choice == 1 and enemy == 2) or (choice == 2 and enemy == 3) or (choice == 3 and enemy == 1)):
        print("победа")
        return 1
    elif((choice == 2 and enemy == 1) or (choice == 3 and enemy == 2) or (choice == 1 and enemy == 3)):
        print("проигрыш")
        return 0
    else:
        print("ничья")
        return 0

def gallows():
    words = ['яблоко', 'банан', 'вишня', 'собака', 'динозавр', 'гойда']
    wordog = r.choice(words)
    word = list(wordog)
    guess = list("_" * len(word))
    mistakes = 0
    while mistakes < 5:
        print(guess)
        print("попыток осталось: " + str(5 - mistakes))
        print("введите одну букву, или целое слово: ")
        letter = str(input()).lower()
        if (letter == wordog):
            print("вы победили")
            break
        elif(len(letter) == 1):
            if(letter in word):
                i = word.index(letter)
                word[i] = '-'
                guess[i] = letter
                if( "".join(e for e in guess) == wordog):
                    break
            else:
                print("буквы нет в слове")
                mistakes+=1
        else:
            print("некорректный ввод")

    return 5 - mistakes

def main():
    overallScore = 0
    while True:
        print("данный проект - набор миниигр. общий счет: "+ str(overallScore) +" \nвыберите игру: \n1) игра на запоминание последовательности \n2)камень ножницы бумага. \n3)виселица.  ")
        selector =  str(input())
        match selector:
            case "1":
                overallScore += memory_game_cards()
            case "2":
                overallScore += RPS()
            case "3":
                overallScore += gallows()

main()