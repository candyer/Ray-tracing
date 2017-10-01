
from hitable import Hitable
from hit_record import Hit_record
from vec3 import Vec3

class Hitable_list(Hitable):
	def __init__(self, hitables):
		self.hitables = hitables

	def hit(self, ray, tmin, tmax, hit_record):
		hit_anything = False
		closest_so_far = tmax
		temp_rec = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))
		for hitable in self.hitables:
			if hitable.hit(ray, tmin, closest_so_far, temp_rec):
				hit_anything = True
				closest_so_far = temp_rec.t
				hit_record.t = temp_rec.t
				hit_record.p = temp_rec.p
				hit_record.normal = temp_rec.normal
		return hit_anything