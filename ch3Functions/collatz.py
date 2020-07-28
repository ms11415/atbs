def collatz(number):
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = 3 * number + 1
    print(number)
    return number


playAgain = 'y'
while playAgain.lower() == 'y':
    print('Please enter a positive integer')
    try:
        myInt = int(input())
        if myInt < 1:
            print('That is not a positive integer.')
        while myInt != 1 and myInt > 0:
            myInt = collatz(myInt)
    except ValueError:
        print('That is not an integer.')
    print("Would you like to try again? Enter 'y' for yes")
    playAgain = input()
print('Thank you for playing. Goodbye.')




