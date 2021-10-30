import random
import sys
#the amount of times the generate function ran and the number that constantly changes
timesran = 0
number = 0
#the number you're aiming to hit.
print('KEEP IN MIND, THE NUMBERS THE COMPUTER GUESSES ARE COMPLETELY RANDOM!')
aimednumber = int(input('what number do you wish to use? '))
#rangearray is the rangearray of the numbers it can guess.
maxrange = int(input('what is the maximum number the computer can guess? '))
rangearray = [1, maxrange]
#the main function
def generate():
    #stupidly long for loop so you dont get recursion error
    for i in range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        #sets up variables
        global aimednumber
        global rangearray
        global timesran
        global number
    #sets up number
        number = random.randint(rangearray[0], rangearray[1])
    #the whole point of the thing
        if number == aimednumber:
            print('the computer guessed: ' + str(number))
    #the amount of times the function ran(wording is a bit weird)
            print('the computer got the number you aimed it to guess in ' + str(timesran) + ' times')
            print('the number was: ' + str(number))
            sys.exit()
        else:
            print('the number the computer guessed is: ' + str(number))
            timesran += 1
generate()
