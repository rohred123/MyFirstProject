#Problem 1:
input_string = input('Enter a number for odd/even number test: ');
#print (input_string);

input_string = str(input_string)
if(input_string.isdigit()):
  #print ('input is digit')
  in_int = int(input_string);
  if(in_int%2 == 0):
    print('Input is even')
  else:
    print('Input is odd')
else:
  print ('Input is not digit. Try again')

#Problem 2:
input_string = input('Enter a number for divisibility by 5 test: ');
#print (input_string);

input_string = str(input_string)
if(input_string.isdigit()):
  #print ('input is digit')
  in_int = int(input_string);
  if(in_int%5 == 0):
    print('Input is divisble by 5')
  else:
    print('Input is not divisible by 5')
else:
  print ('Input is not digit. Try again')

#Problem 3
print("This is a program where you will be entering a digit and this will give you that digit's factorial.")
n=input("Enter the digit: ")
n=str(n)
if(n.isdigit()):
  factorial=1
  i=int(n)
  for i in range(i,1, -1):
    factorial=factorial*i
  print(f"The factorial of {n} is " + str(factorial))
else:
  print("Input is not a digit. Try again.")

#Problem 4

fan_in_status = input('Enter the initial status of fan (Off/On) : ');


fan_in_status = str(fan_in_status)
fan_in_status = fan_in_status.casefold();

if(fan_in_status not in ('on', 'off')):
  print ('Invalid initial status');
  

i=int(1);
while(i):
  fan_enter_status = input('Enter fan status to set as On/Off/Quit : ');
  fan_enter_status = str(fan_enter_status)
  fan_enter_status = fan_enter_status.lower()
  if(fan_enter_status.casefold() not in ('on', 'off', 'quit')):
    print ('Invalid status');
  else:
    if(fan_enter_status == 'quit'):
      print('Quitting program!')
      break
    if(fan_in_status == 'on' and (fan_in_status == fan_enter_status)):
      print('Fan already on!');
    elif(fan_in_status == 'on' and fan_enter_status == 'off'):
      fan_in_status = 'off'
      print('Fan turned off!')
    elif(fan_in_status == 'off' and (fan_in_status == fan_enter_status)):
      print('Fan already off!')
    elif(fan_in_status == 'off' and (fan_enter_status == 'on')):
      fan_in_status = 'on'
      print('Fan turned on!')
      































