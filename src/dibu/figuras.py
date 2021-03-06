#!/usr/bin/env python

import os
display_prog = "display"

class Scene:
    def __init__(self,name="svg",height=200,width=200):
        self.name = name
        self.items = []
        self.height = height
        self.width = width
        return

    def nombre(self, name):
        self.name = name

    def heightAndWidth(self, height, width):
        self.height = height
        self.width = width

    def add(self,item): self.items.append(item)

    def strarray(self):
        var = ["<?xml version=\"1.0\"?>\n",
               "<svg height=\"%d\" width=\"%d\" >\n" % (self.height,self.width),
               " <g style=\"fill-opacity:1.0; stroke:black;\n",
               "  stroke-width:1;\">\n"]
        for item in self.items: var += item.strarray()
        var += [" </g>\n</svg>\n"]
        return var

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name + ".svg"
        file = open(self.svgname,'w')
        file.writelines(self.strarray())
        file.close()
        return

    def display(self,prog=display_prog):
        os.system("%s %s" % (prog,self.svgname))
        return

class Line:
    def __init__(self,start=(0,0),end=(10,10),fill_color='black',line_color='none',line_width=1):
        self.start = start
        self.end = end
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        return

    def from_(self, start):
        self.start = start

    def to(self, end):
        self.end = end

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        return ["  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" style=\"fill:%s;stroke:%s;stroke-width:%d\"/>\n" %\
                (self.start[0],self.start[1],self.end[0],self.end[1],self.fill_color, self.line_color,self.line_width)]

class Circle:
    def __init__(self,center=(100,100),radius=40,fill_color='black',line_color='none',line_width=1):
        self.centro = center
        self.radio = radius
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        return

    def center(self, center):
        self.centro = center

    def radius(self, radius):
        self.radio = radius

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        return ["  <circle cx=\"%d\" cy=\"%d\" r=\"%d\"\n" %\
                (self.centro[0],self.centro[1],self.radio),
                "    style=\"fill:%s;stroke:%s;stroke-width:%d\"  />\n" % (self.fill_color, self.line_color,self.line_width)]

class Ellipse:
    def __init__(self,center=(100,100),radius_x=20,radius_y=30,fill_color='black',line_color='none',line_width=1):
        self.centro = center
        self.radiusx = radius_x
        self.radiusy = radius_y
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width

    def center(self, center):
        self.centro = center

    def rx(self, radius_x):
        self.radiusx = radius_x

    def ry(self, radius_y):
        self.radiusy = radius_y

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        return ["  <ellipse cx=\"%d\" cy=\"%d\" rx=\"%d\" ry=\"%d\"\n" %\
                (self.centro[0],self.centro[1],self.radiusx,self.radiusy),
                "    style=\"fill:%s;stroke:%s;stroke-width:%d\"/>\n" % (self.fill_color, self.line_color ,self.line_width)]

class Polygon:
    def __init__(self,points=[(100,100)],fill_color='black',line_color='none',line_width=1):
        self.puntos = points
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width

    def points(self, points):
        self.puntos = points

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        polygon="<polygon points=\""
        for point in self.puntos:
            polygon+=" %d,%d" % (point[0],point[1])
        return [polygon,\
               "\" \nstyle=\"fill:%s;stroke:%s;stroke-width:%d\"/>\n" %\
               (self.fill_color, self.line_color, self.line_width)]
class Polyline:
    def __init__(self,points=[(100,100)],fill_color='black',line_color='none',line_width=1):
        self.puntos = points
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width

    def points(self, points):
        self.puntos = points

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        polyline="<polyline points=\""
        for point in self.puntos:
            polyline+=" %d,%d" % (point[0],point[1])
        return [polyline,\
               "\" \nstyle=\"fill:%s;stroke:%s;stroke-width:%d\"/>\n" %\
               (self.fill_color, self.line_color, self.line_width)]

class Rectangle:
    def __init__(self,origin=(100,100),size=(200,200),fill_color='black',line_color='none',line_width=1):
        self.origin = origin
        self.height = size[0]
        self.width = size[1]
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        return

    def upper_left(self, origin):
        self.origin = origin

    def size(self, size):
        self.height = size[0]
        self.width = size[1]

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        return ["  <rect x=\"%d\" y=\"%d\" height=\"%d\"\n" %\
                (self.origin[0],self.origin[1],self.height),
                "    width=\"%d\" style=\"fill:%s;stroke:%s;stroke-width:%d\" />\n" %\
                (self.width, self.fill_color, self.line_color ,self.line_width)]


class Text:
    def __init__(self, origin=(100,100), text=' ', font='Arial',size="medium", fill_color='black', line_color='none',line_width=1):
        self.origin = origin
        self.text = text
        self.font = font
        self.size = size
        self.fill_color = fill_color
        self.line_color = line_color
        self.line_width = line_width
        return

    def t(self, text):
        self.text = text

    def at(self, origin):
        self.origin = origin

    def font_family(self, font):
        self.font = font

    def font_size(self, size):
        self.size = size

    def fill(self, fill_color):
        self.fill_color = fill_color

    def stroke(self, line_color):
        self.line_color = line_color

    def stroke_width(self, line_width):
        self.line_width = line_width

    def strarray(self):
        return ["  <text x=\"%d\" y=\"%d\" font-family=\"%s\" font-size=\"%s\" fill=\"%s\" stroke=\"%s\" stroke-width=\"%d\" >\n" %\
                (self.origin[0],self.origin[1],self.font, self.size, self.fill_color, self.line_color ,self.line_width),
                "   %s\n" % self.text,
                "  </text>\n"]
