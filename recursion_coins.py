import time

coins = [1,5,10,25]

possibilities = [[]]
i = 0

def count(coins, n, num_coins_used=0):
	if (n == 0):
		return 1
	
	if (m < 0 & n >= 1):
		return 0
	
	return count(coins, n, num_coins_used-1) +  count(coins, n, num_coins_used-1)


def iter_count(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            ways[j] += ways[j - coin]
    return ways[amount]


#----time a function -------------------------------------------------
def time_funct(function, args, output=False):
	t0 = time.time()
	result = function(args)
	t1 = time.time()
	ElapsedTime = t1-t0
	if output: print("%25s: %i  time: %8.2e seconds" % (function.func_name, result, ElapsedTime) )
	return ElapsedTime

#----given list of functions of form f(n), plot scaling with n -------
def plot_scaling(functs_to_test,num_tests=20,max_value = 1000,max_time  = .1,title=""):
	'''Inputs: 
		functs_to_test : list of unctions 
		num_tests      : number of tests to perform type:int
		max_value      : maximum value to test type:int
		max_time       : stop when execution time reaches this value (seconds)
		title 		   : optional title string for plot
	'''
	nvalues = floor(logspace(1, log10(max_value), num_tests))
	times = zeros(num_tests)
	
	for f in functs_to_test:
		for i in range(num_tests):
			times[i] = time_funct(f, int(nvalues[i]))
		
			#if runtime is becoming too long, bail out of the test
			if (float(times[i]) > max_time):
				break 	
		plt.loglog(nvalues, times, "*-", label=f.func_name)
	
	plt.legend()
	plt.xlabel("value")
	plt.ylabel("time (s)")
	plt.title(title)
	plt.show()
	
#----print out comparison of times for a list of functions -------
def print_comparison(functs_to_test, n):
	for f in functs_to_test:
		time_funct(f, n, output=True)

functs_to_test = [count, iter_count]

print_comparison(functs_to_test,[coins, n])
plot_scaling(functs_to_test)