# Factory/shapefact/ShapeFactory.py
# A simple static factory method.

from __future__ import generators
from helper import *


class Shape(object):
    # Create based on class name:
    def factory(type):
		#return eval(type + "()")
		if type == "rectangle": return Rectangle()
		if type == "line": return Line()
		if type == "ellipse": return Ellipse()
		if type == "polyline": return Polyline()
		if type == "polygon": return Polygon()
		if type == "text": return Text()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)

	def __init__(self):
		"Constructor de Shape"
		self.fill = "white"
		self.stroke = "black"
		self.stroke-width = 1
	
	def toSVG(self):
		" Este método debe ser redefinido. "
		pass
	
	def setParameters(self, kwords**):
		" Este método debe ser redefinido. "
		pass
	
class Rectangle(Shape):

	def __init__(self):
		"Constructor de Rectangle"
		Shape.__init__(self)
		self.upper_left = (0,0)
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")

	
class Line(Shape):

	def __init__(self):
		"Constructor de Line"
		Shape.__init__(self)
		self.from = (0,0)
		self.to = (0,0)
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")

class Circle(Shape):

	def __init__(self):
		"Constructor de Circle"
		Shape.__init__(self)
		self.center = (0,0)
		self.radius = 0
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")
	

class Ellipse(Shape):

	def __init__(self):
		"Constructor de Ellipse"
		Shape.__init__(self)
		self.center = (0,0)
		self.rx = 0
		self.ry = 0
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")

class Polyline(Shape):

	def __init__(self):
		"Constructor de Polyline"
		Shape.__init__(self)
		self.points = []
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")

class Polygon(Shape):

	def __init__(self):
		"Constructor de Polyline"
		Shape.__init__(self)
		self.points = []
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")

class Text(Shape):

	def __init__(self):
		"Constructor de Polyline"
		Shape.__init__(self)
		self.t = ""
		self.at = (0,0)
		
		#opcionales
		self.font-family = ""
		self.font-size = ""
		
    def toSVG(self): print("")
    setParameters(self, kwords**): print("")
	