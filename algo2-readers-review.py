###########################################
#
#       Author Aurelie Jean, PhD
#      In Silico Veritas, LLC (NYC)
#       aurelie@silicoveritas.com
#               2017
###########################################

# ---- libraries 
# for random integer 
from random import randint
# for time
import datetime
import time

# storage
Sum = 0.0
NumberReviews = 0
average = 0.0

# artificial time (would not exist in the code)
now = datetime.datetime.now()
minute = now.minute

# while we are still under 1 minute
while minute < 25 :
    # get review
    review = randint(0,5) 
    # update the number of reviews
    NumberReviews = NumberReviews + 1
    # compute the sum
    Sum = Sum + review
    # compute the average
    average = Sum / NumberReviews
    # update time
    now = datetime.datetime.now()
    minute = now.minute

# to get the time of execution
start_time = time.time()

#print the average on screen
print "\n"
print Sum, NumberReviews
print "The average is ", average
print "\n"

print("--- %s seconds ---" % (time.time() - start_time))
