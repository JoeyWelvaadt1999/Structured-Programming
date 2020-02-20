import math
import random
import binascii

#Opdracht 1 - Pyramide

def pyramidFor():
    height = int(input("Pyramid height: "))
    for i in range(height):
        pyramid = '*' * (i + 1)
        print(pyramid)
    
    for i in range(height - 1):
        pyramid = '*' * (height - 1 - i)
        print(pyramid)

def pyramidWhile():
    height = int(input("Pyramid height:"))
    index = 0
    
    while index < height:
        pyramid = '*'*(index+1)
        print(pyramid)
        index+=1

    index = height -1
    while index > 0:
        pyramid = '*'*(index+1-1)
        print(pyramid)
        index-=1

def pyramid():
    pyramidFor()
    pyramidWhile()

#Opdracht 2 - Tekstcheck

def textCheck():
    text1 = str(input("Input first sentence: "))
    text2 = str(input("Input second sentence: "))

    index = 0

    for c in text1:
        print(text2[index])
        print(c)
        if c is not text2[index]:
            print("The difference was found at index: " + str(index))
            break
        index += 1


#Opdracht 3 - Lijstcheck

def count(index, list):
    count = 0
    for i in range(len(list)):
        if list[i] == index and float(index).is_integer():
            count += 1
    return count

def difference(list):
    list.sort()
    
    return abs(list[0] - list[-1])

def listCheck():
    listIndexes = str(input("Input ones and zeros divided by commas and no spaces: "))
    list = listIndexes.split(',')

    ones = count(1, list)
    zeros = count(0, list)

    if ones > zeros and zeros <= 12:
        return True
    return False
    
#Opdracht 4 - Palindroom
def rotateWord():
    word = str(input("Input word: "))
    print(''.join(reversed(word)))
    return word[::-1]
    

#Opdracht 5 - Sorteren
def sortNumbers():
    listIndexes = str(input("Input numbers divided by commas and no spaces: ")).split(',')
    listIndexes.sort()
    return listIndexes

#Opdracht 6 - Gemiddelde berekenen

def average():
    listIndexes = str(input("Input numbers divided by commas and no spaces: ")).split(',')
    total = 0
    for i in range(len(listIndexes)):
        total += int(listIndexes[i])
    
    print("Average: " + str(total / len(listIndexes)))

    def listInList(listOfLists):
        total = 0
        divider = 0
        for i in range(len(listOfLists)):
            for j in range(len(listOfLists[i])):
                total += listOfLists[i][j]
                divider += 1
        return total / divider
    
    print("Average of list in lists: " + str(listInList([[2,3,5,1,2,6,5], [9,5,3,1], [9,3,1,4]])))

#Opdracht 7 - Random

def guessTheNumber():
    rand = random.randrange(0, 10)
    guess = -1

    while True:
        guess = int(input("Input guess: "))
        if guess == rand:
            print("You guessed it!")
            break
        else:
            print("Your guess was wrong try again!")

#Opdracht 8 - Compressie

def compression():
    
    lines = ""
    with open("text.txt", "rt") as readfile:
        for line in readfile:
            lines += line.lstrip()
        readfile.close()

    with open("text.txt", "wt") as writefile:
        writefile.write(lines)
        writefile.close()

#Opdracht 9 - Cyclisch verschuiven

def cycle():
    char = str(input("Input charactar: "))
    number = int(input("Input n: "))
    binary = list(''.join(format(ord(x), 'b') for x in char))
    print(binary)

    def shiftRight(binary,number):
        return binary[-number:] + binary[:-number]

    def shiftLeft(binary, number):
        return binary[number:] + binary[:number]

    if number > 0:
        binary = shiftLeft(binary,number)
    elif number < 0:
        binary = shiftRight(binary, number)
    
    return binary
    
#Opdracht 10 - Fibonaci

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))

def fibonaci():
    n = int(input("Input number: "))
    print(recur_fibo(n))
        
#Opdracht 11 - Caesarcijfer

def caeser():
    text = str(input("Input text: "))
    rotation = int(input("Input rotation: "))
    chars = list(text)

    caeser = []

    for char in chars:
        asc = ord(char)
        if asc >= (65 + rotation) and asc <= (90 - rotation) or asc >= (97 + rotation) and asc <= (122 - rotation):
            asc += rotation
        caeser.append(chr(asc))
    
    return ''.join(caeser)

#Opdracht 12 - FizzBuzz

def fizzBuzz():
    def multipleOff(n, b):
        if n % b == 0:
            return True
        return False
    
    for i in range(100):
        if multipleOff(i+1, 3):
            print("fizz")
        elif multipleOff(i+1, 5):
            print("buzz")
        else:
            print(i+1)



running = True

def shutdown ():
    global running
    running = False

options = [pyramid, textCheck, listCheck, rotateWord, sortNumbers, average, guessTheNumber, compression, cycle, fibonaci, caeser, fizzBuzz, shutdown]

while running:
    print("Options 1-12 are the assignments and option 13 is to quit the program.")
    option = int(input("Input option assignment 1-13: "))
    print(options[option - 1]())



