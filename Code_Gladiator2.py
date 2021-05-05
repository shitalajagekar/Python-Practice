#  Game

T=int(input("Enter the number of test cases: "))
while (T!=0):
    no_list= list(map(int,input().strip().split(" ")))
    l= no_list[0]
    r=no_list[1]
    prime_no=list()
    for i in range(l,r+1):
        flag = True
        for j in range(2,i):
            if (i % j == 0):
                flag = False
                break

        if flag == True :
            prime_no.append(i)

    length = len(prime_no)
    if length == 0:
        print("-1")
    elif length == 1:
        print("0")
    elif length >= 2:
        difference = prime_no[length-1] - prime_no[0]
        print(difference)

    T -=1



