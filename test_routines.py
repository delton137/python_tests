import time
import collections
import functools
from numpy import *
import matplotlib.pyplot as plt

#----time a function -------------------------------------------------


def time_funct(function, args, output=False):
	t0 = time.time()
	result = function(args)
	t1 = time.time()
	ElapsedTime = t1-t0
	if output: print("%25s: %i  time: %8.2e seconds" % (function.func_name, result, ElapsedTime) )
	return ElapsedTime

#----given list of functions of form f(n), plot scaling with n -------
def plot_scaling(functs_to_test,num_tests=20,max_value = 500,max_time  = .05):
	'''Inputs: 
		functs_to_test : list of unctions 
		num_tests      : number of tests to perform type:int
		max_value      : maximum value to test type:int
		max_time       : maximum time in seconds
	'''
	nvalues = floor(logspace(1, log10(max_value), num_tests))
	times = zeros(num_tests)
	
	for f in functs_to_test:
		for i in range(num_tests):
			times[i] = time_funct(f, int(nvalues[i]))
			
			#f.cache = {}
		
			#if runtime is becoming too long, bail out of the test
			if (float(times[i]) > max_time):
				break 	
		plt.loglog(nvalues, times, "*-", label=f.func_name)
	plt.legend()
	plt.xlabel("value")
	plt.ylabel("time (s)")
	plt.show()
	
#----print out comparison of times for a list of functions -------
def print_comparison(functs_to_test, n):
	for f in functs_to_test:
		time_funct(f, n, output=True)
