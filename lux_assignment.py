# Prompts user to enter desired number.
num=int(input("Enter a number : "))

# Assigning the variables.
n1=0
n2=1
i=1

# Creates an empty list the appends the variables.
lst=[]
lst.append(n1)
lst.append(n2)

while i<num-1:
    n3=n1+n2
    n1=n2
    n2=n3
    lst.append(n3)
    i=i+1

for i in lst:
    if (num == i):
        print("Fibonacci number")
        break
else:
    print("Not fibonacci")