#include <vector>
#include "../utils.hpp"

int ff(std::vector<int> in)
{
    int i=0;
    while(++i)
    {
        if(i>=in.size())
            return i;
        if(in.at(i)!=i)
            return i;
    }
}

int main()
{
    auto in = getv();
    in.push_back(0);

    for(int i=0;i<in.size();i++)
    {
        if((in.at(i)<i)&&(in.at(i)>=0))
        {
            int t = in.at(i);
            in[i]=in.at(t);
            in[t]=t;
            if(in.at(i)!=t)
                i--;
        }
    }

    pv(in);
    std::cout << ff(in) << std::endl;
    return 0;
}
