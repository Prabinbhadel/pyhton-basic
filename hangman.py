import random
words=["apple","banana","earphone","gravitational"]
def showword(game_word,guessletter):
    display=""
    for letter in game_word:
        if letter in guessletter:
            display += letter
        else:
            display += "_"
    return display
def playgame():
    gameword=random.choice(words)
    chance=6
    guessletter=[]
    print(showword(gameword,guessletter))
    while chance>0:
        letter=input("enter a single letter")
        if letter in gameword:
            print("you guessed right")
            print(f"you have {chance} chance left")
            guessletter.append(letter)
        else:
            chance -= 1
            print(f"wrong! you have {chance} chance left")
            guessletter.append(letter)
        print(showword(gameword,guessletter))
        if(set(gameword)<= set(guessletter)):
            print(f"you successfully guesssed word {gameword}")
            break
        if chance==0:
            print("you lose")
            break
playgame()