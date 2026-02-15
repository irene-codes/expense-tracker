def addexpense():
    o = input("Enter your expense ")
    a = input("Enter the date(DD/MM/YR)")
    e = input("Enter category(Food,Travel,others)")
    f = open('expense file', 'a')
    f.write(o + " " + a + " " + e + "\n")
    f.close()
def viewexpense():
    f = open('expense file', 'r')
    for i in f:
        print(i)
def totalexpense():
    f = open('expense file', 'r')
    sum=0
    for i in f:
        x=i.split()
        print(x[0])
        sum+=int(x[0])
    f.close()
    print("your total expense is",sum)
while True:
    choice=input("enter your choice (add expense,view expense,total expense)").lower()
    if choice=="add expense":
        addexpense()
    elif choice=="view expense":
        viewexpense()
    elif choice=="total expense":
        totalexpense()
    k=input("do u want to continue(yes/no)").lower()
    if k!="yes":
        print("Thank you for using it")
        break
    else:
        continue
