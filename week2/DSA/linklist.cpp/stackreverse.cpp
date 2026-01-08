#include <iostream>
using namespace std
Class Node{
    public:
        int data;
        Node*next;
        Node(int val){
            data=val;
            next=Null;
        }
}
class stack{
    stack{
        top=Null;
    }
    void reverseusingstack(Node*head){
        Node*head=top;
        stack<int> st;
        while(temp!=Null){
                
        }

    }
    push(){
        Node*N=new Node(val);
        n->next=top;
        top=n;
    }
    pop(){
        if (top==Null){
            cout<<"stack underflow";
            return;
        }
        Node*temp=top;
        top=top->next;
        delete temp;
    }
    peek(){
        if (top==Null) retun -1;
        return top->data;
    }
    display{
        Node*temp=top;
        while(temp!=Null){
            cout<<temp->data->"";
            temp=temp->data;
        }
        cout<<endl;
    }
}
int main(){
    stack s;
    s.push(3);
    s.pop();
    s.push(5);
    cout<<s.display<<"";
}