#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Objeto {
    int chave;
    string dado;
};

class DoubleHashTable {
    static const int PRIMEIRO_NIVEL = 10;
    static const int PRIMO_HASH = 31;

    size_t segundoNivelTamanho;
    vector<vector<vector<Objeto>>> tabela;

    int h1(int chave) const {
        return chave % PRIMEIRO_NIVEL;
    }

    int h2(int chave) const {
        long long mix = (static_cast<long long>(chave) * PRIMO_HASH);
        return static_cast<int>(mix % static_cast<long long>(segundoNivelTamanho));
    }

public:
    DoubleHashTable(size_t n) {
        segundoNivelTamanho = (n + PRIMEIRO_NIVEL - 1) / PRIMEIRO_NIVEL;
        tabela.resize(PRIMEIRO_NIVEL,
            vector<vector<Objeto>>(segundoNivelTamanho));
    }

    bool inserir(int chave, const string& dado) {
        int i = h1(chave);
        int j = h2(chave);
        vector<Objeto>& lista = tabela[i][j];

        for (size_t k = 0; k < lista.size(); ++k)
            if (lista[k].chave == chave) return false;

        lista.push_back(Objeto{ chave, dado });
        return true;
    }

    bool recuperar(int chave, string& resultado) const {
        int i = h1(chave);
        int j = h2(chave);
        const vector<Objeto>& lista = tabela[i][j];

        for (size_t k = 0; k < lista.size(); ++k) {
            if (lista[k].chave == chave) {
                resultado = lista[k].dado;
                return true;
            }
        }
        return false;
    }
};

int main() {
    DoubleHashTable ht(100);

    ht.inserir(123, "João");
    ht.inserir(77, "Maria");
    ht.inserir(205, "Ana");

    string valor;
    if (ht.recuperar(77, valor))
        cout << "Chave 77 ? " << valor << '\n';
    else
        cout << "Chave não encontrada\n";

    return 0;
}
