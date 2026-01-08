#include <iostream>
using namespace std
class Node{
    public:
        int data;
        Node*next;
        Node(int val){
            data=val;
            next=Null;
        }
};
class stack{
    node*stack;
    public:
        stack(){
            top=Null;
        }
        void push(int val){
            Node*N=new Node(Val);
            n->next=top;
            top=n;
        }
        void pop(int val){
            if (top==Null){
                cout<<"Underflow"<<endl;
                return;
            }
            Node*temp=top;
            top=top->next;
            delete temp;
        }
        void peek{
            if (top==Null)return -1;
            return top->data;
        }
        void display{
            Node* temp= top;
            while(temp=!Null){
                cout<<temp->data->""
                temp=temp->next;
            }
        }
};
int main(){
    stack s;
    s.push(2);
    s.pop();
    s.push(3);
    s.pop();
    s.push(4);
    s.push(5);
    cout<<s.peek();
    cout<<s.display();
}