###########################################
#
#       Author Aurelie Jean, PhD
#      In Silico Veritas, LLC (NYC)
#       aurelie@silicoveritas.com
#     CHANEL (May 24th in NYC)
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
list_reviews = []

SUM = 0
CurrentNumberOfReviews = 0
Average = 0 

# number of online reviews 
NumberOfReviews = 10000;
# loop over a certain number of reviews 
for x in range(NumberOfReviews):
    # get review
    review = randint(0,5)

    # update the number of current reviews
    CurrentNumberOfReviews = CurrentNumberOfReviews + 1

    # update the sum
    SUM = SUM + review

    # update the average
    Average = SUM / CurrentNumberOfReviews

    #I want to print my review average
 

#print the average on screen
print "\n"
print "The average is ", Average
print "\n"
#print the time duration
print("--- %s seconds ---" % (time.time() - start_time))




