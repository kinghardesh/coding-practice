#include <iostream>
using namespace std;
int main() {
    int arr[5];
    for(int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    int idx = 0;

    for(int i = 0; i < 5; i++) {
        if(arr[i] != 0) {
            arr[idx] = arr[i];
            idx++;
        }
    }

    while(idx < 5) {
        arr[idx] = 0;
        idx++;
    }

    for(int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
