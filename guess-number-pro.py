import random

class Guess_number:
    def __init__(self,user_input=int()):
        self.user_input = user_input
    def __guess(self):
        return random.randint(0,50)
    def match(self):
        guessed_number = self.__guess()
        print(f"The answer{guessed_number}")
        for attempts in range(1,7):
            if attempts!=6:
                self.user_input = int(input("Enter the positive number : "))
                if self.user_input == guessed_number:
                    print("=================================================")
                    print("\nCongratulation! Number Matched and You've won \n")
                    print("=================================================")
                    start_game()
                else:
                    print("Wrong Number!\n\n")
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxx\nYou over your total attempts\nxxxxxxxxxxxxxxxxxxxxx")
                start_game()       



def start_game():
    answer = """
are you interested to play the Guess Game :
press 1 to start 
and press 0 to exit \n
"""
    print(answer)
    key_ans = int(input("Enter your answer : "))
    if key_ans==1:
        game = Guess_number()
        game.match()
    else:
        print("Okey! Exit command successfull")
start_game()

