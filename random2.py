import random
adad=random.randint(0,5)
print(f"taghalob :{adad}")
for i in range(4):
    num=int(input("enter your guess : "))
    if num==adad:
        print("win")
        break
    else:
        print("fail")
        if i==3:
            print(f"num {adad}")