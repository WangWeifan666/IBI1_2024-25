# BMI=Weight(kg)/Height(m)^2
#Weight=a
#Height=b
#input a and b into BMI
#calculate and print BMI
a=int(input("Weight"))
b=float(input("Height"))
c=a/(b**2)
print(c) #BMI=c
if c>30: 
    print("obese")
if c<18.5:
    print("underweight")
if c>=18.5 and c<=30:
    print("normal weight")