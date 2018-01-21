# Number theory

def gcd(p, q):
	if p == q:
		return p
	elif p < q:
		return gcd(q, p)
	else:
		return gcd(p-q, q)

class Rational:
	def __init__(self, p, q):
		g = gcd(p, q)
		self.p = p // g
		self.q = q // g

	def __str__(self):
		return str(self.p)+"/"+str(self.q)

	def __repr__(self):
		return str(self)