
'''
код и историю коммитов можно найти так же на https://github.com/novff/python-game

во мне нет сил писать сюжеты поэтому вместо новеллы я написал набор консольных миниигр.
да и методов переменных и способов использования переменных здесь тоже хватит.
'''

import random as r
import time
import os
import numpy as np


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

def topdown_dungeon_game():
    game = True
    playerX = 2
    playerY = 2
    counter = 0
    currentMap=[
            ["#","#","#","#","#","#","#","#","#","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","#","#","_","#","_","_","_","_","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","_","#","#","#","_","_","_","_","#"],
            ["#","_","#","_","_","_","_","_","_","#"],
            ["#","_","#","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","#","#","#","#","#","#","#","#","#"]
        ]
    for i in range(5):
        y = r.choice(range(1, len(currentMap) - 1))
        x = r.choice(range(1, len(currentMap[0] ) - 1))
        if currentMap[y][x]  != "#":
            currentMap[y][x] = "*"

    while game:
        
        os.system('cls')
        currentMap[playerY][playerX] = "O" #иконка игрока
        output = str(np.matrix(currentMap))
        output = output.replace("O",str(counter))
        #удалить ненужные символы из вывода
        output = output.replace("[","")
        output = output.replace("]","")
        output = output.replace(",","")
        output = output.replace("'","")
        print(" " + output)
        #input check
        currentMap[playerY][playerX] = "_" #to remove previous player position
        if(sum(line.count('*') for line in currentMap) == 0):
            return counter
        
        direction = input("куда двинетесь?(wasd): ")
        if direction == "a":
            if currentMap[playerY][playerX - 1]  != "#":
                playerX-=1
                if currentMap[playerY][playerX] == "*":

                    counter +=1
                
        if direction == "d":
            if currentMap[playerY][playerX + 1]  != "#":
                playerX+=1
                if currentMap[playerY][playerX] == "*":
                    counter +=1
                
        if direction == "w":
            if currentMap[playerY - 1][playerX]  != "#":
                playerY-=1   
                if currentMap[playerY][playerX] == "*":
                    counter +=1
                  
        if direction == "s":
            if currentMap[playerY + 1][playerX]  != "#":
                playerY+=1
                if currentMap[playerY][playerX] == "*":
                    counter +=1
                

        
        

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
                word[i] = '/'
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
    print("добро пожаловать в игру, ваша задача набрать 100 очков")
    while overallScore < 100:
        print("данный проект - набор миниигр. общий счет: "+ str(overallScore) +" \nвыберите игру: \n1) игра на запоминание последовательности \n2)камень ножницы бумага. \n3)виселица. \n4)сбор предметов. ")
        selector =  str(input())
        match selector:
            case "1":
                overallScore += memory_game_cards()
            case "2":
                overallScore += RPS()
            case "3":
                overallScore += gallows()
            case "4":
                overallScore += topdown_dungeon_game()

main()
print("поздравляю с завершением игры.")