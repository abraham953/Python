weight = input("Weight : ")
weight = int(weight)
WeightClass= input("(L)bs or K(g): ")
if WeightClass.upper() == 'L':
    weightkg =  weight /2.20462
    print("You are {} KG ".format(weightkg))
elif WeightClass.upper() == 'K':
    weightpound = weight * 2.20462
    print("You are {} LBS ".format(weightpound))
