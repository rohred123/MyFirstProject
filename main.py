while True:
  in_int = int(input('Enter a number: '))
  if in_int == -1:
    break
  if(in_int%3 == 0 and in_int%5 == 0): 
    print('Fizz Buzz')
  elif (in_int%3 == 0):
    print('Fizz')
  elif( in_int%5 == 0):
    print("Buzz")
  else:
    print("Oops")
