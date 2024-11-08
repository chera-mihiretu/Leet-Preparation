#include <bits/stdc++.h>



int main(){
    
    long long times, k;
    std::cin >> times >> k;

    while (k --){
        if ((times% 10)){
             times -= 1;
        }else{
            times /= 10;
        }
    }
    std::cout << times << std::endl;
}