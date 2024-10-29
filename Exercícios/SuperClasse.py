class MinhaString(str):
    def upper(self):
        print ('Chamou a função upper')
        return super().upper()
    
string = MinhaString('oi')
print(string.upper()) #ABC

class A:
    atributo_1 = 'Atributo 1'
    def metodo(self):
        print('Classe A')

class B(A):
    atributo_2 = 'Atributo 2'
    def metodo(self):
        print('Classe B')

class C(B):
    atributo_3 = 'Atributo 3'
    def metodo(self):
        super().metodo()
        super(B, self).metodo()
        print('Classe C')

c = C()
print(c.atributo_1) 
print(c.atributo_2)
print(c.atributo_3)
c.metodo()

print(C.mro()) #Method Resolution Order
print(C.__mro__) #Method Resolution Order
print(B.mro()) #Method Resolution Order