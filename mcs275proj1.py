"""
methods determinant(),
trace(),
inverse(),
characteristic_polynomial(),
and matrix_product()
#Helpful reference
#lecture30
#lecture28
#project3
"""
class Matrix(object):
    def __init__(self,L):
        self.a = float(L[0][0])
        self.b = float(L[0][1])
        self.c = float(L[1][0])
        self.d = float(L[1][1])

    def __str__(self):
        """
        Matrix
        [a,b]
        [c.d
        """
        return "Matrix\n[%f,%f]\n[%f,%f]" % (self.a,self.b,self.c,self.d)

    def determinant(self):
        return self.a * self.d - self.b *self.c
        #QUESTION do you want us to have an option for if there is no determinant

    def trace(self):
        """
        The trace of a two-by-two matrix is a float
        and it is defined as a+d for the instance A, defined as above.
        """
        return self.a +self.d



    def inverse(self):
        D = self.determinant()
        self.b = (-1)*self.b
        return "Inverse Matrix\n[%f,%f]\n[%f,%f]" % (self.d/D,self.b/D,self.c/D,self.a/D)


    def characteristic_polynomial(self):
        """
        Method call: A.characteristic_polynomial()
        The characteristic polynomial of a two-by-two matrix is a polynomial in an unknown,
        say x, and it is defined as x^2-T*x+D for the instance A, defined as above.
        T stands for the trace and D for the determinant of A.
        You must call the methods determinant() and trace() inside the definition of the method characteristic_polynomial().
        The method characteristic_polynomial() must return a string of the form x^2-T*x+D,
        where T and D have been evaluated to their floating point values.
        X**2 - (Trace * x +Determinant)
        #QUESTION, do you want us to have it as x^2 since we aren't actually squaring anything
        """
        T = self.trace()
        D = self.determinant() #how you call another method


        return "x^2-%f*x+%f" % (T,D)



    def matrix_product(self,other):
        """
        For two instances A and B of the object matrix, defined as
        A = Matrix([[a1,b1],[c1,d1]]) and B = Matrix([[a2,b2],[c2,d2]])
        the method matrix_product() must return a new matrix of the form

		[a1*a2 + b1*c2, a1*b2 + b1*d2]
		[c1*a2 + d1*c2, c1*b2 + d1*d2]

        where a1,b1,c1,d1, and a2,b2,c2,d2 are float entries of the instances A and B.
        """
        return "Matrix Product\n[%f,%f]\n[%f,%f]" % (self.a *other.a + self.b *other.c, self.a *other.b + self.b *other.d,self.c *other.a + self.d *other.c,self.c *other.b + self.d *other.d)








def main():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]]) #a,b,c,d are floats #QUESTION do you care what numbers we use
    print(A)
    print("-------")
    print(A.determinant())
    print("-------")
    print(A.trace())
    print("-------")
    print(A.inverse())
    print("-------")
    print(A.characteristic_polynomial())
    print("-------")
    print(A.matrix_product(B))

main()