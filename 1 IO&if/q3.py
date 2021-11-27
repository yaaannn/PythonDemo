weight, height = eval(input())
BMI = weight / (height * height)
print("Your BMI is {:.1f}".format(BMI))
if BMI < 18.5:
    print("too thin")
elif 18.5 <= BMI <= 23.9:
    print("normal")
elif 24 <= BMI <= 27.9:
    print("overweight")
else:
    print("fat")
