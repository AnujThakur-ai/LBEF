class calculator():
    def add(self, *numbers):
        return sum(numbers)


    def sub(self, *numbers):
        if not numbers:
            return  0
        result = numbers[0]
        for n in numbers[1:]:
            result -=n

        return result

    def mul(self, *numbers):
        if not numbers:
            return 0

        result = numbers[0]
        for n in numbers[1:]:
            result *= n

        return result


    def div(self,a,b):
        return a/b

    def a_rec(self, l, b):
        return l*b

    def p_rec(self, l, b):
        return 2*(l+b)

    def a_sq(self, l):
        return l**2

    def p_sq(self, l):
        return 4*l

    def a_cir(self, r):
        PIE = 22/7
        return PIE * r **2

    def p_cir(self, r):
        PIE = 22/ 7
        return  2* PIE * r

    def a_para(self, b, h):
        return b*h

    def p_para(self, b, s):
        return 2*(b *s)

    def a_trap(self, h, b1, b2):
        return 0.5*h*(b1+b2)

    def p_trap(self, s1,s2, b1, b2):
        return s1+s2+b1+b2

