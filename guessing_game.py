from random import shuffle
#This function will shuffle all the numbers in the list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
#list
mylist=['','0','']
shuffle_list(mylist)
#This function will define the player guess
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number 1,2,0")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='0':
        print("Correct!")
    else:
        print("Sorry try again")
        print(mylist)

#Intial list
mylist=['','0','']
#shuffle list
mixedup_list=shuffle_list(mylist)
#user guess
guess=player_guess()
#check guess
check_guess(mixedup_list,guess)
