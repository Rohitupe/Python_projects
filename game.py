
import random
win = random.randrange(1,100)
print(win)
user = int(input("Enter your number\t"))
guess = 1
game_over= False
while not game_over:
    if win == user:
        print(f"you get it right in {guess}")
        game_over=True
    
    else:
        if win < user:
            print("too high\t")
            guess = guess + 1
            user = int(input("Enter your number"))
        
        else:
            print("too low\t")
            guess = guess+1
            user = int(input("Enter your number\t"))


