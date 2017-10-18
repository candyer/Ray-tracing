
from vec3 import Vec3
from ray import Ray
from hit_record import Hit_record
from sphere import Sphere
from hitable_list import Hitable_list
from camera import Camera
from lambertian import Lambertian
from metal2 import Metal

from math import sqrt
from random import random


def color(ray, world, depth):
	rec = Hit_record(t=0, p=Vec3(0, 0, 0), normal=Vec3(0, 0, 0))
	if world.hit(ray, 0.0, float("inf"), rec):
		scattered = Ray(origin=Vec3(0, 0, 0), direction=Vec3(0, 0, 0))
		attenuation = Vec3(1.0, 1.0, 1.0)
		t = rec.material.scatter(ray, rec, attenuation, scattered)
		# print '----', t, t[1]
		if depth < 50 and t[0]:
			return color(scattered, world, depth + 1).mul(t[1])
		else:
			return Vec3(0, 0, 0)
	else:
		unit_direction = ray.direction.unit_vector()
		t = 0.5 * (unit_direction.e1 + 1.0)
		return Vec3(1.0, 1.0, 1.0) * (1 - t) + Vec3(0.5, 0.7, 1.0) * t

def main():
	with open("output2.ppm", "w") as f:
		nx, ny, ns = 200, 100, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)

		camera = Camera()
		sphere1 = Sphere(Vec3(0.0,0.0,-1.0), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3)))
		sphere2 = Sphere(Vec3(0.0, -100.5, -1.0), 100.0, Lambertian(Vec3(0.8, 0.8, 0.0)))
		sphere3 = Sphere(Vec3(1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.6, 0.2), 1.0)) #fuzziness = 1.0
		sphere4 = Sphere(Vec3(-1.0, 0.0, -1.0), 0.5, Metal(Vec3(0.8, 0.8, 0.8), 0.3)) #fuzziness = 0.3

		world = Hitable_list([sphere1, sphere2, sphere3, sphere4])
		for j in range(ny-1, -1, -1):
			for i in range(nx):
				col = Vec3(0.0, 0.0, 0.0)
				for k in range(0, ns):
					u = float(i + random()) / float(nx)
					v = float(j + random()) / float(ny)
					ray = camera.get_ray(u, v)
					col += color(ray, world, 0)

				col /= float(ns)
				col = Vec3(sqrt(col.e0), sqrt(col.e1), sqrt(col.e2))
				ir = int(255.99 * col.r())
				ig = int(255.99 * col.g())
				ib = int(255.99 * col.b())
				line = "{} {} {}\n".format(ir, ig, ib)
				f.write(line)

main()