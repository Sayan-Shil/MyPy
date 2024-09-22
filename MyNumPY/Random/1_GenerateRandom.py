#import numpy as np
from numpy import random
from numpy import array

# Simple Generate Random Floats 0 to 1 
x = random.rand()
print(" Simple Generate Random Floats 0 to 1 ")
print(x)
print("\n")


# Simple Generate Random Floats 0 to 10
print("Simple Generate Random Floats 0 to 10")
x = random.uniform(0,10)
print(x)
print("\n")


#Generating Random Int 1-100
print("Generating Random int 1-100")
x = random.randint(0,10)
print(x)
print("\n")


#Generating Random Array
print("Generating Random Array")
OneD=random.randint(25, size=(5))
TwoD=random.randint(25, size=(2,5))
ThreeD=random.randint(100, size=(2,3,4))

print(OneD)
print("\n")
print(TwoD)
print("\n")
print(ThreeD)
print("\n")



#Generate Number From Array - Random.choice(Array)
spin = array(["X-Suit","Princess Dress", "Samurai Bundle", "Hair Skin", "Molotov","Grenade", "Crowbar","2x Token", "1x GoldStone", "1x Pipe", "Helmet Skin", "Emote A", "Emote B"])
print(spin)

uc = 10;
while uc>=0 :
    getspin= random.choice(spin)
    if(getspin== "X-Suit"):
        print(getspin)
        print("Congratulations !! You have got X-Suit !!")
        break
    print(getspin)
    uc -= 1













