numero = int(input())
Lista = list(map(int, input().split()))
soma  = 0

for i in range(0, numero):
    soma += int(Lista[i])

print(soma)



