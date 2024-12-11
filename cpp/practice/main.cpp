#include <bits/stdc++.h>

void function(){
    static int x = 0;
    x++;
    std::cout << "This is value of x : "<< x << std::endl;
}
int main(){
    function();
    function();
    function();
    function();
    function();
    return 0;
}

