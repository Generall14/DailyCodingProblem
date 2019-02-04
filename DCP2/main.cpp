#include "../utils.hpp"
#include <vector>
#include <numeric>
#include <functional>

int main()
{
    auto in = getv();
    pv(in);
    int pr = std::accumulate(in.begin(), in.end(), 1, std::multiplies<int>());
    for(std::vector<int>::iterator it = in.begin(); it!=in.end(); it++)
        (*it) = pr/(*it);
    pv(in);
    return 0;
}
