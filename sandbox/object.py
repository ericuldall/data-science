#!/usr/bin/python
class Object:

	def __init__(self, some, thing):
		self.some = some
		self.thing = thing

	def tellMe(self):
		return self.some + self.thing

	def fromClass(self):
		return 'parent'

class Child(Object):

	def __init__(self, some, thing):
		self.some = some
		self.thing = thing

	def fromClass(self):
		return 'child'
	

parent  = Object('test', 'ing')
child 	= Child('test', 'ing')
print (parent.fromClass(), parent.tellMe())
print (child.fromClass(), child.tellMe())
