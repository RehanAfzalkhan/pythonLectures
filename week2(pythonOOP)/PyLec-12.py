# OOP
# pascal case  every word 1s letter should be capital
# class Product:
#     brand=


# p1 = Product()  # create an instance p1 of class.here p1 is a reference variable
class Enroll:
    # courses = []

    def __init__(self, name) -> None:
        self.name = name
        self.course = []

    def add_course(self, course_name):
        self.course.append(course_name)

anas = Enroll(name="anas ahmed")``
anas.add_course("NLP")
anas.add_course("Cyber")
jalil = Enroll(name="Muhammad jalil")

print(f"course of  {jalil.name}: {jalil.course}")
print(f"courses of {anas.name} : {anas.course}")
