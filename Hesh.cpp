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

//Проверка множества на пустату
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
// Реализация дерева

struct tree {
    int key;
    string word;
    tree* from_tree = nullptr;



    tree* right = nullptr;
    tree* left = nullptr;

};
//size of tree
int N2 = 25;
tree* koren = new tree{ hash_function("KOREN", N2), "KOREN" };


int add_node(tree* head, string word, int key = -1) {
    if (key == -1) {
        key = hash_function(word, N2);
    }

    if (key > head->key) {
        if (head->right == nullptr) {
            head->right = new tree{ key, word };
            return 0;
        }
        head = head->right;
    }
    if (key < head->key) {
        if (head->left == nullptr) {
            head->left = new tree{ key, word };
            return 0;
        }
        head = head->left;
    }
    else {
        while (head->from_tree != nullptr) {
            head = head->from_tree;
        }
        head->from_tree = new tree{ key, word };
        return 0;
    }
    add_node(head, word, key);
}
bool tree_find_node(tree* head, string word, int key = -1) {
    if (key == -1) {
        key = hash_function(word, N2);
    }

    if (key == head->key) {
        while (head != nullptr) {
            if (head->word == word) {

                return true;
            }
            head = head->from_tree;
        }

        return false;
    }
    if (key > head->key) {
        if (head->right == nullptr) {
            return false;
        }
        head = head->right;
    }
    if (key < head->key) {
        if (head->left == nullptr) {
            return false;
        }
        head = head->left;
    }

    tree_find_node(head, word, key);
}

int result_of_tree_find_node(tree* head, string word) {
    if (tree_find_node(head, word)) {
        cout << "There is your Node " << word << endl;
    }
    else {
        cout << "There is NO your Node( " << word << endl;
    }
    return 0;
}
int trudniy_sluchai(tree* previous_node, tree* node, int a) {
    if (a != 1 || a != 0) {
        cout << "ERROR" << endl;
        return 10000;
    }
    node = node->left;
    while (true) {
        if (node->right == nullptr) {
            if (a == 1) {
                node->right = (previous_node->right)->right;
                node->left = (previous_node->right)->left;
                delete previous_node->right;
                previous_node->right = node;
            }
            else {
                node->right = (previous_node->left)->right;
                node->left = (previous_node->left)->left;
                delete previous_node->left;
                previous_node->left = node;
            }
        }
        node = node->right;
    }
    return 0;
}
int* tree_node_delete(tree* head, string word, int key = -1) {
    if (key == -1) {
        key = hash_function(word, N2);
    }

    if (tree_find_node(head, word)) {
        if (key > head->key) {
            /////
            if ((head->right)->key == key) {
                tree* previous_node = head; head = head->right;
                if (head->from_tree == nullptr) {

                    if ((head->right == nullptr) and (head->left != nullptr)) {
                        previous_node->right = head->left; delete head;
                        return 0;
                    }


                    else if ((head->right != nullptr) and (head->left == nullptr))
                    {
                        previous_node->right = head->right; delete head;
                        return 0;
                    }


                    else if ((head->right != nullptr) and (head->left != nullptr)) {
                        trudniy_sluchai(previous_node, head, 1);
                    }

                    else if ((head->right == nullptr) and (head->left == nullptr)) {
                        delete head; head = nullptr;
                        previous_node->right = nullptr;
                        return 0;
                    }

                }


                else {
                    if (head->word == word) {
                        head->from_tree->right = head->right; head->from_tree->left = head->left;
                        previous_node->right = head->from_tree;
                        delete head; return 0;
                    }
                    while (head->from_tree->word != word) {
                        head = head->from_tree;
                    }
                    auto deletenode = head->from_tree;
                    head->from_tree = deletenode->from_tree;
                    delete deletenode;
                }
            }

            else {
                head = head->right;
            }
        }


        if (key < head->key) {
            /////
            if ((head->left)->key == key) {
                tree* previous_node = head; head = head->left;
                if (head->from_tree == nullptr) {

                    if ((head->right == nullptr) and (head->left != nullptr)) {
                        previous_node->left = head->left; delete head;
                        return 0;
                    }


                    else if ((head->right != nullptr) and (head->left == nullptr))
                    {
                        previous_node->left = head->right; delete head;
                        return 0;
                    }


                    else if ((head->right != nullptr) and (head->left != nullptr)) {
                        trudniy_sluchai(previous_node, head, 0);
                    }

                    else if ((head->right == nullptr) and (head->left == nullptr)) {
                        delete head; head = nullptr;
                        previous_node->left = nullptr;
                        return 0;

                    }
                }

                else {
                    if (head->word == word) {
                        head->from_tree->right = head->right; head->from_tree->left = head->left;
                        previous_node->left = head->from_tree;
                        delete head; return 0;
                    }
                    while (head->from_tree->word != word) {
                        head = head->from_tree;
                    }
                    auto deletenode = head->from_tree;
                    head->from_tree = deletenode->from_tree;
                    delete deletenode;
                }
            }   /////

            else {
                head = head->left;
            }

        }
        if (word == koren->word) {
            cout << "It is impossible to delete koren" << endl;
            return 0;
        }
        tree_node_delete(head, word, key);
    }
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


              //Для второй части
   /*
    add_node(koren, "ignat");
    add_node(koren, "ignat");

    tree_node_delete(koren, "ignat");

    result_of_tree_find_node(koren, "ignat");
    */
}
