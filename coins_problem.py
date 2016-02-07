#solves coins problem - given an unlimted supply of coins with different denominations, 
# how many ways can one make change for amount N ?
# D. Elton 2016
from memoized import *
from test_routines import *

coins = [1,5,10,25]

#-----------recursive solution, memoized -----------------------  
#@memoized
def count(remainder):
	if remainder == 0:
		return 1.0
	if remainder > 0:
		pass
	if remainder < 0:
		return 0
	return sum(count(remainder - coins) for coins in coins)


#----------------iterative solution-------------------------------
def iter_count_ways(N):
	global coins
	num_coins = len(coins)
	ways = zeros(N+1)

	ways[0] = 1

	#build up each row 
	for j in range(1,N+1):         #j = jth column
		for coin in coins:     
			if ((j - coin) >= 0):  
				ways[j] += ways[j - coin]
	return ways[N]



functs_to_test = [count, iter_count_ways]

plot_scaling(functs_to_test)


