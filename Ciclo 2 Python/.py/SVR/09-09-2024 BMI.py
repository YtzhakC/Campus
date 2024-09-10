weight = float(input('Enter your weight in pounds: \n'))
height = float(input('Enter our height in inches: \n'))

kilograms = 0.45359237
meters = 0.0254

w_to_k = weight*kilograms
h_to_m = height*meters

BMI = (w_to_k/(h_to_m**2))

print(f'BMI is {BMI:.2f}')