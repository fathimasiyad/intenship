# class Age:
#     x=10
# p1=Age()
# print(p1.x)    
#
# class Employee:
#     name="fathima"
#     age=18
# obj=Employee()
# print(obj.name)
# print(obj.age)
#constructors
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj=Person("Fathima",18)
# print(obj.name)
# class Student:
#     def __init__(self,subject,mark):
#         self.subject=subject
#         self.mark=mark
# p1=Student("science",48)
# print(p1.subject)
# print(p1.mark)    
#                    inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# d1=Dog ("jack")
# print(d1.name)
# print(d1.make_sound())      
#                                 single inheritance   
# class Brands:
#     brand_name_1="Amazon"
#     brand_name_2="Ebay"
#     brand_name_3="OLX"
# class Products(Brands):
#     prod_1="Online Ecommerce Store"
#     prod_2="Online Store"
#     prod_3="Online By Sell Store"
# obj_1=Products()
# print(obj_1.brand_name_1+ " is an " +obj_1.prod_1)   
# print(obj_1.brand_name_2+ " is an " +obj_1.prod_2)
# print(obj_1.brand_name_3+ " is an " +obj_1.prod_3)
#                                  multiple
# class Brands:
#     brand_name_1="Amazon"
#     brand_name_2="Ebay"
#     brand_name_3="OLX"
# class Products:
#     prod_1="Online Ecommerce Store"
#     prod_2="Online Store"
#     prod_3="Online By Sell Store"
# class Popularity(Brands,Products):
#     prod_1_popularity=100
#     prod_2_popularity=70
#     prod_3_popularity=60
# obj_1=Popularity()
# print(obj_1.brand_name_1+ " is an " +obj_1.prod_1+" is ",obj_1.prod_1_popularity)
# print(obj_1.brand_name_2+ " is an " +obj_1.prod_2+" is ",obj_1.prod_2_popularity)
# print(obj_1.brand_name_3+ " is an " +obj_1.prod_3+" is ",obj_1.prod_3_popularity)


        