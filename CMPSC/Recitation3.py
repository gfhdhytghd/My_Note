class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i**2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
    def __str__(self):
        """Display Complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"    # This is a string representation of the Complex object, not a Complex object
        else:
           return f"{self._real} - {abs(self._imag)}i"
    __repr__ = __str__

    def conjugate(self):
        """Returns a Complex object that represents the Complex conjugate"""
        return Complex(self._real, -self._imag)
    def __mul__(self,other):
        """Multiply two Complex numbers"""
        
        if isinstance(other, Complex) and isinstance(self, Complex):
            real_part = self._real*other._real-self._imag*other._imag    # Value for the real part
            imag_part = self._real*other._imag+self._imag*other._real   # Value for the imaginary part
        elif isinstance(other, int|float) and isinstance(self, Complex):
            real_part = self._real*other    # Value for the real part
            imag_part = self._imag*other   # Value for the imaginary part
        ans = Complex(real_part,imag_part) 
        return ans
    def __rmul__(self,other):
        """Multiply a real and Complex number""" 
        return self*other
