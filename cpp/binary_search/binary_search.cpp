#include <iostream>
#include <vector>
#include <algorithm>

int main (){

	std::vector<int> arr = {1,2,3,3,3,3,3,4,5,6,7};
	for (auto val : arr){
		std::cout << val << " ";
	}
	std::cout << std::endl;
	int searches;
	std::cin >> searches;
	while (searches){
		int target;
		std::cout <<  "Target : ";
		std::cin >> target;
		int lower_bound = std::lower_bound(arr.begin(), arr.end(), target) - arr.begin();
		std::cout << "Lower Bound : "<< lower_bound << std::endl;
		int upper_bound = std::upper_bound(arr.begin(), arr.end(), target) - arr.begin();
		std::cout << "Upper Bound : " << upper_bound << std::endl;	
		searches -- ;
	}
	

	return 0;
}
