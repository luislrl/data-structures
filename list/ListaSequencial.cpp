#include <iostream>
#include <stdexcept>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::exception;
using std::runtime_error;
using std::out_of_range;

class ListaSequencial {
private:
    static const int CAPACIDADE = 10;
    int vetor[CAPACIDADE];
    int tamanho;

public:
    ListaSequencial() : tamanho(0) {}

    bool estaVazia() const {
        return (tamanho == 0);
    }

    bool estaCheia() const {
        return (tamanho == CAPACIDADE);
    }

    int obterTamanho() const {
        return tamanho;
    }

    int obterElemento(int pos) const {
        validarPosicao(pos);
        return vetor[pos - 1];
    }

    void modificarElemento(int pos, int novoValor) {
        validarPosicao(pos);
        vetor[pos - 1] = novoValor;
    }

    void inserir(int pos, int valor) {
        if (estaCheia()) {
            throw runtime_error("A lista esta cheia. Nao e possivel inserir.");
        }

        if (pos < 1 || pos > tamanho + 1) {
            throw out_of_range("Posicao de insercao invalida.");
        }

        for (int i = tamanho; i >= pos; i--) {
            vetor[i] = vetor[i - 1];
        }
        vetor[pos - 1] = valor;
        tamanho++;
    }

    void remover(int pos) {
        if (estaVazia()) {
            throw runtime_error("A lista esta vazia. Nao e possivel remover.");
        }

        validarPosicao(pos);

        for (int i = pos; i < tamanho; i++) {
            vetor[i - 1] = vetor[i];
        }
        tamanho--;
    }

private:
    void validarPosicao(int pos) const {
        if (pos < 1 || pos > tamanho) {
            throw out_of_range("Posicao invalida.");
        }
    }
};

int main() {
    ListaSequencial lista;

    cout << "### TESTE 1: Lista vazia ###" << endl;
    cout << "A lista esta vazia? " << (lista.estaVazia() ? "Sim" : "Nao") << endl;
    cout << "Tamanho da lista: " << lista.obterTamanho() << endl << endl;

    cout << "### TESTE 2: Inserindo elementos ###" << endl;
    try {
        lista.inserir(1, 10);
        lista.inserir(2, 20);
        lista.inserir(3, 30);
        lista.inserir(2, 15);
    }
    catch (exception& e) {
        cout << "Erro ao inserir: " << e.what() << endl;
    }

    cout << "Elementos apos insercoes: ";
    for (int i = 1; i <= lista.obterTamanho(); i++) {
        cout << lista.obterElemento(i) << " ";
    }
    cout << endl;

    cout << "\n### TESTE 3: Modificando elemento ###" << endl;
    try {
        lista.modificarElemento(2, 999);
    }
    catch (exception& e) {
        cout << "Erro ao modificar: " << e.what() << endl;
    }
    cout << "Elementos apos modificacao: ";
    for (int i = 1; i <= lista.obterTamanho(); i++) {
        cout << lista.obterElemento(i) << " ";
    }
    cout << endl;

    cout << "\n### TESTE 4: Removendo elemento ###" << endl;
    try {
        lista.remover(2);
    }
    catch (exception& e) {
        cout << "Erro ao remover: " << e.what() << endl;
    }
    cout << "Elementos apos remocao: ";
    for (int i = 1; i <= lista.obterTamanho(); i++) {
        cout << lista.obterElemento(i) << " ";
    }
    cout << endl;

    cout << "\n### TESTE 5: Verificando lista cheia ###" << endl;
    cout << "A lista esta cheia? " << (lista.estaCheia() ? "Sim" : "Nao") << endl;
    try {
        while (!lista.estaCheia()) {
            lista.inserir(lista.obterTamanho() + 1, 999);
        }
    }
    catch (exception& e) {
        cout << "Erro ao inserir: " << e.what() << endl;
    }
    cout << "A lista esta cheia agora? " << (lista.estaCheia() ? "Sim" : "Nao") << endl;
    cout << "Tamanho da lista: " << lista.obterTamanho() << endl;

    cout << "\n### TESTE 6: Tentando inserir em lista cheia ###" << endl;
    try {
        lista.inserir(1, 12345);
    }
    catch (exception& e) {
        cout << "Erro ao inserir em lista cheia: " << e.what() << endl;
    }

    cout << "\nEstado final da lista: ";
    for (int i = 1; i <= lista.obterTamanho(); i++) {
        cout << lista.obterElemento(i) << " ";
    }
    cout << endl;

    return 0;
}
