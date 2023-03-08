#include<iostream>
#include<random>
#include< stdlib.h>
#include<chrono>
int const N = 100000;
int a[N]; int b = 0;
using namespace std;
int diapozon = 1000;
void create_massive() {
    for (int t = 0; t < diapozon; t++) {
        a[t] = 2 * t;
    }
}

void show_me_massiv(int* s) {
    for (int t = 0; t < diapozon; t++) {
        cout << a[t] << ", ";
    }
}
void massiv() {
    for (int t = 100; t <= N; t += 100) {
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
    int l = 0;
    int r = diapozon - 1;
    int mid;
    while ((l <= r) && (flag == false)) {
        mid = (l + r) / 2;
        if (massiv[mid] == iskomoe) { flag = true;} 
        else if (massiv[mid] > iskomoe) { r = mid - 1; } 
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

void suma_dvux(int iskomaya_summa, int* massiv) {
    bool flag = false;
    for (int j = 0; (j != diapozon) && (flag == false); j++) {
        for (int i = j + 1; (flag == false) && (i < diapozon); i++) {
            if (massiv[j] + massiv[i] == iskomaya_summa) {
                cout << "fijures are " << massiv[i] << " and " << massiv[j] << endl;
                flag = true;
            }
        }
    }
}

int suma_dvux_uporyadochenaya(int iskomaya_summa, int* massiv) {
    bool flag = true;
    int l = 0;
    int r = diapozon - 1;
    while (flag && l < r)
    {
        if (massiv[l] + massiv[r] == iskomaya_summa) {
            cout << "fijures are " << massiv[l] << " and " << massiv[r] << endl;
            flag = false;
        }
        else if (massiv[l] + massiv[r] < iskomaya_summa) {
            l += 1;
        }
        else if (massiv[l] + massiv[r] > iskomaya_summa){
            r -= 1;
        }
    }
    return 0;
}

void clocks_of_perebor_for_summ(int iskomoe, int* massiv) {
    for (int size = 1000; size <= N; size = size + 1000) {
        auto begin = chrono::steady_clock::now();
        diapozon = size;
        for (unsigned cnt = 1; cnt != 0; --cnt) {
            suma_dvux(iskomoe, massiv);
        }
        auto end = chrono::steady_clock::now();
        auto time_span =
            chrono::duration_cast<chrono::microseconds>(end - begin);
        cout << time_span.count() << ", ";
    }
}

void clocks_of_summ_for_uporyadochenaya(int iskomoe, int* massiv) {
    for (int size = 1000; size <= N; size = size + 1000) {
        auto begin = chrono::steady_clock::now();
        diapozon = size;
        for (unsigned cnt = 7500; cnt != 0; --cnt) {
            suma_dvux_uporyadochenaya(iskomoe, massiv);
        }
        auto end = chrono::steady_clock::now();
        auto time_span =
            chrono::duration_cast<chrono::microseconds>(end - begin);
        cout << time_span.count() << ", ";
    }
}

void clocks_of_perebor(int iskomoe, int* massiv) {
    for (int size = 100; size <= N; size = size + 100) {
        auto begin = chrono::steady_clock::now();
        diapozon = size;
        for (unsigned cnt = 1000; cnt != 0; --cnt){
            prosto_perebor(iskomoe, massiv);
        }
        auto end = chrono::steady_clock::now();
        auto time_span =
            chrono::duration_cast<chrono::microseconds>(end - begin);
        cout << time_span.count() << ", ";
    }
}

void clocks_of_binarny(int iskomoe, int* massiv) {
    for (int size = 100; size <= N; size = size + 100) {
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
    //show_me_massiv(a);
    clocks_of_perebor(-1, a);
    //cout << "\n\n";
    //clocks_of_binarny(-1, a);
    cout << "\n\n";
    massiv();
    //binarny(-1, a);
    //suma_dvux_uporyadochenaya(1, a);
    //clocks_of_perebor_for_summ(1, a);
    //clocks_of_summ_for_uporyadochenaya(1, a);
    //suma_dvux(2500, a);
}
