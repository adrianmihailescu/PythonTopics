class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def subtract(cls, x, y):
        return x - y

print(Math.add(5, 3))
print(Math.subtract(10, 3))
