#include<iostream>
#include<random>
#include< stdlib.h>
#include<chrono>
int const N = 1000000;
int a[N]; int b = 0;
using namespace std;
int diapozon = 1000;
void create_massive() {
    for (int t = 0; t < diapozon; t++) {
        //auto t = rand();
        //if (t != 0) {
        a[t] = 2 * t;
        //}
        //else {
          //t = t + 1;
          //a[i] = t;
        //}
    }
}

void show_me_massiv(int* s) {
    for (int t = 0; t < diapozon; t++) {
        cout << a[t] << ", ";
    }
}
void massiv() {
    for (int t = 1000; t <= N; t += 1000) {
        cout << t << ", ";
    }
}

void sorting_function(int* massiv) {
    while (true) {
        b = 0;
        for (int n = 0; n < N - 1; n++) {
            if (a[n] > a[n + 1]) {
                b = 1; auto t = a[n]; a[n] = a[n + 1]; a[n + 1] = t;
            }
        };
        if (b == 0) {
            break;
        }

    }
}

int prosto_perebor(int iskomoe, int* massiv) {
    /*int i = 0;
    while (massiv[i] != iskomoe && i <= diapozon ) {
        i++;
        if (i >= diapozon) { return 0; }
    }*/
        int i = 0;
        while (massiv[i] != iskomoe && i <= diapozon)
        {
            i++; if (i == diapozon) {
                //std::cout << "There is no element " << iskomoe << " in massive" << std::endl;
                return 0;
            }
        };
        //std::cout << "index of value - " << iskomoe << " is - " << i << std::endl;
}

void binarny(int iskomoe, int* massiv) {
    bool flag = false;
    int l = 0; // левая граница
    int r = diapozon - 1; // правая граница
    int mid;
    while ((l <= r) && (flag == false)) {
        mid = (l + r) / 2; // считываем срединный индекс отрезка [l,r]
        if (massiv[mid] == iskomoe) { flag = true;} //проверяем ключ со серединным элементом
        else if (massiv[mid] > iskomoe) { r = mid - 1; } // проверяем, какую часть нужно отбросить
        else if (massiv[mid] < iskomoe) { l = mid + 1; } }
    //if (flag) cout << "index of value - " << iskomoe << " is - " << mid;
    //else cout << "There is no element " << iskomoe << " in massive" << endl;
    //system("pause");
}

int random_element_from_massiv() {
    int arr[] = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0 };

    unsigned seed = 1001;
    default_random_engine rng(seed);
    uniform_int_distribution <unsigned> dstr(0, 9);

    for (unsigned counter = 100; counter != 0; --counter);
    cout << arr[dstr(rng)] << endl;
    return arr[dstr(rng)];
}

void clocks_of_perebor(int iskomoe, int* massiv) {
    //auto begin = chrono::steady_clock::now();
    for (int size = 1000; size != N; size = size + 1000) {
        auto begin = chrono::steady_clock::now();
        diapozon = size;
        for (unsigned cnt = 100; cnt != 0; --cnt){
            prosto_perebor(iskomoe, massiv);
        }
        auto end = chrono::steady_clock::now();
        auto time_span =
            chrono::duration_cast<chrono::microseconds>(end - begin);
        cout << time_span.count() << ", ";
    }
}

void clocks_of_binarny(int iskomoe, int* massiv) {
    //auto begin = chrono::steady_clock::now();
    for (int size = 1000; size <= N; size = size + 1000) {
        diapozon = size;
        auto begin = chrono::steady_clock::now();
        for (unsigned cnt = 1000000; cnt != 0; --cnt){
            binarny(iskomoe, massiv);
        } 
        auto end = chrono::steady_clock::now();
        auto time_span =
            chrono::duration_cast<chrono::microseconds>(end - begin);
        cout << time_span.count() << ", ";
    }
  }

void main() {
    create_massive();
    clocks_of_perebor(-1, a);
    cout << "\n\n";
    //clocks_of_binarny(-1, a);
    cout << "\n\n";
    massiv();
    //binarny(-1, a);
}
