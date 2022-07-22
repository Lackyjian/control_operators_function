#Printing 1 to 10 using for loop
for i in range(11):
    print(i)
#using continue statemenet
for i in range(11):
    if(i%2==0):
        continue
    print(i)
#using break statemenet
for j in range(0,11):
    if(j==7):
        break
    print(j)
#using while loop
while(i>0):
    print(i)
    i=i-1