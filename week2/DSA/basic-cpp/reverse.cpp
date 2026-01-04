#include <iostream>
using namespace std;
int main(){
    int arr1[] = {1,2,3,4,5};
    int rev[5];
    for(int i=0;i<5;i++){
        rev[i]=arr1[4-i];
    }
    for(int i=0;i<5;i++){
        cout<<rev[i]<<" ";
    }
    return 0;
}
