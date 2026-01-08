#include<iostream>
class Node{
    public:
        int data;
        Node* prev;
        Node* next;
        Node(int val){
            data = val;
            prev = Null;
            next = Null;
        }      
    void display(Node*head){
        Node*temp=head;
        while(temp!=Null){
            cout<<temp->data<<"";
            temp=temp->next<<"";
        }
    cout<<endl;
    }
    void insertathead(Node*&head,int val){
        Node*N=new Nodeode(val);
        while(head->prev){
            N->dat=val;
            N->next=head;
            head->prev=N;
        }
        head=N;
    }
    void insertattail(Node*&head,int val){
        Node*N=new Node(val)
        if(head==Null){
            head=N;
            return;
        }
        Node*temp=head;
        while(temp->next!=Null){
            temp=temp->next;
        }
        temp->next=N;
        N->prev=temp;
    }
    void deleteattail(Node*&temp,int val){
        if (head->next==Null){
            delete head;
            head= NULL;
            return;
        }
        while(temp->next!=NULL){
            temp->next = temp;
        }
        temp->prev->next=Null;
        delete temp;
    }
    void reverseDLL(Node*&head){
        Node*curr=head;
        Node*temp=Null;
        while(curr!=Null){
            temp=curr->prev;
            curr->prev=curr->next;
            curr->next=temp;
            curr=curr->prev;
        }
        if (temp!=Null){
            head=temp->prev;
        }
    }


}
int main(){
    Node*head= new head(1);
    Node*second=new head(2);
    Node*third=new head(3);
    head->next=second;
    second->next=head;
    second->next=third;
    third->prev=second;
    insertathead(head,0);
    display(head);
    insertathead(head,4);
    display(head);
    

    return 0;
}

