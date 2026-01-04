#include <iostream>
using namespace std;
int main(){
    int arr1[5];
    int start=0;
    int end=4;
    for(int i=0;i<5;i++){
        cin>>arr1[i];
    }
    while(start<end){
        swap(arr1[start],arr1[end]);
        start++;
        end--;
    }
    for(int i=0;i<5;i++){
        cout<<arr1[i]<<" ";
    }
}
