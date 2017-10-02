
from math import sqrt
from random import random

from vec3 import Vec3
from ray import Ray
from hit_record import Hit_record
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera


def color(ray, world):
	hit_record = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))
	if world.hit(ray, 0.0, float("inf"), hit_record):
		return Vec3(hit_record.normal.x() + 1, hit_record.normal.y() + 1, hit_record.normal.z() + 1) * 0.5 
	else:
		unit_direction = ray.direction.unit_vector()
		t = 0.5 * (unit_direction.y() + 1.0)
		return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

def main():
	with open("output.ppm", "w") as f:
		nx, ny, ns = 200, 100, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)

		sphere1 = Sphere(Vec3(0, 0, -1), 0.5)
		sphere2 = Sphere(Vec3(0, -100.5, -1), 100)
		world = Hitable_list([sphere1, sphere2])

		for j in range(ny-1, -1, -1):
			for i in range(0, nx):

				col = Vec3(0, 0, 0)
				for s in range(ns):
					u = float(i + random()) / float(nx)
					v = float(j + random()) / float(ny)
					ray = Camera().get_ray(u, v)
					# p = ray.point_at_parameter(2.0)
					col += color(ray, world)

				col /= ns
				ir = int(255.99 * col.r())
				ig = int(255.99 * col.g())
				ib = int(255.99 * col.b())
				line = "{} {} {}\n".format(ir, ig, ib)
				f.write(line)
main()










