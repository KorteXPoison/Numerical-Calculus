import sympy

#x0 = xn-2
#x1 = xn-1
def Secant(f, x0, x1, tolerancia = 0.001, num_max_iteracoes = 20):
	num_max_iteracoes_original = num_max_iteracoes
	sympy_x = sympy.symbols("x")

	f_x0 = f.evalf(subs={sympy_x: x0})
	f_x1 = f.evalf(subs={sympy_x: x1})
	diferenca = float('inf')

	while tolerancia <= diferenca and num_max_iteracoes:

		x_novo = x1 - f_x1*(x1 - x0)/(f_x1 - f_x0)
		diferenca = abs(x0-x1)

		x0 = x1
		x1 = x_novo
		f_x0 = f_x1
		f_x1 = f.evalf(subs={sympy_x: x_novo})

		num_max_iteracoes -= 1


	err = 'número máximo de iterações excedido' if diferenca > tolerancia else None
	return [x1, diferenca, num_max_iteracoes_original-num_max_iteracoes, err]


# f = sympy.sympify("2*x**3+5*x**2-3*x+2")

f = None
try:
	f = sympy.sympify(input("função: "))
except Exception as e:
	print("Sintaxe Incorreta")
	exit()

x0 = float(input("x0: "))
x1 = float(input("x1: "))

tolerancia = input("tolerancia (0.001): ")
tolerancia = float(tolerancia) if tolerancia else 0.001

num_max_iteracoes = input("número máximo de iterações (20): ")
num_max_iteracoes = int(num_max_iteracoes) if num_max_iteracoes else 20

print(Secant(f, x0, x1, tolerancia, num_max_iteracoes))