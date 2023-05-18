#include <iostream>
using namespace std;
#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>



struct for_hash
{
    string word;
    for_hash* next = nullptr;
    for_hash* prev = nullptr;
};

for_hash* address;



// N размер массива
// Cоздание пустого множества
for_hash* create(int N) {
    for_hash* hash_table = new for_hash[N];
    return hash_table;
}






// Хеш функция
int hash_function(string word, int N) {
    int sum = 0;
    for (int i = 0; i < word.size(); i++) {
        sum += (int)word[i];
    }
    return sum % N;
}


for_hash* add_element_cepochki(string word, for_hash* hash_table, int N) {
    for_hash* a = &hash_table[hash_function(word, N)];
    while (a->next != nullptr) {
        a = a->next;
    }
    for_hash* new_element = new for_hash;
    new_element->word = word;
    new_element->prev = a;
    a->next = new_element;
    return hash_table;
}

//Проверка множества на пустоту
int proverka(for_hash* hash_table, int N) {
    for (int i = 0; i < N; i++) {
        if (hash_table[i].next != nullptr) {
            cout << "hash_table IS NOT empty" << endl;
            return 0;
        }
    }
    cout << "hash_table IS empty" << endl;
    return 0;
}





for_hash* poisk(string word, for_hash* hash_table, int N) {
    for_hash* ukazatel = hash_table[hash_function(word, N)].next;
    while (ukazatel != nullptr) {
        if (ukazatel->word == word) {
            return ukazatel;
        }
        ukazatel = ukazatel->next;
    }
    return nullptr;
}





bool result_of_poisk(string word, for_hash* hash_table, int N) {
    if (poisk(word, hash_table, N) != nullptr) {
        cout << "There IS element in Hashtable!" << endl;
        return true;
    }
    else {
        cout << "There IS NO element in Hashtable!" << endl;
        return false;
    }

}





int delete_element(string word, for_hash* hash_table, int N) {
    auto ukazatel = poisk(word, hash_table, N);
    if ((ukazatel->prev) != nullptr) {
        (ukazatel->prev)->next = ukazatel->next;
    }
    if ((ukazatel->next) != nullptr) {
        (ukazatel->next)->prev = ukazatel->prev;

    }

    delete ukazatel;
    return 0;
}

int main()
{

    //Для первой части

    int N = 10;
    address = create(N);
    add_element_cepochki("ignat", address, N);
    delete_element("ignat", address, N);

    result_of_poisk("ignat", address, N);
    //proverka(address, N);

}
