class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

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

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize2(serialize2(node)).left.left.val == 'left.left'
assert deserialize2(serialize2(node)).right.val == 'right'

