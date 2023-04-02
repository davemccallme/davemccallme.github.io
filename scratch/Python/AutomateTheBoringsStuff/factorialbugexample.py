# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:24:52 2019

@author: DavidM
"""

#Title: buggy problem example

#About: this program calulates factorials

################################################################
#turn off all logging messages in shell
#logging.disable(logging.CRITICAL)
################################################################


import logging   #add debuging log messages to shell
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)')

logging.debug('Start of Program')


#Variables
x = 1
y = 5

#Definitions
def factorial(n):
    logging.debug('Start of factorial is (%s)' % (n))
    total = x



####### PROGRAM START #######################
    
    logging.debug('Start of Program')
    
    for i in range(1, n+1):             #note range starts typically  at 0 
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is %s' %(total))    
    return total
    
print(factorial(y))

logging.debug('End of program')