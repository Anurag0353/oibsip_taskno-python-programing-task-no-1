def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi
def interpret_bmi (bmi):
    if bmi<18.5:
        return "underweight"
    elif 18.5<=bmi<25.0:
        return "Great! You are Healthy"
    elif 25.0<=bmi<30.0:
        return "Overweight"
    else:
        return "Obese"
def main():
    weight=float(input("Enter the weight in kg:"))
    height=float(input("Enter the height in cm"))
    bmi=calculate_bmi(weight,height)
    interpretation =interpret_bmi(bmi)
    print(f"your BMI is:{bmi:.2f}")
    print(f"you are classified as:{interpretation}") 
if __name__ == "__main__":
    main()
      
