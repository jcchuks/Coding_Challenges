//https://www.hackerrank.com/challenges/ctci-linked-list-cycle
//Tortoise and the Hare algos

/*
Detect a cycle in a linked list. Note that the head pointer may be 'NULL' if the list is empty.

A Node is defined as: 
    struct Node {
        int data;
        struct Node* next;
    }
*/

 
bool has_cycle(Node* head) {
    // Complete this function
    // Do not write the main method
    if(!head){
        return false;
    }
    
    Node* tortoise = head->next;
    Node* hare = (head->next)?head->next->next: NULL;
    while (tortoise && hare){
        if (tortoise == hare){
            return true;
        }else{
            tortoise = tortoise->next;
            hare = hare -> next ? hare->next->next : NULL;
        }
    }
    return false;
    
}
