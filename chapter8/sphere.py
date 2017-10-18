from hitable import Hitable

from math import sqrt

class Sphere(Hitable):

	def __init__(self, center, radius, material):
		self.center = center
		self.radius = radius
		self.material = material

	def hit(self, ray, tmin, tmax, rec):
		oc = ray.origin - self.center
		a = ray.direction.dot(ray.direction)
		b = oc.dot(ray.direction)
		c = oc.dot(oc) - self.radius * self.radius

		discriminant = b * b - a * c
		if discriminant > 0:
			temp = (-b - sqrt(discriminant)) / a
			if tmin < temp < tmax:
				rec.t = temp
				rec.p = ray.point_at_parameter(rec.t)
				rec.normal = (rec.p - self.center) / self.radius
				rec.material = self.material
				return True
		else:
			return False