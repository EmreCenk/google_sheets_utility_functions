

	
def method1(num1, num2):
  # Method 1 of finding what num1*num1*num2 is
	a = num1**2
	b = a * num2
	return b

def method2(num1, num2):
  # Method 2 of finding what num1*num1*num2 is
	a = num1*num2
	b = a*num1
	return b

def prove_everyone_wrong():
	"""
	A simulation I wrote to prove that there could, in theory, be a decimal difference depending on how we multiply very big and very small floats.
	The issue came up when a rounding/floating point inaccuracy resulted in a gigantic difference when looking model predictions in my MDM4UI (Data Management) Course. 
	
	THESIS
	With very large and very small decimals, there can theoretically be difference when the order of operation is changed during multiplication.
	
	In other words:
	Let a, b ∈ Q.
	We consider the multiplying in the following orders: (a*a)*b and a*(a*b). In theory, this order
	difference could create different outcomes at extreme a and b values. Such an example is when:
	1) There is an extremely large a value
	2) There is an extremely small b value with very long decimal digits.
	
	
	The reason for this is that when a is an extremely big number, it becomes very difficult to compute a*a with high precision. 
	The same goes for when b is an extremely small value with very long decimals. 
	
	When you compute (a*a), then multiply that with b, you end up multiplying a gigantic number with an extremely small number with lots of decimals.
	In these circumstances, it becomes very difficult to maintain floating point accuracy. 
	
	However, if we first find (a*b), then multiply that number with a, what we have is a relatively normal number, multiplied with a relatively big number.
	With these circumstances, it becomes much easier to maintain floating point accuracy. 
	
	To prove this, I wrote this simulation where I would test this theory by generating extreme examples of the concept/theory given above. 
	
	
	RESULTS
	After simulating thousands of combinations and comparing the multiplication methods, the biggest difference I found between the two methods was a difference of ~0.01 .
	It does not seem very significant at first, but when dealing with very large numbers, this difference becomes crucial.
	
	Overall, this phenomena does make a difference at extreme examples, however does not effect many scenarios in practice. 
	The only potential application I can see is cryptography. However, many specialized libraries have already been developed for such 
	use cases. 
	
	In conclusion, I am happy to have proved my point.
	"""
	print("\n"*100)

	limit = 1000
	starting = 10000
	random = 0.00923

	maxnodecimal = 1000000
	besti = 0
	bestj = 0

	total_example_number = 0
	for i in range(limit):
		starting += 100000
		
		r1 = method1(starting, random) 
		r2 = method2(starting, random)
		if r1 != r2:
			# print(starting, random, r1, r2)
			total_example_number += 1
			dif = abs(r1-r2)
			if dif < maxnodecimal:
				maxnodecimal = dif
				besti = starting
				bestj = random

	print("Final example number:",total_example_number)
	print(besti, bestj, maxnodecimal)

def automate1(a = ""):
	if a == "":
		a = """32.7	24.4	25.7	23.8	19.3	25.1	26.7	32.1	30	31.6	19.4	23.1
		28.9	30.6	29.2	34	32.2	34.5	30.2	29.3	27.2	28.1	20.4	17.7
		29.8	31.8	33.3	30.9	30.8	32.8	30.4	29.8	20.9	26.5	23.6	15.9
		29.6	32.4	34.1	27.4	28.8	26.9	27	28.3	29.1	30	26.7	16.8
		29.7	29.1	29.3	33.3	33.5	27.7	26.7	29	29.3	19.5	28.4	
		24.1	22.7	24.4	26.6	22	25.6	26.4	22.5	22.3	24.1	18.3	
		22	24.5	26.4	28.4	29.6	31.2	29.3	25.4	26	24.2	18.8	
		28.6	31.9	28.9	28.5	29.9	23.1	27.7	27.7	27	18.8	24	"""

	print("\n"*100)
	a=a.split("\n")
	for i in range(len(a)):
		a[i] = a[i].split("\t")

	x = 0
	for collum in range(len(a[0])):
		for row in range(len(a)):
			print(a[row][collum])
			x+=1

	print(x)


a = """
0 20 0 3 10 60 0 50
1 40 1 10 20 30 1 62
2 65 2 9 30 20 2 68
3 80 3 16 40 15 3 72
4 92 4 15 60 10 4 74
5 108 5 22
6 21
7 28
8 27
9 34"""
a = a.replace(" ", "\t")
print(a)
