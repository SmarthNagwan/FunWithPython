choice = int(input('WHAT YOU WANT TO ACCSESS?\n1 = quiz\n2 = number guesser\n3 = rock/paper/scissors\n4 = Print table of any given number\n5 = Total finder for a retail shop\n6 = Adventure Game\n7 = Calculator\n '))

if choice == 1:
    print("WELCOME TO MY MATH QUIZ")
    playing = input("DO YOU WANT TO PLAY? : ")
    if playing.lower() != 'yes':
        quit()

    print("Okay Let's play :) ")
    score = 0
    q1 = input("what is the value of sin(30)? [HINT: Answer the simplified version]: ")
    if q1 == '0.5' or q1 == '1/2':
        print("CORRECT +1")
        score += 1
    else:
        print("Incorrect 0")

    q2 = input('what is the value of sin(x)/cos(x)? ')
    if q2 == 'tan(x)':
        print("CORRECT +1")
        score += 1
    else:
        print("Incorrect 0")

    q3 = input('what is the formula for the perimeter of a rectangle; where length = x, breadth = y? ')
    if q3 == '2(x+y)':
        print("CORRECT +1")
        score += 1
    else:
        print("Incorrect 0")

    q4 = input('sum of two odd numbers will always be? ')
    if q4 == 'even':
        print("CORRECT +1")
        score += 1
    else:
        print("Incorrect 0")

    q5 = input('what is the probability of getting a 3 if a dice is rolled once? ')
    if q5 == '1/6':
        print("CORRECT +1")
        score += 1
    else:
        print("Incorrect 0")

    print("You got", score, "questions correct")
    if score <= 2:
        print('YOU NEED TO IMPROVE')
    elif score <= 4:
        print('GREAT')
    else:
        print('EXCELLENT!')

    print('YOUR PERCENTAGE :', (score / 5) * 100)

elif choice == 2:
    import random
    top_of_range = int(input("Enter the maximum number: "))

    if top_of_range <= 0:
        print('Please enter a number greater than 0 next time.')
        quit()
    else:
        print('Guess a number between 0 and', top_of_range)

    random_number = random.randint(0, top_of_range)
    score = 0

    while True:
        score += 1
        user_guess = int(input('Make a guess: '))
        if user_guess == random_number:
            print('Congratulations! You guessed the correct number.')
            break
        elif random_number > user_guess:
            print('Guess higher.')
        else:
            print('Guess lower.')

    print('You guessed it right in', score, 'attempts.')

elif choice == 3:
    import random
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break
        if user_input not in options:
            continue
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print('Computer picked', computer_pick)
        if (user_input == "rock" and computer_pick == 'scissors') or (user_input == "paper" and computer_pick == 'rock') or (
                user_input == "scissors" and computer_pick == 'paper'):
            print('You Won !!!')
            user_wins += 1

        else:
            print('Computer won!!!')
            computer_wins += 1

    print('You won', user_wins, 'times.')
    print('Computer won', computer_wins, 'times.')
    print('GoodBye!')

elif choice == 4:
    a = int(input('ENTER THE NUMBER YOU WANT TABLE OF:'))
    n = a 
    while n <= a * 10:
        print(n)
        n += a
    

elif choice == 5:
    total = 0
    while True:
        item = input("Enter the product name or press ok to end\n").lower()
        if item == 'ok':
            break
        quantity = float(input("Enter the quantity\n"))
        
        if item == 'dal':
            total += 60 * quantity
        elif item == 'chawal':
            total += 85 * quantity
        elif item == 'rajma':
            total += 50 * quantity
        elif item == 'chole':
            total += 35 * quantity
        elif item == 'chocolate':
            total += 30 * quantity
        elif item == 'ice cream':
            total += 100 * quantity

    print('TOTAL : ', total)        

elif choice == 6:
    import time
    
    def intro():
        print("Welcome to the Adventure Game!")
        time.sleep(1)
        print("You find yourself in a mysterious forest...")
        time.sleep(1)
        print("Your goal is to find the treasure hidden somewhere in the forest.")
        time.sleep(1)

    def choose_path():
        print("\nWhich path will you choose?")
        print("1. Left")
        print("2. Right")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    def left_path():
        print("\nYou chose the left path...")
        time.sleep(1)
        print("You encounter a wild bear!")
        time.sleep(1)
        print("What will you do?")
        print("1. Fight")
        print("2. Run")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            print("\nYou chose to fight...")
            time.sleep(1)
            print("The bear is too strong! You were defeated...")
        elif choice == '2':
            print("\nYou chose to run...")
            time.sleep(1)
            print("You managed to escape from the bear!")

    def right_path():
        print("\nYou chose the right path...")
        time.sleep(1)
        print("You find a hidden cave!")
        time.sleep(1)
        print("Inside the cave, you find a treasure chest!")
        time.sleep(1)
        print("Congratulations! You found the treasure!")

    def play_game():
        intro()
        time.sleep(1)
        path = choose_path()
        if path == '1':
            left_path()
        elif path == '2':
            right_path()
        else:
            print("Invalid choice. Please try again.")

    play_game()
    

elif choice == 7:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            print("Invalid")
        
        else:
            return x/y
    
    print("What task you want to do\n1 addition\n2 subtraction\n3 multiplication\n4 division\n")
    while True:
        choice = int(input("Enter your choice :\n"))
        if choice in [1,2,3,4]:
            num1 = float(input("First number:\n"))
            num2 = float(input("Second number:\n"))
            if(choice==1):
                print('Answer:',add(num1,num2))
            elif(choice==2):
                print('Answer:',subtract(num1,num2))
            elif(choice==3):
                print('Answer:',multiply(num1,num2))
            elif(choice==4):
                print('Answer:',divide(num1,num2))
                

        else:
            print('Invalid')

        another_calculation = input("Do you want to perform another calculation (yes/no)\n").lower()
        if(another_calculation != 'yes'):
            break
    print("THANKS:) ")