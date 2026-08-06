from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str= "Ram"    #default value
    age:Optional[int]= None
    email:EmailStr
    cgpa :float = Field(gt=0,lt=10) 
new_student = {'age':'24','email':'abc@gmail.com','cgpa':5} # pydantic automatically done type casting and it automatically validate email

student = Student(**new_student)

print(student)