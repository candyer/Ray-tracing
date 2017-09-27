
from math import sqrt
class Vec3:
	def __init__(self, e0, e1, e2):
		self.e = [float(e0), float(e1), float(e2)]
		self.length = sqrt(self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2])

	def x(self): return self.e[0]
	def y(self): return self.e[1]
	def z(self): return self.e[2]
	def r(self): return self.e[0]
	def g(self): return self.e[1]
	def b(self): return self.e[2]

	def __eq__(self, a):
	 	return self.e[0] == a.e[0] and self.e[1] == a.e[1] and self.e[2] == a.e[2]

	def __neg__(self):
		return Vec3(-self.e[0], -self.e[1], -self.e[2])

	def __pos__(self):
		return self

	def __add__(self, other):
		return Vec3(
			self.e[0] + other.e[0], 
			self.e[1] + other.e[1], 
			self.e[2] + other.e[2]
		)

	def __sub__(self, other):
		return Vec3(
			self.e[0] - other.e[0], 
			self.e[1] - other.e[1], 
			self.e[2] - other.e[2]
		)

	def __mul__(self, other):
		return Vec3(
			self.e[0] * other.e[0], 
			self.e[1] * other.e[1], 
			self.e[2] * other.e[2]
		)

	def __div__(self, other):
		return Vec3(
			self.e[0] / other.e[0], 
			self.e[1] / other.e[1], 
			self.e[2] / other.e[2]
		)

	def squared_length(self):
		return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

	def dot(self, other):
		return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

	def cross(self, other):
		return Vec3(
			self.e[1] * other.e[2] - self.e[2] * other.e[1],
			-(self.e[0] * other.e[2] - self.e[2] * other.e[0]),
			self.e[0] * other.e[1] - self.e[1] * other.e[0]
		)

	def unit_vector(self):
		return Vec3(
			self.e[0] / self.length,
			self.e[1] / self.length,
			self.e[2] / self.length
		)

	def __str__(self):
		return 'Vec3({}, {}, {})'.format(*self.e)


def generate_gradient():
	with open("output.ppm", "w") as f:
		nx, ny = 200, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)
		for j in range(ny - 1, -1, -1):
			for i in range(nx):
				vec = Vec3(i / float(nx), j / float(ny), 0.2) 
				ir = int(255.99 * vec.r())
				ig = int(255.99 * vec.g())
				ib = int(255.99 * vec.b())
				line = "{} {} {}\n".format(ir,ig,ib)
				f.write(line)

generate_gradient()

