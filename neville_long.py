

def read_column():
	column = []
	while True:
		text_input = input().strip()
		if not text_input: break
		column.append(float(text_input))
	return column

def Neville(x, x_arr, y_arr):
	num_iter = len(y_arr)-1

	arr = [[float("nan")]*i for i in range(num_iter+1)]
	arr[0] = [e for e in y_arr]


	for j in range(1, num_iter+1):
		for i in range(j, num_iter+1):
			numerator = (x-x_arr[i-j])*arr[j-1][i]-(x-x_arr[i])*arr[j-1][i-1]
			denominator = x_arr[i] - x_arr[i-j]
			print(f"     (x-x_arr[{i-j}])*arr[{j-1}][{i}]-(x-x_arr[{i}])*arr[{j-1}][{i-1}]     /     x_arr[{i}] - x_arr[{i-j}]")
			print(f"     (x-{x_arr[i-j]})*{arr[j-1][i]}  -  (x-{x_arr[i]})*{arr[j-1][i-1]}     /     {x_arr[i]} - {x_arr[i-j]}")
			print(f"     {numerator/denominator}")
			print(f"     -")
			arr[j].append(numerator/denominator)
		print("---------------------")

	return arr[-1][-1], arr




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


while True:
	text_input = input("Insira um valor de x para interpolar: ").strip()

	if not text_input: break
	value = float(text_input)
	result, matrix = Neville(value, x_arr, y_arr)
	print(matrix)
	print("------------")
	print(result)