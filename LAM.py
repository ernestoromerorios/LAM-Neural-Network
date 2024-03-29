import numpy as np
from fractions import Fraction
import os

patterns = int(input("Number of patterns: "))
inn = int(input("Number of input neurons: "))
outn = int(input("Number of output neurons: "))
patin = []

aux = True
minus = 0

for i in range(patterns):
    print(f"\nInput vector #{i+1}\n")
    patin.append([])
    for j in range(inn):
        patin[i].append(int(input(f"Data #[{j+1}]: ")))
        if aux and (patin[i][j] == 0):
        	minus = 0
        	aux = False
        if aux and (patin[i][j] == -1):
        	minus = -1
        	aux = False

patout = []

for i in range(patterns):
    print(f"\nOutput vector #{i+1}\n")
    patout.append([])
    for j in range(outn):
        patout[i].append(int(input(f"Data #[{j+1}]: ")))
        if aux and (patin[i] == 0):
        	minus = 0
        	aux = False
        if aux and (patin[i] == -1):
        	minus = -1
        	aux = False

w = []

if (inn == outn):
	print("Square Matrix")
	square = True
	for i in range(inn):
		w.append([])
		for k in range(outn):
			suma = 0
			for j in range(patterns):
				suma += ((2*patin[j][i])-1)*((2*patout[j][k])-1)
				print(f'([2*{patin[j][i]}]-1)*([2*{patout[j][k]}]-1)',end=" ")
				if ((j+1) != (patterns)):
					print("+ ",end="")
			print(f'= {suma}\n')
			w[i].append(suma)

else:

	square = False
	for i in range(inn):
		w.append([])
		for k in range(outn):
			suma = 0
			for j in range(patterns):
				suma += ((2*patin[j][i])-1)*((2*patout[j][k])-1)
				print(f'([2*{patin[j][i]}]-1)*([2*{patout[j][k]}]-1)',end=" + ")
			print(f' = {suma}\n')
			w[i].append(suma)	

print("Weight Matrix:\n")
for i in range(len(w)):
	print("[",end="")
	for j in range(len(w[i])):
		if j+1 == len(w[i]):
			print(f"{w[i][j]}", end="")
		else:
			print(f"{w[i][j]}", end=",")
	print("]")
print("\n")

if not(square):
	print("Non-Square Matrix. Must be transposed.")
	w = np.transpose(w)
	print("Weight Matrix (TRANSPOSED):\n")
	for i in range(len(w)):
		print("[",end="")
		for j in range(len(w[i])):
			if j+1 == len(w[i]):
				print(f"{w[i][j]}", end="")
			else:
				print(f"{w[i][j]}", end=",")
		print("]")
	print("\n")

bias = []
print("Bias:")

print("[",end="")
for i in range(len(w)):
	suma = 0
	for j in range(len(w[i])):
		suma += w[i][j]
	bias.append(suma*(-0.5))
for i in range(len(bias)):
	print(f"{Fraction(str(bias[i])).limit_denominator()}", end="")
	if ((i+1) != (len(bias))):
		print(",",end="")
print("]\n")

print("Patterns Evaluation:\n")

for i in range(len(patin)):
	print(f"Evaluation X{i+1}")
	aux = np.dot(w,patin[i])+(np.array(bias))
	aux[aux >= 0] = 1
	aux[aux < 0] = minus
	if (np.allclose(np.array(aux),np.array(patout[i]))):
		print(f"{np.array(aux)} Correctly associates with {np.array(patout[i])} (Y{i+1})")
	else:
		print(f"{np.array(aux)} Does not associate correctly")

