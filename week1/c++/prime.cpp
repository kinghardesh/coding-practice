#include <iostream>
using namespace std;

int main() {
    int n, flag = 1;
    cout << "Enter number: ";
    cin >> n;

    if(n <= 1)
        flag = 0;

    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0) {
            flag = 0;
            break;
        }
    }

    if(flag)
        cout << "Prime Number";
    else
        cout << "Not Prime";

    return 0;
}
