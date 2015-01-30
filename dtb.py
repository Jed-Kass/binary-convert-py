from decimal import *


x = raw_input("Please enter your IP: ")
 
 
print sanityCheck(x)
if sanityCheck(x) != True:
    print sanityCheck(x)
else:
    quit


print formatDetection(x)
print binaryToDecimal(x)
    
