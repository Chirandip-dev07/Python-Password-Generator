import random
cap_let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
low_let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_set = ['0','1','2','3','4','5','6','7','8','9']
special_set = ['_','@','/','.','#','$','&','*']
passwd = " "

print("WELCOME TO PASSWORD GENERATOR")
ch = input("DO YOU WANT TO GENERATE A PASSWORD? (Y/N) : ")

while ch=="Y":
    for i in range(random.randint(2,5)):
        passwd = passwd + random.choice(cap_let)
    for j in range(random.randint(2,5)):
        passwd = passwd + random.choice(low_let)  
    for k in range(random.randint(2,3)):
        passwd = passwd + random.choice(num_set)
    for l in range(random.randint(1,3)):
        passwd = passwd + random.choice(special_set)
    print("YOUR GENERATED PASSWORD IS :", passwd)
    passwd = " "
    ch = input("DO YOU WANT TO GENERATE ANOTHER PASSWORD? (Y/N) : ")

print(" ")

print("THANKS FOR USING PASSWORD GENERATOR")