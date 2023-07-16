#random values

import random


class Dice:            # should have two line spaces before and after
    def roll (self):                       #method
        first=random.randint(1,6)                   
        second= random.randint(1,6)
        return first,second                   #it is tuple, so () was not used after return as (first, secnd)
    

dice=Dice()
#print(dice.roll())




#-----------------------------------------------------------------------------------------------------------------


#pathlib used here new instance:

from pathlib import Path  #Path its a class as its P.
# relative path, current to somewhere as.
# absolute path , root of harddisk as c:\program files\microsoft \user\local
# we can check wehther that directory of module is exists.
#path.glob() with such search current directopry , in current path * is all files.






#------------------------------------------------------------------------------------------------------------------------

# pypi google it for packages.


#-----------------------------------------------------------------------------------------------------------------------------


