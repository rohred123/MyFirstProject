print("This is a kg to lb converter.")
x= input("Please enter your weight : ")
y= input("Enter the units of the weight you put before this. In the format lbs or kgs: ")
x= int(x);
y= y.casefold();
if y=="kgs" or y=="kg":
  print("Weight in pounds is  " + str(x*2.205))
elif y== 'lbs' or y=="lb":
  print("Weight in kg is " + str(x/2.205))
else:
  print ("You can't follow directions.")

name = 'Rohan';
print('Name is ' + name[-2]);
print(len(name))

from scipy.special import gammaln
from math import log, floor

def digits_in_factorial(n):
    return floor( gammaln(n+1)/log(10.0) ) + 1

var=digits_in_factorial(25)
print(var)

function factorial(n) 
    // Put your code here.
    if (n<0){
     console.log("no negatives!");
    }
    if(n === 0){
      return 1;
  }
    return n*factorial(n-1);
}
factorial(100);



























