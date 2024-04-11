# SHIKHAR UPADHYAY

    """ Question- A, B and C are classes
    A is a super class. B is a sub class of A. C is a sub class of B.
    
    Create three methods in each class, 2 methods are specific to each class and third 
    method (override method) should be in all three Classes A, B and C
    
    Create a class with main method. Create an object for each class A, B and C in main 
    method and call every method of each class using its own object/instance.
    
    Call an overridden method with super class reference to B and C class’s objects
    Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
    process only for data members"""

class A:
    def __init__(self):
        self.data_A1 = "Data A1 - Specific to class A"
        self.data_A2 = "Data A2 - Specific to class A"
        self.data_override = "Data Override - Class A"

    def method_A1(self):
        print(self.data_A1)
    
    def method_A2(self):
        print(self.data_A2)
    
    def override_method(self):
        print(self.data_override)

class B(A):
    def __init__(self):
        super().__init__()
        self.data_B1 = "Data B1 - Specific to class B"
        self.data_B2 = "Data B2 - Specific to class B"
        self.data_override = "Data Override - Class B"

    def method_B1(self):
        print(self.data_B1)
    
    def method_B2(self):
        print(self.data_B2)
    
    def override_method(self):
        print(self.data_override)

class C(B):
    def __init__(self):
        super().__init__()
        self.data_C1 = "Data C1 - Specific to class C"
        self.data_C2 = "Data C2 - Specific to class C"
        self.data_override = "Data Override - Class C"

    def method_C1(self):
        print(self.data_C1)
    
    def method_C2(self):
        print(self.data_C2)
    
    def override_method(self):
        print(self.data_override)

class Main:
    def main(self):
        obj_A = A()
        obj_B = B()
        obj_C = C()

        print("Calling methods of class A:")
        obj_A.method_A1()
        obj_A.method_A2()
        obj_A.override_method()

        print("\nCalling methods of class B:")
        obj_B.method_B1()
        obj_B.method_B2()
        obj_B.override_method()

        print("\nCalling methods of class C:")
        obj_C.method_C1()
        obj_C.method_C2()
        obj_C.override_method()

        print("\nRuntime Polymorphism with Data Members:")
        print("Calling overridden method with superclass reference to B and C class objects:")
        super_ref_B = B()
        super_ref_C = C()

        super_ref_B.override_method()  # Calls B's override_method
        super_ref_C.override_method()  # Calls C's override_method

if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()
