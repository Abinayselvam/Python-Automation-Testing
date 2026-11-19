class Employee:
    def display_details(self):
        print("Name: Abinaya")
        print("Role: Software Engineer")


# Creating an object
employee = Employee()

# Calling the method
employee.display_details()


#using contructor
class Student:
    #constructor
    def __init__(self,name,role):
        self.name = name;
        self.role = role;
    def  display_details(self):
        print("Name:",self.name);
        print("RoleNo:",self.role);

student1 = Student("Abinaya","RA1001");
student2 =Student("Sinch","RA10002");
student1.display_details();
student2.display_details();