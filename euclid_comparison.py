import time

def gcd_normal(a, b):
	start = time.clock()

	if a == 0:
		return b
	if b == 0:
		end = time.clock()
		passed = end - start
		print("Slow: " + str(passed))

		return a
	while a != b:
		if a>b:
			a -= b
		else:
			b -= a

	end = time.clock()
	passed = end - start
	print("Slow: " + str(passed))

	return a

def gcd_advanced(a, b):
	start = time.clock()

	while a != b:
		if a == 0:
			end = time.clock()
			passed = end - start
			print("Fast: " + str(passed))

			return b
		if b == 0:
			return a
		if a > b:
			a = a % b
		else:
			b = b % a

	end = time.clock()
	passed = end - start
	print("Fast: " + str(passed))

	return a


print("---------- Greatest Common Divisor --------\n")

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

print("");
print("Greatest common divisor is: " + str(gcd_normal(num1, num2)) + " (slow)")
print("Greatest common divisor is: " + str(gcd_advanced(num1, num2)) + " (fast)")


