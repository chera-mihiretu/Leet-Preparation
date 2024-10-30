#include <iostream>
#include <vector>
#include <algorithm>

int main (){

	std::vector<int> numbers;

	for (int i=0 ; i < 30; ++i){
		numbers.push_back(i);

	}

	std::vector<int> copied;
	copied.resize(3);

	std::copy(numbers.begin() + 2, numbers.begin() + 5, copied.begin());

	for (auto value : copied){
		std::cout << value << std::endl;
	}
}
