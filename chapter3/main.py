
from vec3 import Vec3
from ray import Ray

def color(ray):
	unit_direction = ray.direction.unit_vector()
	t = 0.5 * (unit_direction.e[1] + 1.0) 
	return Vec3(1.0, 1.0, 1.0) * Vec3(1 - t, 1 - t, 1 - t) + Vec3(0.5, 0.7, 1.0) * Vec3(t, t, t)

def main():
	with open("output.ppm", "w") as f:
		nx, ny = 200, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)

		lower_left_corner = Vec3(-2.0, -1.0, -1.0)
		horizontal = Vec3(4.0, 0.0, 0.0)
		vertical = Vec3(0.0, 2.0, 0.0)
		origin = Vec3(0.0, 0.0, 0.0)
		for j in range(ny - 1, -1, -1):
			for i in range(nx):
				u = i / float(nx)
				v = j / float(ny)
				direction = lower_left_corner + Vec3(u, u, u) * horizontal + Vec3(v, v, v) * vertical
				ray = Ray(origin, direction)
				col = color(ray)
				ir = int(255.99 * col.r())
				ig = int(255.99 * col.g())
				ib = int(255.99 * col.b())
				line = "{} {} {}\n".format(ir,ig,ib)
				f.write(line)

main()

