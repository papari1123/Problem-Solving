/* 
괜히 복잡하게 푼 듯..
이 풀이말고, 이진탐색트리의 정의에 따라 중위순회 시 크기가 정렬됨을 알면 쉽게 풀 수 있음.



The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/
    struct NodeInfo {
        bool flag;
        int max;
        int min;
    };
    
    NodeInfo getNodeInfo(Node* root)
    {
        NodeInfo nodeInfo;
        nodeInfo.max = root->data;
        nodeInfo.min = root->data;
        nodeInfo.flag = true;
        if(root->left!=NULL)
        {
            NodeInfo nodeLeftInfo = getNodeInfo(root->left);
            if(nodeLeftInfo.max >= root->data || !nodeLeftInfo.flag)
                nodeInfo.flag = false; 
            nodeInfo.max = max(nodeLeftInfo.max,nodeInfo.max);
            nodeInfo.min = min(nodeLeftInfo.min,nodeInfo.min);
        }
        if(root->right!=NULL)
        {
            NodeInfo nodeRightInfo = getNodeInfo(root->right);
            if(nodeRightInfo.min <= root->data || !nodeRightInfo.flag)
                nodeInfo.flag = false;
            nodeInfo.max = max(nodeRightInfo.max,nodeInfo.max);
            nodeInfo.min = min(nodeRightInfo.min,nodeInfo.min);
        }    
        return nodeInfo;
    }

	bool checkBST(Node* root) {
		return getNodeInfo(root).flag;
	}


