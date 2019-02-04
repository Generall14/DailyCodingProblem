#include "utils.hpp"
#include <iostream>
#include <sstream>
#include <string>

std::vector<int> getv()
{
	std::string s;
    std::getline(std::cin, s);
    std::istringstream ss(s);
    std::vector<int> v;
    while(std::getline(ss, s, ' '))
        v.push_back(std::stoi(s));
    return v;
}

void pv(std::vector<int> vec)
{
    std::cout << "[ ";
    for(auto v: vec)
        std::cout << v << " ";
    std::cout << "]" << std::endl;
}
