def calculate_bmi(height, weight):
    print("height="+str(height))
    print("weight="+str(weight))
    bmi = weight / (height**2)
    print("BMI"+str(bmi))
    if bmi<18.5:
        underweight=-1
        print("You are underweight")
        return -1
    if 18.5<=bmi<=25.0:
        normal_weight=0
        print("You are normal weight")
        return 0
    if bmi>25.0:
        overweight = 1
        print("you are overweight")
        return 1
calculate_bmi(weight=57,height=1.73)



