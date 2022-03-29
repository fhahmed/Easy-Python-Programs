#The_Game_Of_Rock_Paper_Scissors
user1=input("Player 1, please enter your name:")
ch1= input("Rock, Paper or Scissors? ")
while ch1.lower() not in ['rock','scissors','paper']:
    print("Check the spelling please!")
    ch1= input("Rock, Paper or Scissors? ")
user2=input("Player 2, please enter your name:")
ch2= input("Rock, Paper or Scissors? ")
while ch2.lower() not in ['rock','scissors','paper']:
    print("Check the spelling please!")
    ch2= input("Rock, Paper or Scissors? ")
def choice(c1,c2):
    if c1.lower()=='rock':
        if c2.lower()=='scissors':
            return("%s wins!!" %user1)
        elif c2.lower()== 'rock':
            return("Its a tie!!")
        else:
            return("%s wins!!" %user2)
    elif c1.lower()=='paper':
        if c2.lower()=='scissors':
            return("%s wins!!" %user2)
        elif c2.lower()== 'paper':
            return("It's a tie!!")
        else:
            return("%s wins!!" %user1)
    elif c1.lower()=='scissors':
        if c2.lower()=='rock':
            return("%s wins!!" %user2)
        elif c2.lower()== 'scissors':
            return("It's a tie!!")
        else:
            return("%s wins!!" %user1)
    
print(choice(ch1,ch2))