#include <iostream>
#include <queue>


void maxHeap(){
	
	std::priority_queue<int> my_heap;
	int len;
	std::cin >> len;
	for (int i = 0; i < len; i ++ ){
		int item;
		std::cin >> item;

		my_heap.push(item);

	}
	while(!my_heap.empty()){
		std::cout << my_heap.top() << std::endl;
		my_heap.pop();
	}
}
void minHeap(){

	std::priority_queue<int, std::vector<int>, std::greater<int>> my_heap;
	

	int len;
	std::cin >> len;

	while(len){
		int item;
		std::cin >> item;
		my_heap.push(item);
		len -- ;
	}

	while(!my_heap.empty()){
		std::cout << my_heap.top() << std::endl;
		my_heap.pop();
	}
}


int main (){
	minHeap();
}
