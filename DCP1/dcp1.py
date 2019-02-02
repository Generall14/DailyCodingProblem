def do(vec, num):
	vec.sort(reverse=True)
	for i in range(len(vec)-1):
		for j in range(i+1, len(vec)):
			if vec[i]+vec[j]==num:
				return [vec[i], vec[j]]
	return False

while True:
	print("Podaj wektor: ")
	ivec = [int(x) for x in input().split()]
	print("Podaj liczbę: ")
	inum = int(input())
	print(do(ivec, inum))
	print("\r\n")
