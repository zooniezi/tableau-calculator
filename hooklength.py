import math
while True:

    print("Type the values of λ !")
    lambdas = list(map(int, input().split()))
    temp = sorted(lambdas, reverse = True)
    if lambdas != temp:
        print("\nValues of λ are unavailable!\nPlease type the values of λ again.\n")
        continue
    for i in lambdas:
        if i <= 0:
            print("\nThere exist λ which is lower than 1.\nPlease type the values of λ again.\n")
            break
            
    else:        
        k = len(lambdas)
        l_i = []
        n = sum(lambdas)
        for i in range(len(lambdas)):
            l_i.append(lambdas[i]+k-i-1)



        value = 1

        for i in range(k):
            for j in range(i+1,k):
                value = value*(l_i[i]-l_i[j])


        denominator = 1
        for i in range(k):
            denominator = denominator * math.factorial(l_i[i])


        f_lambda = math.factorial(n)*value/denominator


        print("\nCalculation complete!\nThe number of standard tableaux is : ", int(f_lambda))
        print("\n")
