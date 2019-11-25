
# Define complex number as pair of real numbers, as in Rudin

class ComplexNumber:

	def __init__(a, b):
		""" a and b should be real numbers """
		self.realc = a
		self.imagc = b

	def norm():
		return math.sqrt(a*a + b*b)

	def conjugate():
		return ComplexNumber(a, -b)

	def __add__(x):
		return ComplexNumber(a + x.a, b + x.b)

	def __neg__(x):
		return ComplexNumber(-x.a, -x.b)

	def __mul__(x):
		return ComplexNumber(a*x.a - b*x.b, a*x.b + b+x.a)

	def inverse(x):
		return ComplexNumber(a, -b)*ComplexNumber(1/(norm()*norm()), 0)

