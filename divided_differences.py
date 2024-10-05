

def read_column():
	column = []
	while True:
		text_input = input().strip()
		if not text_input: break
		column.append(float(text_input))
	return column






def DividedDifferencesCoeffs(x_arr, y_arr):
	num_iter = len(y_arr)-1

	arr = [[] for i in range(num_iter+1)]
	arr[0] = [e for e in y_arr]


	for n in range(1, num_iter+1):
		for i in range(num_iter-n+1):
			numerator = arr[n-1][i+1]-arr[n-1][i]
			denominator = x_arr[(i+n)]-x_arr[i]
			arr[n].append(numerator/denominator)

	return [e[0] for e in arr], arr


def DividedDifferencesEval(x, x_arr, coefficients):
	result = 0
	for coeff_index, coeff in enumerate(coefficients):
		
		multiplier = 1
		for i in range(coeff_index):
			multiplier *= x-x_arr[i]

		result += coeff*multiplier
	print()

	return result








x_arr = []
y_arr = []

print("Insira a coluna x: ")
x_arr = read_column()
if len(x_arr) < 2:
	print("insira pelo menos 2 valores")
	exit()

print("Insira a coluna y: ")
y_arr = read_column()
if len(y_arr) != len(x_arr):
	print("coluna y tem que ter a mesma quantidade de elementos da coluna x")
	exit()

coefficients, matrix = DividedDifferencesCoeffs(x_arr, y_arr)

print("Coeficientes:", coefficients)
print()

while True:
	text_input = input("Insira um valor de x para interpolar: ").strip()
	if not text_input: break
	value = float(text_input)
	print(DividedDifferencesEval(value, x_arr, coefficients))