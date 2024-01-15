class Calculator:
    sum =0
    def __init__(self,x,operators,y):
        self.x = x
        self.operators = operators
        self.y = y
        
    def Calculatorq(self):
        if self.operators == '+':
            return self.x + self.y
        
        elif self.operators == '-':
            return self.x - self.y

        elif self.operators == '*':
            return self.x * self.y 

        elif self.operators == '/':
            return self.x / self.y
        
        elif self.operators == '**':
            return pow(self.x , self.y)


        else:
            pass

print("If you want to calculate a power then choose the number.","\n"," Then and click'**' And then the attachment you want ")       
x = Calculator(int(input("Enter the first number: ")),input("Enter your account action: "),int(input("Enter the second number: ")))
print(x.Calculatorq())