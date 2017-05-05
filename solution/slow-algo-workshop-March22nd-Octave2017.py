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
list_reviews = []
NumberReviews = 0
average = 0.0

# loop over a certain number of reviews 
for x in range(10000):
    # get review
    review = randint(0,5)
    # add the review to the list
    list_reviews.append(review)
    # update the number of reviews
    NumberReviews = NumberReviews + 1
    # set the sum to 0 again
    Sum = 0.0
    # compute the sum
    for y in list_reviews:
       Sum = Sum + y
    # compute the average
    average = Sum / NumberReviews

#print the average on screen
print "\n"
print "The average is ", average
print "\n"
#print the time duration
print("--- %s seconds ---" % (time.time() - start_time))
