obj1 = ["Q", "T", "L", "H", "O"]

obj = input()
cara = input()
dimen = int(input())
j 
 
if obj == obj1[1]: #se for tri^ngulo dimen = altura

    k = int(dimen * 2 - 1) # n° de caracteres na ultima fileira
    a = int(((dimen - 1) * 2 - 1)/2) # espaços 
    b = 1
    for i in range (dimen):
      print (a * " ", cara * b, a * " ")
      a -= 1
      b = b + 2
