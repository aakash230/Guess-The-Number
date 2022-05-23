import random
a= random.randint(1,100)
no_of_guesses=1
print("number of guesses is limited to only 10 times: ")
while (no_of_guesses<=10):
    guess=int(input("guess the number: \n"))
    if guess>a:
        print("you entered greater number please input smaller number.\n")
    elif guess<a:
        print("you entered smaller number please input greater number.\n")
    else:
        print("you won,you guessed the right number  \n")
        print(no_of_guesses,"number of guesses you took to finish")
        break
    print(10-no_of_guesses,"no of guesses left")
    no_of_guesses = no_of_guesses +1
if(no_of_guesses>10):
    print("game over!!","\nOriginal Number was",a)
