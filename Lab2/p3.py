# to check whether year entered is leap year or not
yr = int(input(" Enter year " ))
if((yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0 ):
    print(" It is a leap year " )
else:
    print (" It is not a leap year " )
