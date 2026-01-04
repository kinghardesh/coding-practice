#include  <iostream>
using namespace std;
int main(){
    int arr1[5];
    for(i=0;i<5;i++){
        cin>>arr1[i];
    }
    isbool sorted=true;
    for(int i=0;i<4;i++){
        if(arr1[i]>arr1[i+1]){
            sorted=false;
            break;
        }
    }
    if(sorted){
        cout<<"Array is sorted"<<endl;
    }
    else{
        cout<<"Array is not sorted"<<endl;
    }
    return 0;
}

    