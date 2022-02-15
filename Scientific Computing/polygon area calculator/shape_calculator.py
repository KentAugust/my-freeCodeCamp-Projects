class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	
	def set_width(self, width):
		self.width = width
	
	def set_height(self, height):
		self.height = height
	
	def get_area(self):
		self.area = self.width * self.height
		return self.area
	
	def get_perimeter(self):
		self.perimeter = self.width*2 + self.height*2
		return self.perimeter
	
	def get_diagonal(self):
		self.diagonal = (self.width**2 + self.height**2)** 0.5
		return self.diagonal
	
	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture."
		self.figure = ""
		for row in range(round(self.height)):
			self.figure += "*"*round(self.width) + "\n"
		return self.figure
	
	def get_amount_inside(self, obj):
		
		inside = self.get_area() / obj.get_area()
		return int(inside)
	
	def __repr__(self):
		self.info = f'Rectangle(width={self.width}, height={self.height})'
		return self.info

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)
	
	def set_side(self, side):
		self.width = side
		self.height = side
	
	def set_width(self, width):
		self.set_side(width)
	
	def set_height(self, height):
		self.set_side(height)
	
	def __repr__(self):
		self.info = f'Square(side={self.width})'
		return self.info