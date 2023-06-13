#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

b1 = BaseModel()
print(b1)
u1 = User()
print(u1)
a1 = Amenity()
print(a1)
c1 = City()
print(c1)
p1 = Place()
print(p1)
r1 = Review()
print(r1)
s1 = State()
print(s1)

