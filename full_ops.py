# full_ops.py
# cd Desktop\Phyton
# Usage: python3 full_ops.py c_in n_wv
#  Example: python3 full_ops.py 120 84
#  84
#  1
#  1
#  10080
#  10080
#  0
# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors
#  ...
# Output:
#  print(int(c_out)) # output channel count
#  print(int(h_out)) # output height count
#  print(int(w_out)) # output width count
#  print(int(adds))  # number of additions performed
#  print(int(muls))  # number of multiplications performed
#  print(int(divs))  # number of divisions performed
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# initialize script arguments
c_in = 0.0
n_wv = 0.0

# parse script arguments
if len(sys.argv)==3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
    
else:
   print(\
    'Usage: '\
    'full_ops.py c_in n_wv'\
   )
   exit()
##===============================================
c_out = n_wv
muls = n_wv*c_in
adds = n_wv*c_in
#Due to a fully connected layer
divs = 0
h_out = 1
w_out = 1

#output
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed