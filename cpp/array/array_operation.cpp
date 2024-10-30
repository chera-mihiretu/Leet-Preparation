#include <iostream>
#include <vector>

int main (){
	std::vector<int> numbers;
	if (!numbers.empty())
		numbers.pop_back();
	for (int i= 0 ; i < 10; i ++){
		numbers.push_back(i);
	}
	numbers.pop_back();
	numbers.pop_back();
	for (int number : numbers) std::cout << number << " " ;
	std::cout << std::endl;

}
