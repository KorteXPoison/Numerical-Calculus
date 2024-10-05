import sympy

def Newton(f, x0, tolerancia = 0.001, num_max_iteracoes = 20):
	num_max_iteracoes_original = num_max_iteracoes

	sympy_x = sympy.symbols("x")
	derivada = sympy.diff(f, sympy_x)

	xn = x0
	diferenca = float('inf')

	while tolerancia <= diferenca and num_max_iteracoes:
		x_proximo = xn - f.evalf(subs={sympy_x: xn})/derivada.evalf(subs={sympy_x: xn})
		diferenca = abs(xn-x_proximo)
		num_max_iteracoes -= 1
		xn = x_proximo

	err = 'número máximo de iterações excedido' if diferenca > tolerancia else None
	return [xn, diferenca, num_max_iteracoes_original-num_max_iteracoes, err]


# f = sympy.sympify("2*x**3+5*x**2-3*x+2")

f = None
try:
	f = sympy.sympify(input("função: "))
except Exception as e:
	print("Sintaxe Incorreta")
	exit()

x0 = float(input("x0: "))

tolerancia = input("tolerancia (0.001): ")
tolerancia = float(tolerancia) if tolerancia else 0.001

num_max_iteracoes = input("número máximo de iterações (20): ")
num_max_iteracoes = int(num_max_iteracoes) if num_max_iteracoes else 20

print(Newton(f, x0, tolerancia, num_max_iteracoes))