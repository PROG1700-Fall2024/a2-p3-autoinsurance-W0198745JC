#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:  W0198745   
#Student Name:  Jenille Cheney

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("welcome to the Auto Insurance Calculator")
#Input Male or Female
    sex= input("Are you 'Male' or 'Female' : ").lower()  #almost forgot my .lower but caught it in the testing phase
# Input age
    age= input("Enter your age : ")
#input price of vehicle 
    vehiclePrice = float(input("Enter the purchase price of vehicle : "))
#If/Else Sex 
    if sex == "male":
        if age >= "15" and age <"25":
            monthlyFee = (0.25* vehiclePrice)/12
        elif age >= "25" and age < "40":               # originally had == and it didnt work until I made it >=
            monthlyFee = (0.17*vehiclePrice)/12
        else:
            monthlyFee = (0.10*vehiclePrice)/12
    else:
        if age >="15" and age < "25":
            monthlyFee = (0.20*vehiclePrice)/12
        elif age >="25" and age < "40":
            monthlyFee = (0.15*vehiclePrice)/12
        else:
            monthlyFee = (0.10*vehiclePrice)/12
#elifage
#calculate monthly  #ended up doing this within the elif statements
    print("Your Monthly Insurance will be $ {0:.2f}".format(monthlyFee))
#Output Monthly Cost

# I found doing the flow chart made this move very quickly with very few mistakes other than minor adjustments





    # YOUR CODE ENDS HERE

main()