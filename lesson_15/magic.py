class A:

    def __init__(self):
        self.value = 10

    def __add__(self, other):
        return "Выполняется метод __add__"

    def __radd__(self, other):
        return "Выполняется метод __radd__"
    
    def __iadd__(self, other):
        self.value += other
        return self
    
    def __str__(self):
        return f"value: {self.value}"
    
a = A()
print(a+1)
print(1+a)
a+=1
print(a)
