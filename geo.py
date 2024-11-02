#See if the the child has a medical problem
medical=input('Do you have a medical problem Y or N')
attendence=int(input('How many days have u attended school'))
if medical == "Y":
    print("You can take a leave")
else:
    if attendence>= 65:
        print("You can take a leave")
    else:
        print("You can not take a leave")