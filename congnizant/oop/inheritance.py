# ------------------------
# 1. SINGLE INHERITANCE
# ------------------------
class Parent:
    def show_parent(self):
        print("Single: This is the Parent class")

class Child(Parent):
    def show_child(self):
        print("Single: This is the Child class")

single = Child()
single.show_parent()
single.show_child()

print("-" * 40)

# ------------------------
# 2. MULTIPLE INHERITANCE
# ------------------------
class Father:
    def skill_father(self):
        print("Multiple: Father can drive")

class Mother:
    def skill_mother(self):
        print("Multiple: Mother can cook")

class Kid(Father, Mother):
    def skill_kid(self):
        print("Multiple: Kid can code")

multiple = Kid()
multiple.skill_father()
multiple.skill_mother()
multiple.skill_kid()

print("-" * 40)

# ------------------------
# 3. MULTILEVEL INHERITANCE
# ------------------------
class Grandparent:
    def show_gp(self):
        print("Multilevel: Grandparent class")

class Parent2(Grandparent):
    def show_parent(self):
        print("Multilevel: Parent class")

class Child2(Parent2):
    def show_child(self):
        print("Multilevel: Child class")

multilevel = Child2()
multilevel.show_gp()
multilevel.show_parent()
multilevel.show_child()

print("-" * 40)

# ------------------------
# 4. HIERARCHICAL INHERITANCE
# ------------------------
class Parent3:
    def show_parent(self):
        print("Hierarchical: Parent class")

class Child3a(Parent3):
    def show_child1(self):
        print("Hierarchical: Child 1 class")

class Child3b(Parent3):
    def show_child2(self):
        print("Hierarchical: Child 2 class")

hier1 = Child3a()
hier2 = Child3b()
hier1.show_parent()
hier1.show_child1()
hier2.show_parent()
hier2.show_child2()

print("-" * 40)

# ------------------------
# 5. HYBRID INHERITANCE (Multiple + Multilevel)
# ------------------------
class A:
    def show_A(self):
        print("Hybrid: Class A")

class B(A):
    def show_B(self):
        print("Hybrid: Class B")

class C(A):
    def show_C(self):
        print("Hybrid: Class C")

class D(B, C):  # Multiple + Multilevel
    def show_D(self):
        print("Hybrid: Class D")

hybrid = D()
hybrid.show_A()
hybrid.show_B()
hybrid.show_C()
hybrid.show_D()
