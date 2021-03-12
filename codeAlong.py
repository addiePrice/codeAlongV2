"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""
    1. Add to list
    2. Return the value at an index position
    3. Random Choice
    4. End program  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                randomSearch()
            else:
                break
        except:
            print("An error occured! :( ")

        
def addToList():
    newItem = input("What would you like to add? Please enter an integer ")
    myList.append(int(newItem))
    print(myList)
    
def indexValues():
    indexPos = input("At what index position would you like to look?  ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

    
if __name__ == "__main__":
    mainProgram()
