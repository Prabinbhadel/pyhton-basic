#rock paper scissors against computer
import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=="r":
            return False
        if you=='s':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
print("comp turn:rock(r) paper(p) or scissors(s)")
ranno=random.randint(1,3)
if ranno==1:
    comp='r'
elif ranno==2:
    comp='p'
elif ranno==3:
    comp='s'

you=input("your turn:rock(r) paper(p) or scissor(s)")
b=game(comp,you)
print(f"you choose {you}")
print(f"computer choose {comp}")

if b==None:
    print("its a tie")
elif b==True:
    print("you win")
elif b==False:
    print("you lose")
