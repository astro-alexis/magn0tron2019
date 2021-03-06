# ffgen0xx saves an array of filling factor that is an input for the magn0xx procedure
# the final array ff is a 3 x N array, each slice of 3 elements is a combination of filling factors which sum is 100
# the final array is saved into a pickle file.

# Only change the ff_increment variable, which sets the increment between two possible filling factor values.
# for exemple ff_increment = 25 means ff0 = [0,25,50,75,100]

import numpy as np
import pickle
import os as os

print('[info] ffgen0xxx.py | generates filling factor combinations for magn0xx')
print('[info] v1.0 | 2018-11-21 | alexis.lavail@physics.uu.se')
# Variables
ff_increment = 4
ff_max = 100
print('[info] generating a filling factor array with ff_increment={} & ff_max={}'.format(ff_increment,ff_max))
# Creating the filling factors arrays
ff0 = np.arange(ff_max/ff_increment+1, dtype=int) * ff_increment
ff1 = np.arange(ff_max/ff_increment+1, dtype=int) * ff_increment
ff2 = np.arange(ff_max/ff_increment+1, dtype=int) * ff_increment

# ff will store the final array of filling factor
ff = np.empty((0,3), int)
print('[info] entering the main loop')
# looping through all the filling factor possibilities and checking in which cases
# the sum of all filling factor is 100%: is yes -> store into ff array
for ii0 in range(len(ff0)):
    for ii1 in range(len(ff1)):
        for ii2 in range(len(ff2)):
            if ff0[ii0] + ff1[ii1] + ff2[ii2] == 100:
                    ff  = np.append(ff, np.array([[ff0[ii0],ff1[ii1],ff2[ii2]]]), axis=0)


# the main loop is done.
ff = ff.T
print('[result] generated a final array with shape {}'.format(ff.shape))

# Storing the ff array into a HDF5 file now
if os.path.exists('./ff0xx.p'):
    os.remove('./ff0xx.p')
    print('[info] removed an existing "ff0xx.p" file')

pickle.dump( ff, open( "ff0xx.p", "wb" ) )
print('[result] filling factor array saved to "ff0xx.p"')
