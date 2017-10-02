
from hitable import Hitable
from math import sqrt

class Sphere(Hitable):

	def __init__(self, cen, r):
		self.cen = cen
		self.r = r

	def hit(self, ray, tmin, tmax, hit_record):
		oc = ray.origin - self.cen
		a = ray.direction.dot(ray.direction)
		b = oc.dot(ray.direction)
		c = oc.dot(oc) - self.r * self.r		
		discriminant = b * b - a * c
		if discriminant > 0:
			temp = (-b - sqrt(b * b - a * c)) / a
			if tmin < temp < tmax:
				hit_record.t = temp
				hit_record.p = ray.point_at_parameter(hit_record.t)
				hit_record.normal = (hit_record.p - self.cen) / self.r
				return True
		return False