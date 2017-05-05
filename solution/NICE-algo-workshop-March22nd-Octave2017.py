###########################################
#
#       Author Aurelie Jean, PhD
#      In Silico Veritas, LLC (NYC)
#       aurelie@silicoveritas.com
#     OCTAVE (March 21st-23rd @Evian)
#               2017
###########################################

# ---- libraries 
# for random integer 
from random import randint
# for time calculation
import time

# start time to compute the time duration of the calculation
start_time = time.time()

# storage
average = 0.0
Number_reviews = 0
Sum = 0.0

# --- WRITE CODE HERE --- 
for i in range(1000000):
    # get my review
    my_review = randint(0,5)
    
    # update the number of reviews
    Number_reviews = Number_reviews + 1
   
    # update the sum
    Sum = Sum + my_review 
    # compute the average by dividing by the number of reviews
    average = Sum / Number_reviews

# after the loop print the average
print "the average is =", average
# -----------------------

#print the time duration
print("--- %s seconds ---" % (time.time() - start_time))

