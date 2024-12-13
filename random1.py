import random
adad=random.randint(0,5)
print("taghalob",adad)
n = 0
for i in range(4):
    num=int(input("enter your guess : "))
    n+=1
    if num==adad:
        print("win")
        break
    else:
        print("fail")
        if n==4:
            print(f"num {adad}")