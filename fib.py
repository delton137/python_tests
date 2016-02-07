#Different ways of calculating the Fibonacci sequence
#D. Elton 2016

from test_routines import *
from memoized import *

#--- normal recursive Fibonacci number calculator -------------
def recursive_fib(n):
  if n < 2:
    return 1
  else:
    return recursive_fib(n-1) + recursive_fib(n-2)

#--- memoized recursive Fibonacci number calculator -------------
@memoized
def memoized_recursive_fib(n):
  if n < 2:
    return 1
  else:
    return memoized_recursive_fib(n-1) + memoized_recursive_fib(n-2)


#--- simple iteration -------------------------------------------
def iter_fib(n):
	if n < 2:
		return 1
	rnm1 = 2
	rnm2 = 1
	for i in xrange(n-2):  
		rn = rnm1 + rnm2
		rnm2 = rnm1
		rnm1 = rn
	return rn


#--- iteration using matrix multiplication ----------------------
M = matrix([[1, 1], [1, 0]])
def matrix_iter_fib(n):
  if n < 2:
    return 1
  MProd = M.copy()
  for i in xrange(n-2):
    MProd *= M
  return MProd[0,0] + MProd[0,1]


#--- direct computation ------------------------------------------
def direct_fib(n):	
	s5 = sqrt(5)
	return int( (1/s5)*( ((1 + s5)/2)**(n+1) - ((1 - s5)/2)**(n+1) ) )


functs_to_test = [recursive_fib, memoized_recursive_fib, iter_fib, matrix_iter_fib, direct_fib]

#print_comparison(functs_to_test,5)
plot_scaling(functs_to_test)





