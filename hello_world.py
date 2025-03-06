print("Hello, World!")

class NumberProcessor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        
# Beispielverwendung
processor = NumberProcessor(10, 5)
print("Addition:", processor.add())
print("Subtraktion:", processor.subtract())
print("Multiplikation:", processor.multiply())
print("Division:", processor.divide())