import sympy
sympy_x = sympy.symbols("x")

n = 4

f = None
try:
	f = sympy.sympify(input("função: "))
except Exception as e:
	print("Sintaxe Incorreta")
	exit()
a = float(input("insira o a: "))
b = float(input("insira o b: "))

h = (b-a)/n


x_arr = [a+i*h for i in range(n+1)]
y_arr = [f.evalf(subs={sympy_x: x}) for x in x_arr]

result = (2/45)*h*(y_arr[0]*7+y_arr[1]*32+y_arr[2]*12+y_arr[3]*32+y_arr[4]*7)
print(result)

