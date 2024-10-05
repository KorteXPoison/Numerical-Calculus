import re
import numpy as np

def DiagonallyDominant(m): return not max([sum([abs(e) for e in r[:len(m)]])-abs(r[r_i])*2 > 0 for r_i, r in enumerate(m)])
def DiagonallyDominantStrict(m): return not max([sum([abs(e) for e in r[:len(m)]])-abs(r[r_i])*2 >= 0 for r_i, r in enumerate(m)])
def Det(m): return np.linalg.det(np.array(m)[:, :len(m)])



def InputRow():
	text = input().strip()
	if not text: return []
	row_text = re.split(r"\s+", text)
	row = [float(entry) for entry in row_text]
	return row

def InputMatrix():
	row = InputRow()
	if not row: return None
	matrix = [row]
	while row := InputRow():
		if len(row) != len(matrix[0]): return None
		matrix.append(row)
	return matrix




def FuncFromString(code_str):
	code_str = re.sub(r"def \w+", "def ffs", code_str)
	# print(code_str)
	exec(code_str) 				#https://docs.python.org/3/library/functions.html#exec (executa string como código)
	return locals()["ffs"]		#retornar a definição da função 'ffs' presente nas variáveis locais

def GaussSeidel_FunctionVec(matrix):
	func_vec = []
	for row_index, row in enumerate(matrix):
		row_code = ""
		for elem_index, elem in enumerate(row[:-1]):
			if elem_index == row_index: continue
			row_code += f"+{elem}*x[{elem_index}]"
		row_code = f"({row[-1]}-({row_code}))/{row[row_index]}"
		row_code = f"def fun(x): return {row_code}"
		fun = FuncFromString(row_code)
		func_vec.append(fun)
	return func_vec

def GaussSeidel(func_vec, x_vec = [], tolerancia = 0.0001, num_max_iter = 10):
	if not x_vec: x_vec = [0]*len(func_vec)

	diff = float('inf')
	while diff > tolerancia and num_max_iter:
		
		x_vec_old = [x for x in x_vec]

		for i in range(len(x_vec)): x_vec[i] = func_vec[i](x_vec) #gauss-seidel

		diff = max([abs(x_vec[i]-x_vec_old[i]) for i in range(len(x_vec))])

		num_max_iter -= 1
	
	err = 'número máximo de iterações excedido' if diff > tolerancia else None

	return x_vec, diff, err


print("Insira a matriz A+B:")
matriz = InputMatrix()
if not matriz: 
	print("matriz errónea")
	exit()

print("Insira a matriz x0 (0n):")
x_vec = InputMatrix()
if not x_vec: x_vec = [0]*len(matriz)

tolerancia = input("tolerancia (0.001): ")
tolerancia = float(tolerancia) if tolerancia else 0.0001
print()

num_max_iteracoes = input("número máximo de iterações (10): ")
num_max_iteracoes = int(num_max_iteracoes) if num_max_iteracoes else 10
print()



dd = DiagonallyDominant(matriz)
dds = DiagonallyDominantStrict(matriz)
d = Det(matriz)
print("Diagonalmente Dominante: ", "sim" if dd else "não")
print("Diagonalmente Dominante (estrito): ", "sim" if dd else "não")
print("Determinante: ", d)

if d==0:
	print("Este sistema não tem solução, ou a solução contem 0=0. Pretende continuar? s/n (s):", end="")
	resposta = input()
	if resposta == 'n': exit()
elif not dd:
	print("Esta matriz não é diagonalmente dominante e pode não converger. Pretende continuar? s/n (s):", end="")
	resposta = input()
	if resposta == 'n': exit()
elif not dds:
	print("Esta matriz não é estritamente diagonalmente dominante e pode não converger. Pretende continuar? s/n (s):", end="")
	resposta = input()
	if resposta == 'n': exit()
print()


func_vec = GaussSeidel_FunctionVec(matriz)

resultado = GaussSeidel(func_vec, x_vec, tolerancia, num_max_iteracoes)

if resultado[2] is not None:
	print("!!!", resultado[2], "!!!")
	print(f"Resultado provisório: ", end="")#x1:{resultado[0][0]}, x2:{resultado[0][1]}, x3:{resultado[0][2]}")
	for i, x in enumerate(resultado[0]): print(f"x{i+1}:{x}; ", end="")
	print()
	print(f"Erro obtido: {resultado[1]}")
	exit()
print(f"Resultado: ", end="")#x1:{resultado[0][0]}, x2:{resultado[0][1]}, x3:{resultado[0][2]}")
for i, x in enumerate(resultado[0]): print(f"x{i+1}:{x}; ", end="")
print()
print(f"Maior erro final: {resultado[1]}")


# 9 2 3 7
# 1 12 9 2
# 4 6 14 1
