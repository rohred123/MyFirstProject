print("This is a kg to lb converter")
x= input("Please enter your weight in either kgs or lbs and then click enter to proceed: ")
y= input("Enter the units you used in the first question. Please put in the form kgs or lbs. Then click enter: ")
x= int(x);
if y=="kgs":
  print("Weight in pounds is  " + str(x*2.205))
elif y== 'lbs':
  print("Weight in kg is " + str(x/2.205))
else:
  print ("You can't follow directions.")






















