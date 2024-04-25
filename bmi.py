def calculate_bmi(height, weight):
    print("height="+str(height))
    print("weight="+str(weight))
    bmi = weight / (height**2)
    print("BMI"+str(bmi))
    if bmi<18.5:
        print("You are underweight")
    if 18.5<=bmi<=25.0:
        print("You are normal weight")
    if bmi>25.0:
        print("you are overweight")
calculate_bmi(weight=57,height=1.73)



