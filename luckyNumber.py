def luckyNumber(name):
    number = len(name)*9
    print("Hello ", name,". Your lucky number is: ",str(number))


name = input("Please insert your name: ")
luckyNumber(name)
input("Thanks for using this program, Press anyting for exit...")
