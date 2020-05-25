input_string = input('Enter a number: ');
#print (input_string);

input_string = str(input_string)
if(input_string.isdigit()):
  #print ('input is digit')
  in_int = int(input_string);
  if(in_int%2 == 0):
    print('Output is '+ str(in_int+3))
  else:
    print('Output is ' + str(in_int*4))
else:
  print ('input is not digit. Try again')

print(round(5.5))  


























