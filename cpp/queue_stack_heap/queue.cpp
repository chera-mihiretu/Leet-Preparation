#include <iostream>
#include <queue>
#include <deque>
void theQueue() {
	
	std::queue<int> numbers;

	for (int i =0 ; i < 10; i ++ ){
		numbers.push(i);
	}
	
	while(!numbers.empty()){
		std::cout << numbers.front() << numbers.back() << std::endl;
		
		numbers.pop();
	}
}


void theDeque(){
	
	std::deque<int> numbers;

	for (int i = 0; i < 20; i ++ ){
		numbers.push_back(i);
	}

	while (!numbers.empty()){
		std::cout << numbers.front() << " " << numbers.back() << std::endl;
		numbers.pop_back();
		numbers.pop_front();
	}
	
}

int main (){
	theDeque();
}
