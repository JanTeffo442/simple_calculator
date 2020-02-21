class Calculator:
    
    def __init__(self):
        pass
    
    def add(self, *args):
        total = 0
        for num in args:
            number = int(num)
            total += number
        return total
    
    def multiply(self, *args):
        product = 1
        for num in args:
            number = int(num)
            product *= number
        return product

            