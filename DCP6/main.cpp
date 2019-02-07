#include <iostream>
#include <string>

using namespace std;
template<class T>
class List
{
    class Node
    {
        public:
        Node *xptr = nullptr;
        T val;
    public:
        Node(T nval):val(nval){}
        T get() const {return val;}
        Node* next(Node* prev) const {return reinterpret_cast<Node*>(reinterpret_cast<uint32_t>(xptr)^reinterpret_cast<uint32_t>(prev));}
        void push(Node* ptr)
        {
            xptr = reinterpret_cast<Node*>(reinterpret_cast<uint32_t>(xptr)^reinterpret_cast<uint32_t>(ptr));
            ptr->xptr = reinterpret_cast<Node*>(reinterpret_cast<uint32_t>(ptr->xptr)^reinterpret_cast<uint32_t>(this));
        }
    };
    Node *node;
public:
    List(T init)
    {
        node = new Node(init);
    }

    void Add(T nval)
    {
        Node* ptr = node;
        while((ptr->xptr!=ptr)&&(ptr->xptr!=nullptr))
            ptr = ptr->next(ptr);
        ptr->push(new Node(nval));
    }
};

int main()
{
    List<int> lst(1);
    lst.Add(2);
    lst.Add(3);
    //lst.Add("L3");
    //lst.Add("L4");
    //lst.Add("L5");

    return 0;
}
