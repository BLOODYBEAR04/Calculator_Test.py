temp = input("Input the temperature you want to convert(put C for Celsius and F for Fahrenheit after the desired number): ")
degree = int(temp[:-1])
conv = temp[-1]

if conv.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  far = "Fahrenheit"
  print("The temperature in", far, "is", result,"F°")
elif conv.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  cel = "Celsius"
  print("The temperature in", cel, "is", result,"C°")
else:
  print("Use proper convention(C for celsius and F for fahrenheit after the desired number).")