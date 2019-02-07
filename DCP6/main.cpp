#include <iostream>
#include <string>
#include <stdexcept>

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
        Node* next(Node* prev) const
        {
            uint64_t x = reinterpret_cast<uint64_t>(xptr)^reinterpret_cast<uint64_t>(prev);
            if(!x)
                throw std::logic_error("index out of range");
            return reinterpret_cast<Node*>(x);
        }
        void push(Node* ptr)
        {
            xptr = reinterpret_cast<Node*>(reinterpret_cast<uint64_t>(xptr)^reinterpret_cast<uint64_t>(ptr));
            ptr->xptr = reinterpret_cast<Node*>(reinterpret_cast<uint64_t>(ptr->xptr)^reinterpret_cast<uint64_t>(this));
        }
    };
    
    Node* geti(int i=-1)
    {
        Node* ptr = node;
        try
        {
            Node* prev = nullptr;
            while(i--)
            {
                Node* tmp = ptr;
                ptr = ptr->next(prev);
                prev = tmp;
            }
        }
        catch(logic_error e)
        {
            if(i>=0)
                throw e;
        }
        return ptr;
    }

    Node *node;
public:
    List(T init)
    {
        node = new Node(init);
    }

    void Add(T nval)
    {
        geti()->push(new Node(nval));
    }

    T get(unsigned int i)
    {
        return (geti(i))->val;
    }
};

int main()
{
    List<string> lst("L0");
    lst.Add("L1");
    lst.Add("L2");
    lst.Add("L3");
    lst.Add("L4");
    lst.Add("L5");
    try
    {
        for(int i=0;i<20;i++)
            cout << "lst[" << i << "] = " << lst.get(i) << endl;
    }
    catch (logic_error)
    {
        cout << "iaor" << endl;
    }

    return 0;
}
