#ifndef BinaryTree_h
#define BinaryTree_h
#include <iostream>
using namespace std;

template <class Type>
class BinaryTree;

template <class Type>
class BinTreeNode
{
    friend class BinaryTree<Type>;
private:
    BinTreeNode<Type> *leftChild, *rightChild;
    Type data;
public:
    BinTreeNode () : leftChild (NULL), rightChild (NULL){}
    BinTreeNode (Type item, BinTreeNode<Type> *left = NULL,BinTreeNode<Type> *right = NULL)
        : data (item), leftChild (left), rightChild (right){}
    Type GetData () const {return data;}
};

template <class Type>
class BinaryTree
{
public:
    BinaryTree () : root(NULL){}
    void create(Type *array);
    void InordPrint();
    void pttree();
    void PordPrint();
    friend ostream& operator << (ostream& out, BinaryTree<Type>& Tree)
    {
        out << "二叉树的前序遍历序列:\n";
        Tree.Traverse(Tree.root, out);
        out << endl;
        return out;
    }
    int getDepth(BinTreeNode<Type> *ro);
    int getNum(BinTreeNode<Type> *ro);
    int getLeafNum(BinTreeNode<Type> *ro);
    void destroy(BinTreeNode<Type> *node);
    bool ifEmpyt();
    BinTreeNode<Type> *getRoot();
private:
    BinTreeNode<Type> *root;
    BinTreeNode<Type> *st[30];
    int top;
    BinTreeNode<Type> *qu[20];
    int qi;
    void Traverse(BinTreeNode<Type> *node, ostream& out);
    void printree(BinTreeNode<Type> *t)const;
    void Postorder(BinTreeNode<Type> *t)const;
};
#endif /* BinaryTree_h */
