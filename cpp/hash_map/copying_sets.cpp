#include <iostream>
#include <set>


int main (){
	
	std::set<int> setOne = {1,2,3,4};

	std::set<int> setTwo = setOne;

	setTwo.erase(3);

	for (auto value : setOne){
		std::cout << value;
	}

	std::cout << std::endl;

	for (auto value = setTwo.begin(); value != setTwo.end(); ++value){
		std::cout << *value;
	}
	
	std::cout << std::endl;

	return 0;

}
