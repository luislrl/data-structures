import time
import argparse

# Algoritmos de Ordenação
def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        minInd = i
        for j in range(i + 1, n):
            if arr[j] < arr[minInd]:
                minInd = j
        arr[i], arr[minInd] = arr[minInd], arr[i]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i - 1
        while j >= 0 and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem

# Função para leitura do arquivo .in
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip().split()))

def main():
    # Configurando os argumentos para usar o terminal
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("input_file")
    args = parser.parse_args()

    # Lendo o arquivo
    arr = read_input_file(args.input_file)

    # Medindo o tempo para SelectionSort
    selection_arr = arr.copy()
    startTime = time.time()
    SelectionSort(selection_arr)
    selectionTime = time.time() - startTime

    # Medindo o tempo para InsertionSort
    insertionArr = arr.copy()
    startTime = time.time()
    InsertionSort(insertionArr)
    insertionTime = time.time() - startTime

    # Resultados
    print("Tempo SelectionSort: {:.6f} segundos".format(selectionTime))
    print("Tempo InsertionSort: {:.6f} segundos".format(insertionTime))

if __name__ == "__main__":
    main()
