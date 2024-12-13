import random
adad=random.randint(0,5)
print(f"taghalob :{adad}")
for i in range(4):
    num=int(input("enter your guess : "))
    if num==adad:
        print("win")
        break
    elif i==3:
        print(f"fail the number is {adad}")
       