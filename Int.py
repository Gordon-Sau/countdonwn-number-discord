class Int(int):
    def __truediv__(self, x):
        if ((self % x) == 0):
            return Int(self // x)
        raise ValueError(f"{self} is not divisible by {x}")
    def __rtruediv__(self, x):
        if ((x % self) == 0):
            return Int(x // self)
        raise ValueError(f"{x} is not divisible by {self}")
