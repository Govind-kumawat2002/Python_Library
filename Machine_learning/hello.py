# class animal:
#     name = 'govind'
#     age = 18
#     weight = 80
#     def display(self):
#         print(self.name)
# animal_name = animal()
# print(animal_name.name)

# animal_obj = animal()
# print(animal_obj.weight)
  # class = blueprint 

# class  Animal:

#     # class variable 
#     name = 'eleaphant'
#     weight = 2000 
#     age = 25

#     # function vs method 
#     def display(self):
#         print(self.weight)





# animal_objects1 = Animal()
# animal_objects2 = Animal()


# animal_objects1.name = "python"
# print(animal_objects1.name)

# print(animal_objects2.name)

# class animal:
#     num1 = 100
#     num2 = 200
#     def __init__(self,name,weight,age):
#         #instance variable

#         self.animal_name = name 
#         self.animal_weight = weight
#         self.animal_age = age 
#             # function vs method 
#     def display(self):
#         print(self.animal_name)
#         print(self.animal_age)
#         print(self.animal_weight)
# obj = animal(name= 'cutiya',weight=800,age=1)
# obj2= animal('govind',200,12)
# obj2.display()
# obj.display()

class laptop:
    brand = 'victus'
    price = 2
@classmethod
def class_method(cls):
    print(cls.brand)
    print(cls.price)
obj1 =laptop()
print(obj1.brand)
print(obj1.price)

@staticmethod
def hello():
    print("hello")
hello()


       


