Winning_num=21
random=input("guess the number")
guess_number=int(random)
if Winning_num==guess_number:
    print("You won")
else:
    if Winning_num>guess_number:
        print("Guessing number is too low")
    else:
        print("Guessing number is too high")
                        
