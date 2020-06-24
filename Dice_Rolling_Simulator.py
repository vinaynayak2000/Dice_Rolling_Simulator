import random
import time

u='y'
while(u=="y" or u=="yes"):
    print("Dice is rolling...")
    time.sleep(1)
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    print("Your Dice_1 value is",dice_1)
    print("Your Dice_2 value is",dice_2)
    time.sleep(1)
    if(dice_1==dice_2):
        print("Congo Same values appeared :-)")


    u=input("Do you want to roll the dice again(y/n)? ").lower()
print("Thanks for playing")    