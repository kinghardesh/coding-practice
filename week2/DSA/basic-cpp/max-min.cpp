#include <iostream>
using namespace std;
int main(){
    int arr1[6];
    for(int i=0;i<6;i++){
        cin>>arr1[i];
    }
    int max=arr1[0];
    int min=arr1[0];
    for(int i=0;i<6;i++){
        if(arr1[i]>max){
            max=arr1[i];
        }
        if(arr1[i]<min){
            min=arr1[i];
        }
        cout<<"\nMax:"<<max<<endl;
        cout<<"\nMin:"<<min<<endl;
        return 0;
    }
}