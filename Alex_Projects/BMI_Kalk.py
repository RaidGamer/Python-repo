import math
print("="*64)
print("Välkommen till min BMI kalkylator.")
print(" ")
print("För att ta reda på ditt BMI värde svara på de följande frågorna.\nSvara så exakt som du kan, typ en decimal.")
print(" ")
weight = input("1) Hur mycket väger du i kg?: ")
height = input("2) Hur lång är du i m?: ")
weightReal = float(weight)
heightmeter = float(height)

heightmeter_squared = heightmeter**2 #förbereder inför formeln, tar höjden i meter i kvadrat

bmi = weightReal/heightmeter_squared #bmi formel tyngd/höjd_kvadrat
bmiround = round(bmi, 1) #avrundar resultatet till en decimal
bmi_text = str(bmiround)
print(" ")
if 18.5<=bmi<=25: 
    print("Grattis du är hälsosam")
else: print("Du borde gympa")
print("Ditt BMI är " + bmi_text + ".")
print("="*64)
