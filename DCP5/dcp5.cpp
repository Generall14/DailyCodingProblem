#include <iostream>
#include <functional>

auto cons(int a, int b)
{
    auto loc = [a, b](std::function<int(int, int)> ff){return ff(a, b);};
    return loc;
}

int car(auto ex)
{
    auto loc = [](int a, int b)->int{return a;};
    return ex(loc);
}

int cdr(auto ex)
{
    auto loc = [](int a, int b)->int{return b;};
    return ex(loc);
}

int main()
{
    std::cout << car(cons(3, 4)) << std::endl;
    std::cout << cdr(cons(3, 4)) << std::endl;
    return 0;
}
