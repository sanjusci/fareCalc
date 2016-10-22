def maximumSubArray(arr):
    maximum,maximum_reset = 0,0
    subarr1,subarr2 = [],[]
    for val in arr:
        maximum_reset += val
        if maximum_reset < 0:
            maximum_reset = 0

        if maximum < maximum_reset:
            maximum = maximum_reset
            subarr1.append(val)
        elif val > 0:
            subarr2.append(val)     
    return [subarr1,subarr2]
 

# Driver function to check the above function 

a = [1, 2, 5, -7, 2, 3]

print "Maximum or Minimum subarray", maximumSubArray(a)

# output : Maximum or Minimum subarray [[1, 2, 5], [2, 3]]
