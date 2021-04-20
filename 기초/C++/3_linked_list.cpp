/*
    Sructure로 linked-list Node를 만들고,
    Node를 생성 및 삭제하는 방법.
*/

#include <iostream>

using namespace std;
struct Node {
    int data;
    struct Node *next;
};
int main(void)
{
    Node *head = NULL;
    Node *tail = NULL;
    Node *cur = NULL;
    Node *newNode = NULL;
    int readData;
    while(1)
    { // linked list 생성
        cout << "put data (0: break)";
        cin >> readData;
        if(readData == 0)
            break;
        newNode = new Node();
        newNode->data = readData;
        newNode->next = NULL;
        if(head == NULL)
            head = newNode;
        else
            tail->next = newNode;
        tail =  newNode;
    }
    cout<<endl;

    cout << "print output";
	if (head == NULL)
	{
		cout << "no data" << endl;
	}
	else
	{ // cursor를 움직이며 데이터 확인.
		cur = head;
		cout << cur->data << " ";

		while (cur->next != NULL)
		{
			cur = cur->next;
			cout << cur->data << " ";

		}
	}
	cout << endl <<"remove node.";
    if (head == NULL)
		return 0;
	else
	{
        // head 삭제 후 계속 삭제..
		Node *removeNode = head;
		Node *removeNextNode = head->next;

		cout <<"remove : "<<removeNode->data << endl;
		free(removeNode); // 삭제

		while (removeNextNode != NULL)
		{
			removeNode = removeNextNode;
			removeNextNode = removeNextNode->next;
			
			cout<<"remove : "<<removeNode->data << endl;
			free(removeNode);
		}
	}

    return 0;
}