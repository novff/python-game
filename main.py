import random as r
import threading
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
            print("игра окончена, ваш счет" + str(score))
            noMistake = False

        




def main():
    print("игра на запоминание последовательности:")
    memory_game_cards()

main()