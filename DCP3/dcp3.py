class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


#Wersja 1, oparta na znacznikach, ograniczony zakres znaków w wartościach
# "[val&left$right]"
def serialize(node):
	temp = "["+str(node.val)+"&"
	if node.left:
		temp += serialize(node.left)
	temp += "$"
	if node.right:
		temp += serialize(node.right)
	temp += "]"
	return temp

def deserialize(string):
	left = None
	right = None
	print(string)
	fidx = string.index('&')
	name = string[1:fidx]
	sidx = fidx+1
	if string[sidx]=="[":
		cnt = 1
		while cnt:
			sidx += 1
			if string[sidx]=="[":
				cnt += 1
			if string[sidx]=="]":
				cnt -= 1
		left = deserialize(string[fidx+1:sidx+1])
	tidx = sidx+1
	if string[tidx]=="[":
		cnt = 1
		while cnt:
			tidx += 1
			if string[tidx]=="[":
				cnt += 1
			if string[tidx]=="]":
				cnt -= 1
		right = deserialize(string[sidx+1:tidx+1])
	return Node(name, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
#assert deserialize(serialize(node)).right.val == 'right' # coś tu się jednak pieprzy


# Wersja 2, oparta na wskaźnikach, brak ograniczeń
# "SV-VL-SR->valleftright", gdzie:
# SV - liczba znaków w wartości
# SL - liczba znaków w stringu lewej wartości
# ST - j.w., dla prawej wartości
def serialize2(node):
	if node==None:
		return ""
	sl = serialize2(node.left)
	sr = serialize2(node.right)
	return str(len(node.val))+"-"+str(len(sl))+"-"+str(len(sr))+"->"+node.val+sl+sr


def deserialize2(string):
	print(string)
	v = string.split("-")
	oth = string[string.index(">")+1:]
	name = oth[0:int(v[0])]
	left = None
	right = None
	if int(v[1])>0:
		left = deserialize2(oth[int(v[0]):int(v[0])+int(v[1])+1])
	if int(v[2])>0:
		right = deserialize2(oth[int(v[0])+int(v[1]):int(v[0])+int(v[1])+int(v[2])+1])
	return Node(name, left, right)

assert deserialize2(serialize2(node)).left.left.val == 'left.left'
assert deserialize2(serialize2(node)).right.val == 'right'

