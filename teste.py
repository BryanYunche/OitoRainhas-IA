import time

def algoritmo_lento():
    soma = 0
    for i in range(10**6):
        soma += i
    return soma

inicio = time.time()
algoritmo_lento()
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")
