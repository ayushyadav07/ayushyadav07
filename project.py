import time;   #importing time module
n=0                           
sec=1     #for 1 second
stime=time.time()    #starting time
while 1:                      
    ctime=time.time()     #current time
    ttime=ctime-stime      #total time
    if ttime>sec:      #condition of termination
        print(n)              
        break       #exiting out of the loop
    n=n+1        #incrementing value of n by 1
