#np.isinf() 10*1000                inf means infinity
#this function returns either true or false 
#this function checks whether a value in a function is infinite or not 



import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))


