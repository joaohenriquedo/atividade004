dir = input("insira a direção que voce deseja contar: baixo:A/a ou cima:C/c")
if dir == "c".lower():
    num = int(input("digite um numero superior a 1:"))
    print("contando pra cima:")
    for i in range(1, num, +1  ):
        print(i)
if dir in"a".lower():
    num =  input("insira um numero menor que 20:")
    print("contando pra baixo:")
    for i in range(20, num -1, -1):
            print(i)
else:
    print("direção invalida")
    print("joão henrique")

 