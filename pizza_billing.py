
pizza=(input("What size of pizza do you want: "))

if(pizza== "small"):
    bill=100
    print(f"for small pizza the bill is{bill}")
elif(pizza== "medium"):
        bill=200
        print(f"for medium pizza the bill is{bill}")
elif(pizza== "large"):
        bill=300
        print(f"for large pizza the bill is{bill}")
peperoni=input("Do you want paperoni(Y/N)")
if(peperoni=='y'or peperoni=='Y'):
        if(pizza=="small"):
            bill=bill+30
            print(f"your bill for peperoni small pizza is{bill}")
        elif(pizza=="medium" or pizza=="large"):
            bill=bill+50
            print(f"your bill for peperoni pizza is{bill}")
        else:
            print("peperoni not required")
extra_cheese=input("Do you want extra chesse(Y/N)")
if(extra_cheese=='y' or extra_cheese=='Y'):
    bill=bill+20
    print(f"your total bill is{bill}")

else:
    print("wrong input")
