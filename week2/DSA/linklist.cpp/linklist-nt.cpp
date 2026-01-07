#include <iostream>
using namespace std;
class Node{
    public:
    int data
    Node*next;
    Node(int val){
        data=val;
        next=NULL;
    }
};
void display(Node*head){
    Node*temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
}
void insertattail(Node*&head,int val){
    Node*N=new Node(val);
    if(head==Null)L{
        head=N;
        return;
    }
    Node*temp=head;
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=N;
}
void insertathead(Node*&head,int val){
    Node*N=new Node(val);
    N->next=head;
    head=N;
}

void deleteathead(Node*&head){
    Node*todel=head;
    head=head->next;
    delete todel;
}
void deleteattail(Node*&head){
    Node*temp=head;
    while(temp->next->next!=Null){
        temp=temp->next;
    }
    Node*todel=temp->next;
    temp->next=NULL;
    delete todel;
}

int main(){
    Node*head=new Node(1);
    head->next=new Node(2);
    head->next->next=new Node(3);
    head->next->next->next=new Node(4);
    insertattail(head,5);
    display(head);  
    return 0;
    

}



