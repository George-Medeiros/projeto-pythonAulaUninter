import numpy as np

def main():
    valores = np.array([1, 2, 3, 4, 5])
    print("Valores:", valores)
    soma = np.sum(valores)
    print("Soma:", soma)
    return soma

if __name__ == "__main__":
    soma_total = main()
    print("Soma total:", soma_total)

