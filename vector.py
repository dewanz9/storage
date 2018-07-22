import math


class Vector(object):
	"""a 3d vector class"""
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def from_points(self, point1, point2):
		"""creates the vector from two points"""
		self.x = point2[0] - point1[0]
		self.y = point2[1] - point1[1]
		self.z = point2[2] - point1[2]

	def get_magnitude(self):
		"""returns the magnitude of the vector"""
		mag = math.sqrt(self.x**2+self.y**2+self.z**2)
		return mag

	def get_direction(self):
		"""returns the direction clockwise from positive z"""
		angle_rads_x_axis = math.atan2(self.z, self.x)
		angle_degrees = math.degrees(angle_rads_x_axis)
		return (angle_degrees*-1)+90

	def from_direc_mag(self, direction, magnitude):
		"""sets the vector with a given direction and magnitude"""
		direction = math.radians(direction)
		if 0 <= direction and direction < math.pi/2:
			x = magnitude * math.sin(direction)
			z = magnitude * math.cos(direction)
		elif math.pi/2 <= direction and direction < math.pi:
			x = magnitude * math.cos(direction-math.pi/2)
			z = magnitude * math.sin(direction-math.pi/2)
		elif math.pi <= direction and direction < (math.pi*3)/4:
			x = magnitude * math.sin(direction-math.pi)
			z = magnitude * math.cos(direction-math.pi)
		else:
			x = magnitude * math.cos(direction-(math.pi*3)/4)
			z = magnitude * math.sin(direction-(math.pi*3)/4)

		self.x = x
		self.z = z

	def add(self, vector):
		"""adds two vectors and returns the result"""
		x = self.x + vector.x
		y = self.y + vector.y
		z = self.z + vector.z
		temp = Vector()
		temp.x,temp.y,temp.z = x,y,z
		return temp