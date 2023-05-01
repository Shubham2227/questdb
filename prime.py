# Python3 program to check whether a number
# is prime or not using recursion

# Function check whether a number
# is prime or not


def isPrime(n, i):

	# Corner cases
	if (n == 0 or n == 1):
		return False

	# Checking Prime
	if (n == i):
		return True

	# Base cases
	if (n % i == 0):
		return False

	i += 1

	return isPrime(n, i)


# Driver Code
if (isPrime(35, 2)):
	print("true")
else:
	print("false")

# This code is contributed by bunnyram19
