
def max_num(a, b, c):
    return max [(a,b,c)]

print(max_num(1, 2, 3))
print(max_num(7, 2, 4))
print(max_num(80, 90, 101))



def mult_list(list):
    if len(lst) == 0:
        return 0
    
    prod = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i
            
    return prod

print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))



def rev_string(str):
    return str[::-1]

print(rev_string(""))
print(rev_string("berrys"))
print(rev_string("The 1975"))


def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

"""

def pascal():
	#your code here

pascal(1)
'''
output:
1
'''

pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
"""