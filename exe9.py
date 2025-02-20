print("joao henrique")
dir = input("insira a direção que voce deseja contar: baixo:A/a ou cima:C/c")
if dir == "c".lower():
    for i in range(1, int(input("digite um numero superior a 1:"))+1):
        print(i)
elif dir =="A".lower():
    num = int(input("digite um numero abaixo de 20:"))
    if num <=20:
        for i in range(20, num -1, -1):
            print(i)