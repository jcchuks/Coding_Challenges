/*
Breadth first Search in C/C++ compatible code. No extra libs included.
Solution to https://www.hackerrank.com/challenges/tree-level-order-traversal on Hackerrank.
 
struct node
{
    int data;
    node* left;
    node* right;
}*/
struct Que{
    struct QueNode* hd;
    struct QueNode* tl;
};

struct QueNode{
    struct QueNode* next;
    struct node* nd;    
};
bool isEmpty(struct Que* que){
    if ((que->hd == NULL)){
        return true;
    }else{
        return false;
    }
}

void enq(struct Que* que, struct node* item){
    struct QueNode* newQnode = (struct QueNode*)malloc(sizeof(QueNode));
    if(isEmpty(que)){
        newQnode->nd = item;
        newQnode->next = NULL;
        que->hd = newQnode;
        que->tl = newQnode;   
    }else{
        struct QueNode* temp = que->tl; 
        newQnode->next = NULL;
        newQnode->nd = item;
        temp->next = newQnode; 
        que->tl = newQnode;
    } 
}

struct QueNode* deq(struct Que* que){
    if(isEmpty(que)){
        return ((struct QueNode*)NULL);
    }else{
        struct QueNode* value;
        value = que->hd;
        que->hd = que->hd->next;
        return value;        
    }
}

void LevelOrder(node * root)
{
  if(!root){
      return;
  }
    struct Que* Q = (struct Que*)malloc(sizeof(struct Que));
    Q->hd = NULL;
    Q->tl = NULL;
        
    enq(Q,root);
    int i = 0;
    while(!isEmpty(Q)){
        struct QueNode* item ;
        item = deq(Q); 
        printf("%d ",item->nd->data);
        if ( item->nd->left!=NULL){
            enq(Q,item->nd->left);
        }
        if( item->nd->right!=NULL){
           enq(Q,item->nd->right) ;
        } 
    }
  
  
}
