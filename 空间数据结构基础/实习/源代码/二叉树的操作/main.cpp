#include "BinaryTree.h"

template<class Type>
void BinaryTree<Type>::destroy(BinTreeNode<Type> *node)
{
    if(node != NULL)
    {
        destroy(node->leftChild);
        destroy(node->rightChild);
        delete node;
    }
}

template <class Type>
void BinaryTree<Type>::Traverse(BinTreeNode<Type> *node, ostream &out)
{
    if ( node != NULL ) {
        out << node->data <<' ';
        Traverse (node->leftChild, out);
        Traverse (node->rightChild, out);
    }
}

template <class Type>
void BinaryTree<Type>::create(Type *nodevalue)
{
    BinTreeNode <Type> *t;
    int ai = 0;
    t = new BinTreeNode<Type>();
    t->data = nodevalue[0];
    t->leftChild = NULL;
    t->rightChild = NULL;
    root = t;
    qi = 0;
    qu[qi] = t;
    ai = 1;
    while (nodevalue[ai] != '#') {
        if(nodevalue[ai] == ' ')
        {
            qu[ai] = NULL;
        }
        else{
            t = new BinTreeNode<Type>();
            t->data = nodevalue[ai];
            t->leftChild = NULL;
            t->rightChild = NULL;
            qu[qi]->leftChild = t;
            qu[2*qi+1] = t;
        }
        ai++;
        if(nodevalue[ai] == '#')
            break;
        if(nodevalue[ai] == ' ')
        {
            qu[ai] = NULL;
        }
        else{
            t = new BinTreeNode<Type>();
            t->data = nodevalue[ai];
            t->leftChild = NULL;
            t->rightChild = NULL;
            qu[qi]->rightChild = t;
            qu[2*qi+2] = t;
        }
        ai++;
        qi++;
    }
    cout << "二叉树已经建立完成" << endl;
}

template <class Type>
void BinaryTree<Type>::InordPrint()
{
    top = -1;
    BinTreeNode <Type> *p;
    if(root == NULL)
    {
        return ;
    }
    p = root;
    while(p || top>=0){
        if(p)
        {
            st[++top] = p;
            p = p->leftChild;
        }
        else{
            p = st[top--];
            cout << p->data << ' ';
            p = p->rightChild;
        }
    }
    cout << endl;
}

template <class Type>
void BinaryTree<Type>::printree(BinTreeNode<Type> *t)const
{
    if(t != NULL)
    {
        cout << t->data;
        if(t->leftChild!=NULL || t->rightChild!=NULL)
        {
            cout << '(';
            printree(t->leftChild);
            if(t->rightChild!=NULL)
                cout << ',';
            printree(t->rightChild);
            cout << ')';
        }
    }
}

template <class Type>
void BinaryTree<Type>::Postorder(BinTreeNode<Type> *t)const
{
    if ( t != NULL ) {
        Postorder(t->leftChild);
        Postorder(t->rightChild);
        cout<<t->data<<' ';
    }
}

template <class Type>
void BinaryTree<Type>::pttree()
{
    if(root != NULL)
        printree(root);
    cout << endl;
}

template <class Type>
BinTreeNode<Type> *BinaryTree<Type>::getRoot()
{
    return root;
}

template <class Type>
void BinaryTree<Type>::PordPrint()
{
    if(root != NULL)
        Postorder(root);
    cout << endl;
}

template <class Type>
int BinaryTree<Type>::getDepth(BinTreeNode<Type> *ro)
{
    if (ro == NULL)
        return 0;
    int l, r;
    l = getDepth(ro->leftChild);
    r = getDepth(ro->rightChild);
    return l>=r ? (l+1) : (r+1);
}

template <class Type>
int BinaryTree<Type>::getNum(BinTreeNode<Type> *ro)
{
    if (ro == NULL)
        return 0;
    int l, r;
    l = getNum(ro->leftChild);
    r = getNum(ro->rightChild);
    return l+r+1;
}

template<class Type>
int BinaryTree<Type>::getLeafNum(BinTreeNode<Type> *ro)
{
    static int leaf = 0;
    if (ro == NULL)
        return 0;
    if (ro->leftChild == NULL && ro->rightChild == NULL)
    {
        leaf++;
    }
    getLeafNum(ro->leftChild);
    getLeafNum(ro->rightChild);
    return leaf;
}

template<class Type>
bool BinaryTree<Type>::ifEmpyt()
{
    if (root == NULL)
        return false;
    else
        return true;
}

int main()
{
    BinaryTree<char> mybt;
    BinTreeNode<char> *R;
    char data[20]={'a', 'b', 'c', ' ', 'e', 'f', 'g', ' ', ' ', 'h', 'i', 'j', '#'};
    mybt.create(data);
    R = mybt.getRoot();
    mybt.pttree();
    cout << endl;
    cout << "非递归中序遍历并输出二叉树:" << endl;
    mybt.InordPrint();
    cout << endl;
    cout << mybt;
    cout << endl;
    cout << "后序遍历并输出二叉树:" << endl;
    mybt.PordPrint();
    cout << endl;
    cout << "该二叉树的深度为：" << mybt.getDepth(R) << endl;
    cout << "该二叉树节点个数为：" << mybt.getNum(R) << endl;
    cout << "该二叉树叶子结点数为：" << mybt.getLeafNum(R) << endl;
    mybt.destroy(R);
    if(mybt.ifEmpyt())
        cout << "该二叉树已空" << endl; //记得改程序，false和true互倒
    return 0;
}
