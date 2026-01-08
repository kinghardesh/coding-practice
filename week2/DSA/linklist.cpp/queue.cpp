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
}
class queue{
    Node*rear;
    Node*front;
    public:
        Queue(){
            front=rear=Null;
        }
        void enqueu(int val){
            Node*n=new Node(val);
            if (rear==Null){
                front=rear=n;
                return;
            }
            rear->next=n;
            rear=n;
        }
        void dequeu{
            if(front===Null){
                cout<<"the queue is overflow";
            }
            Node*temp=front;
            front=front->next;
            if(front==Null)rear=null;
            delete temp;
        }
        void display(){
            Node*temp=front;
            while(temp!=Null){
                cout<<temp->next->"";
                temp=temp->next
            }
        cout<<endl;    
        }
        peek(){
            if (front==Null) return -1;
            return front->next
        }
}
int main(){
    queue q;
    q.enqueu(4);
    q.enqueu(2);
    q.enqueu(6);
    q.dequeu();
    cout<<q.peak()<<endl;
    q.display();
}