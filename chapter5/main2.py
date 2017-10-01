
from vec3 import Vec3
from ray import Ray
from math import sqrt
from hit_record import Hit_record
from sphere import Sphere
from hitable_list import Hitable_list

def color(ray, world):
	hit_record = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))
	if world.hit(ray, 0.0, float("inf"), hit_record):
		return Vec3(hit_record.normal.x() + 1, hit_record.normal.y() + 1, hit_record.normal.z() + 1) * 0.5 
	else:
		unit_direction = ray.direction.unit_vector()
		t = 0.5 * (unit_direction.y() + 1.0)
		return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

def main():
	with open("output2.ppm", "w") as f:
		nx, ny = 200, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)
		lower_left_corner = Vec3(-2.0, -1.0, -1.0)
		horizontal = Vec3(4.0, 0.0, 0.0)
		vertical = Vec3(0.0, 2.0, 0.0)
		origin = Vec3(0.0, 0.0, 0.0)

		sphere1 = Sphere(Vec3(0, 0, -1), 0.5)
		sphere2 = Sphere(Vec3(0, -100.5, -1), 100)
		world = Hitable_list([sphere1, sphere2])

		for j in range(ny-1, -1, -1):
			for i in range(0, nx):
				u = float(i) / float(nx)
				v = float(j) / float(ny)
				direction = lower_left_corner + horizontal * u + vertical * v
				ray = Ray(origin, direction)
				col = color(ray, world)
				ir = int(255.99 * col.r())
				ig = int(255.99 * col.g())
				ib = int(255.99 * col.b())
				line = "{} {} {}\n".format(ir, ig, ib)
				f.write(line)
main()










