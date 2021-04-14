/*
이진트리의 노드 생성, 삽입, 삭제와
전위, 중위, 후위 순회 방법을 공부함.
*/

#include <iostream>
using namespace std;
struct Node {
    char data;
    struct Node *left;
    struct Node *right;
};
void preOrder(struct Node *node);
void postOrder(struct Node *node);
void inOrder(struct Node *node);

int main(void)
{
    int N;
    cin >> N;
   
    Node *NodeList[26];    
    // 노드를 먼저 생성하고 시작.
    for(int i=0; i<N;i++)
    {
         Node *rootNode = new Node();  
         NodeList[i] = rootNode;
    }
    // 노드를 이미 생성했기 때문에 데이터와 연결만 넣어주면 됨.
    for(int i=0; i<N;i++)
    {  
        char rootData, left, right;
        cin>>rootData>>left>>right; 
        NodeList[rootData-'A']->data = rootData;
        if(left=='.')   
            NodeList[rootData-'A']->left = NULL; 
        else 
            NodeList[rootData-'A']->left = NodeList[left-'A'];
        if(right=='.')    
            NodeList[rootData-'A']->right = NULL; 
        else
            NodeList[rootData-'A']->right = NodeList[right-'A'];
    }
    //전위 순회 : root->left->right
    preOrder(NodeList[0]);
    cout<<endl;
    //중위 순회 : left->root->right
    inOrder(NodeList[0]);
    cout<<endl;
    //후위 순회 : left->right->root
    postOrder(NodeList[0]);
    cout<<endl;
    return 0;
}
void preOrder(struct Node *node)
{
    if(node!=NULL)
    {
    cout<<node->data; //root
    preOrder(node->left);
    preOrder(node->right);
    }
}
void inOrder(struct Node *node)
{
    if(node!=NULL)
    {
    inOrder(node->left);
    cout<<node->data; //root
    inOrder(node->right);
    }
}
void postOrder(struct Node *node)
{
    if(node!=NULL)
    {
    postOrder(node->left);
    postOrder(node->right);
    cout<<node->data; //root
    }
}