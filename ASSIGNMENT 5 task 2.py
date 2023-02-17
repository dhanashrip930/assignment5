#Challenge 2: Implement a Calculator Class
class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2 
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num2/self.num1
num1= float(input("Enter the num1:"))
num2= float(input("Enter the num2:"))
obj_calculator = calculator(num1,num2)
sum = obj_calculator.add()
sub1 = obj_calculator.sub()
mul1 = obj_calculator.mul()
div1 = obj_calculator.div()
print(f"{int(sum)} \n{int(sub1)} \n{int(mul1)} \n{div1}")       