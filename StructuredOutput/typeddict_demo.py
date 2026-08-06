from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person :Person ={'name':'Manish','age':24} #it only tells what type should of value it doesnot give error if we wrong define .like age  is int 24 but if we define age str '24' then it doesnot give error.

print(new_person)