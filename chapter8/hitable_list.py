
from hitable import Hitable
from hit_record import Hit_record
from vec3 import Vec3

class Hitable_list(Hitable):
	def __init__(self, hitables):
		self.hitables = hitables

	def hit(self, ray, tmin, tmax, rec):
		hit_anything = False
		closest_hit_so_far = tmax
		tmp_rec = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))

		for hitable in self.hitables:
			if hitable.hit(ray, tmin, closest_hit_so_far, tmp_rec):
				hit_anything = True
				closest_hit_so_far = tmp_rec.t
				rec.t = tmp_rec.t
				rec.p = tmp_rec.p
				rec.normal = tmp_rec.normal
				rec.material = tmp_rec.material

		return hit_anything