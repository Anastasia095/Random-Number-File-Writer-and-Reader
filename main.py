""" 

      Problem #7 Random Number File Writer and #8 Random Number File Reader                

     Program Description: This program will write a series of numbers to a file and read the random numbers from the file, then it will display numbers, total of numbers and number of random numbers read from the file.

"""


#*** Modules\Libraries

import os                   #*** system() - OS commands
import random
import array

os.system("cls")            #*** clear screen

    #*** Begin execution of the program
    #*** Function definitions
def greeting():
    print("This program will write a series of numbers to a file and read the random numbers from the file, then it will display numbers, total of numbers and number of random numbers read from the file.")
    print()
def Generate_Number(fileobj,quantity):
    for i in range(quantity):
      randNum = random.randint(1, 500)
      fileobj.write(str(randNum)+"\n")
    return randNum
def Read_Number(fileobj):
    numbers = fileobj.read().splitlines()
    units = len(numbers)
 
    print("The number of random numbers read from the file", units)
    print()
    
    sum = 0
    i = 0
    for i in range (units):
        print("#", i+1, " ", numbers[i])
        sum+=int(numbers[i])
        i+=1
    print()
    print("The sum of the numbers:",sum)

def main():
    greeting()
    file = open("randomNumber.txt","w") 
    while True:
        try:
            file = open("randomNumber.txt","r+")
            print("Successfully opened file")
            print()
            break
        except:
            input("Error opening file. Press Enter to exit the program and try again. . .")
            quit()          
    quantity = int(input("How many random numbers would you like to be generated and stored? "))
    while quantity < 1:
          print("ERROR number of generated numbes can't be less than 0: ")
          quantity= int(input("Enter your selection: "))
    print("\n")          
    Generate_Number(file, quantity)
    file.close()
    file = open("randomNumber.txt","r")
    Read_Number(file)
    while True:
        try:
            file = open("randomNumber.txt","r+")
            print("Successfully opened file")
            print()
            break
        except:
            input("Error opening file. Press Enter to exit the program and try again. . .")
            quit()
    file.close()

if __name__ == "__main__":
    main()