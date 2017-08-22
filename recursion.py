"""
Demonstrations of recursion for pedagogical use.
"""

def power(x, n):
	if n == 0:
		return 1.0
	elif 0 < k:
		return x * power(x, n-1)
	else:
		return 1.0/power(x,-n)

def combo(n, r):
	"""
	Compute C(n, r) - the number of combinations of r items out of n items.
	Uses recursion relation from Pascal's Triangle. 
	Proof (LaTeX): {{n-1} \choose {r-1}}+{{n-1} \choose r}=\frac{(n-1)!}{(n-r)!(r-1)!}+\frac{(n-1)!}{(n-r-1)!r!}
	Note: inefficent method.
	"""
	if r < 0 or n < r:
		return False # Error
	elif r == 0 or r == n:
		return 1 # Base case
	else:
		return combo(n-1, r) + combo(n-1, r-1) # Recursive case

def run_combo():	
	assert combo(5, 2) == 10
	print combo(5, 2)

# Mutally recursive functions.
def collatz(n):
	if n == 1:
		print n
		return 0
	else:
		print str(n) + " -> ",
		if n % 2 == 0:
			return collatz_even(n)
		else:
			return collatz_odd(n)

def collatz_even(n):
	return collatz(n/2)

def collatz_odd(n):
	return collatz((3*n)+1)

def run_collatz():
	collatz(3) # Should print 3 ->  10 ->  5 ->  16 ->  8 ->  4 ->  2 ->  1

# run_combo()

class IntList:
	def __init__(self, v=None, n=None):
		self.value = v
		self.next = n
	
	def get_value(self):
		return self.value

	def get_next(self):
		return self.next

	def set_value(self, v):
		self.value = v

	def set_next(self, n):
		self.next = n

	def find_last(self):
		if self.get_next() == None:
			return self
		else:
			return self.get_next().find_last()

	def append(self, v):
		self.find_last().set_next(IntList(v, None))

	def __str__(self):
		if self.get_next() == None:
			return str(self.get_value())
		else:
			return str(self.get_value()) + ' -> ' + str(self.get_next())

	def get_sum(self):
		if self.get_next() == None:
			return self.get_value()
		else:
			return self.get_value() + self.get_next().get_sum()

def get_sum_with_args(lst):
	if lst == None:
		return 0
	else:
		return lst.get_value() + get_sum_with_args(lst.get_next())


def run_intlist():
	lst = IntList(2, None)
	lst.append(3)
	lst.append(5)
	lst.append(7)
	assert lst.get_sum() == 17
	assert get_sum_with_args(lst) == 17
	print lst
	print "Sum :", lst.get_sum()

# run_intlist()



def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def tr_factorial(n, accumulator):
	"""Tail recursive implementation of factorial function."""
	if n == 0:
		return accumulator
	else:
		return tr_factorial(n-1, accumulator*n)

def run_tr_factorial(n):
	return tr_factorial(n, 1)

# print factorial(5)
# print run_tr_factorial(100)

def fib(n):
	"""
	Naive implementation of Fibonacci function. 
	Extremely slow performance with n = 100.
	"""
	if n == 0 or n == 1:
		return 1
	else: 
		return fib(n-1) + fib(n-2)

def tr_fib(a, b, n):
	"""Tail recursive implementation of Fibonacci function."""
	if n <= 0:
		return b
	else:
		return tr_fib(b, a+b, n-1)

def run_tr_fib(n):
	return tr_fib(0,1,n)

# print fib(10)
# print run_tr_fib(10)

""" Recursive implementation of prime factorization. """

def prime_factorize(n):
	return tr_prime_factorize(n, 2)

def tr_prime_factorize(n, fac):
	if n == 1:
		return []
	elif n % fac == 0:
		return [fac] + tr_prime_factorize(n/fac, fac)
	return tr_prime_factorize(n, fac+1)

def test_prime_factorize():
	assert prime_factorize(120) == [2, 2, 2, 3, 5]

"""

Step-by-step follow-through:

prime_factorize(99)
= tr_prime_factorize(99, 2)
= tr_prime_factorize(99, 3)
= [3] + tr_prime_factorize(33, 3)
= [3] + [3] + tr_prime_factorize(11, 3)
= [3] + [3] + tr_prime_factorize(11, 4)
= [3] + [3] + tr_prime_factorize(11, 5)
.
.
= [3] + [3] + tr_prime_factorize(11, 11)
= [3] + [3] + [11] + tr_prime_factorize(1, 11)
= [3] + [3] + [11] + []
= [3,3,11]

>>> prime_factorize(799964687**20) # 799964687 = 919 * 929 * 937
[919, 919, 919, 919, 919, 919, 919, 919, 919, 919, 919, 919, 919, 
 919, 919, 919, 919, 919, 919, 919, 929, 929, 929, 929, 929, 929, 
 929, 929, 929, 929, 929, 929, 929, 929, 929, 929, 929, 929, 929, 
 929, 937, 937, 937, 937, 937, 937, 937, 937, 937, 937, 937, 937, 
 937, 937, 937, 937, 937, 937, 937, 937]

>>> prime_factorize(799964687**100)
RuntimeError: maximum recursion depth exceeded in cmp

Note to self: Python does not have tail recursion optimization and 
recursion has a limit of ~1000 calls.

"""

def palindrome(s):
	"""Recursive implementation of a palindrome checker."""
	if len(s) < 2:
		return True
	elif s[0] != s[-1]:
		return False
	else:
		return True and palindrome(s[1:-1])

"""

palindrome('lol')
= True and palindrome('o')
= True and True


palindrome('seas')
= True and palindrome('ea')
= True and False

"""

def count_change(n, coins):
	if n == 0:
		return 1
	elif n < 0 or coins == []:
		return 0
	else:
		return count_change(n, coins[:-1]) + count_change(n-coins[-1], coins)


"""
There are 3 ways to make 10 cents with pennies and nickels:

1+1+1+1+1+1+1+1+1+1+1
1+1+1+1+1+1+5
5+5

count_change(10, [1,5])
= count_change(10, [1]) + count_change(5, [1,5])
= [count_change(10, []) + count_change(9, [1])] + [count_change(5, [1]) + count_change(0, [1,5])]
= [[0 + count_change(9, [])] + count_change(8, [1])] + [(basically 1) + (basically 1)]
= [0 + 0 + (basically 1)] + [(basically 1) + 1 +]

count_change(5, [1,5])
= count_change(5, [1]) + count_change(0, [1,5])
= (count_change(5, []) + count_change(4, [1])) + 1
= [0 + 0 + 0 + 0 + 1] + 1
= 2

count_change(5, [1])
= count_change(5, []) + count_change(4, [1])
= 0 + count_change(4, []) + count_change(3, [1])
= (basically 1)
= 1

"""

def test_count_change():
	assert count_change(10,[1,5]) == 3
	assert count_change(5,[1,5]) == 2
	assert count_change(5,[1]) == 1






