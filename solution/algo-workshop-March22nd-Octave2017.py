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
list_reviews = []

# --- WRITE CODE HERE --- 
for i in range(100000):
    # get my review
    my_review = randint(0,5)
    list_reviews.append(my_review)
    
    # update the number of reviews
    Number_reviews = Number_reviews + 1
    
    Sum = 0.0 
    # ---- compute the average ----
    # 1) compute the sum
    for j in list_reviews:
      Sum = Sum + j 
    # 2) divide by the number of reviews
    average = Sum / Number_reviews
    # -----------------------------

# after the loop print the average
print "the average is =", average
# -----------------------

#print the time duration
print("--- %s seconds ---" % (time.time() - start_time))

