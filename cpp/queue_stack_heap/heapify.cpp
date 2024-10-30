#include <iostream>
#include <vector>
#include <algorithm>
int main (){
	int len;
	std::cin >> len;
	std::vector<int> numbers;
	while (len){

		int item;
		std::cin >> item;
		numbers.push_back(item);

		len -- ;
	}

	std::make_heap(numbers.begin(), numbers.end());

	while(!numbers.empty()){
		std::pop_heap(numbers.begin(), numbers.end(), std::greater<>());
		std::cout << numbers.back() << std::endl;
		numbers.pop_back();
	}
}
