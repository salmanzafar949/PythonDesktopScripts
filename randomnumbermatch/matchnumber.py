import random

print('Enter number between 0-9:')
user_no=int(input('Enter no: '))

genrated_no = random.randrange(0,9)

if user_no == genrated_no:
     print("Congratulation you won")
     print("Automated number:" + str(genrated_no))
else:
    print("You lose")
    print("Automated number:" + str(genrated_no))