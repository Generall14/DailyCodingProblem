class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def serialize(self):
		temp = "["+str(self.val)+"&"
		if self.left:
			temp += self.left.serialize()
		temp += "$"
		if self.right:
			temp += self.right.serialize()
		temp += "]"
		return temp

#wrapper:
def serialize(node):
	return node.serialize()

# [val&left$right]
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
