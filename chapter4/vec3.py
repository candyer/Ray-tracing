
from math import sqrt
class Vec3:
	def __init__(self, e0, e1, e2):
		self.e0 = e0
		self.e1 = e1
		self.e2 = e2
		self.length = sqrt(e0**2 + e1**2 + e2**2)

	def x(self): return self.e0
	def y(self): return self.e1
	def z(self): return self.e2
	def r(self): return self.e0
	def g(self): return self.e1
	def b(self): return self.e2

	def __eq__(self, a):
	 	return self.e0 == a.e0 and self.e1 == a.e1 and self.e2 == a.e2

	def __neg__(self):
		return Vec3(-self.e0, -self.e1, -self.e2)

	def __pos__(self):
		return self

	def __add__(self, other):
		return Vec3(
			self.e0 + other.e0, 
			self.e1 + other.e1, 
			self.e2 + other.e2
		)

	def __sub__(self, other):
		return Vec3(
			self.e0 - other.e0, 
			self.e1 - other.e1, 
			self.e2 - other.e2
		)

	# def __mul__(self, other):
	# 	return Vec3(
	# 		self.e0 * other.e0, 
	# 		self.e1 * other.e1, 
	# 		self.e2 * other.e2
	# 	)

	def __mul__(self, other):
		return Vec3(
			self.e0 * other, 
			self.e1 * other, 
			self.e2 * other
		)

	def __div__(self, other):
		return Vec3(
			self.e0 / other, 
			self.e1 / other, 
			self.e2 / other
		)

	def squared_length(self):
		return self.e0 * self.e0 + self.e1 * self.e1 + self.e2 * self.e2

	def dot(self, other):
		return self.e0 * other.e0 + self.e1 * other.e1 + self.e2 * other.e2

	def cross(self, other):
		return Vec3(
			self.e1 * other.e2 - self.e2 * other.e1,
			-(self.e0 * other.e2 - self.e2 * other.e0),
			self.e0 * other.e1 - self.e1 * other.e0
		)

	def unit_vector(self):
		return Vec3(
			self.e0 / self.length,
			self.e1 / self.length,
			self.e2 / self.length
		)

	def __str__(self):
		return 'Vec3({}, {}, {})'.format(self.e0, self.e1, self.e2)

