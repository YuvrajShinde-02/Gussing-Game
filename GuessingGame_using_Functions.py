play_again = True
wallet = 0

def chances():
    global wallet
    print("Congratulations".center(40, '-'))

    if chance == 1:
        print("You have won Rs.100 reward !")
        wallet = wallet + 100
    elif chance == 2:
        print("You have won Rs.50 reward !")
        wallet = wallet + 50
    else:
        print("You have won Rs.25 reward !")
        wallet = wallet + 25


def hint():
    print("Sorry Try Again !")
    if c_guess > u_guess:
        print("Think of a bigger number !")
    else:
        print("Think of a smaller number !")

def withdrawl():
    global wallet
    w_amount = int(input("How much amount do you want to withdraw : "))
    if w_amount <= wallet:
        wallet -= w_amount
        print(f"Amount of Rs.{w_amount} has been transferred to your account !")

    else:
        print("Insufficient wallet balance !")



while play_again:

    if wallet >= 10:
        wallet -= 10
        import random
        c_guess = random.randint(1, 11)

        for chance in range(1, 4):
            print("chance : ", chance, "/ 3")
            u_guess = int(input("Enter the guess : "))

            if c_guess == u_guess:
                chances()
                break
            else:
                hint()

        print("Your balance is Rs.{}".format(wallet))

        print("-" * 40)
        choice = input("Do you want to play again [Yes/No] ?")
        if choice != 'y':
            play_again = False

            withdraw = input("Do you want to withdraw your amount [Yes/No] ?")
            if withdraw == 'y':
                withdrawl()

    else:
        print("Insufficient amount !")
        amt = int(input("Enter min amount of Rs.10 : "))
        wallet += amt