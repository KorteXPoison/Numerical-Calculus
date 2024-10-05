import sympy

#INPUT QUIRKS:
#e (euler's number) must be input as 'exp(1)' (or 'exp(x)' for e^x)
#pi is just 'pi'
#power symbol can be '^' or '**' (python's)

def sign(x): return 1 if x >= 0 else -1

def Bisec(f, intervalo, tolerancia = 0.0001, num_max_iteracoes = 20):
	sympy_x = sympy.symbols("x")
	err = None

	a, b = intervalo
	m = 0
	f_a = f.evalf(subs={sympy_x: a})
	f_b = f.evalf(subs={sympy_x: b})
	f_m = 0

	while tolerancia <= abs(b-a) and num_max_iteracoes:
		
		m = (a + b)/2
		f_m = f.evalf(subs={sympy_x: m})

		if sign(f_m) != sign(f_a):
			f_b = f_m
			b = m
		elif sign(f_m) != sign(f_b):
			f_a = f_m
			a = m
		else:
			err = 'os sinais são iguais neste intervalo'

		num_max_iteracoes -= 1

	if err is None and abs(b-a) > tolerancia: err = 'número máximo de iterações excedido'
	return [a, b, err]



f = None
try:
	f = sympy.sympify(input("função: "))
except Exception as e:
	print("Sintaxe Incorreta")
	exit()

x0 = float(input("x0: "))
x1 = float(input("x1: "))

if x1 < x0:
	xs = x0
	x0 = x1
	x1 = xs

tolerancia = input("tolerancia (0.001): ")
tolerancia = float(tolerancia) if tolerancia else 0.001

num_max_iteracoes = input("número máximo de iterações (20): ")
num_max_iteracoes = int(num_max_iteracoes) if num_max_iteracoes else 20

print(Bisec(f, [x0, x1], tolerancia, num_max_iteracoes))