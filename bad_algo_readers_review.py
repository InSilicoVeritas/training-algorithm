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

# ---- storage
average = 0.0
# list of reviews
reviews = []

# artificial time (would not exist in the code)
now = datetime.datetime.now()
minute = now.minute

# while we are still under 1 minute
while minute < 21 :
    # get review
    reviews.append(randint(0, 5))
    # update time
    now = datetime.datetime.now()
    minute = now.minute

# print the reviews on screen
print "\n"
#print "The list of reviews are:\n",reviews
print "\n"

# to get the time of execution
start_time = time.time()

# ---- average the reviews
average = 0.0 
# loop over the reviews to sum them
for i in range(len(reviews)):
    average = average + reviews[i]
# divide by the number of reviews
average = average/len(reviews)
# -----------

#print the average on screen
print "The average is ", average
print "\n"

print("--- %s seconds ---" % (time.time() - start_time))

