# program to convert temperatures to and from celsius, fahrenheit
T = input("Inter temperature to convert F or C : ")
degree = int(T[:-1])
X = T[-1]

if X.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  Y = "Fahrenheit"
elif X.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  Y = "Celsius"
else:
  print("Not Valid")
  quit()
print("Temperature in", Y, "is", result, "degrees.")