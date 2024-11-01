#include <iostream>
#include <set>
#include <string>
#include <algorithm>

int main(){

	int length;
	std::cin >> length;
	std::set<std::string> my_set;

	for (int i =0 ; i < length; i++ ){
		std::string item;

		std::cin >> item;

		my_set.insert(item);
	}
	
	std::cout << "Insert The One You Want to do Operation On" << std::endl;

	std::cin >> length;
	std::set<std::string> another_set;
	
	for (int i =0 ; i < length; i ++ ){
		std::string item;
		std::cin >> item;

		another_set.insert(item);
	}
	/*
	std::cout << "This Is Union" << std::endl;

	std::set<std::string> unioned;

	unioned.insert(my_set.begin(), my_set.end());

	unioned.insert(another_set.begin(), another_set.end());

	for (auto value : unioned){
		std::cout << value << std::endl;
	}

	std::cout << "This is Intersection" << std::endl;

	std::set<std::string> intersection;

	for (auto value : my_set){
		if (another_set.find(value) != another_set.end()){
			intersection.insert(value);
		}
	}

	
	for (auto value : intersection){
		std::cout << value << std::endl;
	} */

	// This is are built in function from algorithm 
	//
	



	std::set<std::string> unioned, intersectioned, difference, symmetric;

	std::cout << "Union" << std::endl;
	std::set_union(my_set.begin(), my_set.end(), another_set.begin(), another_set.end(), std::inserter(unioned, unioned.begin()));
	for (auto value : unioned) std::cout << value << " ";
	std::cout << " " << std::endl;
	std::cout << "Intersection" << std::endl;
	std::set_intersection(my_set.begin(), my_set.end(), another_set.begin(), another_set.end(), std::inserter(intersectioned, intersectioned.begin()));
	
	for (auto value : intersectioned) std::cout << value << " ";
	std::cout << " " << std::endl;
	std::cout << "Difference" << std::endl;
	std::set_difference(my_set.begin(), my_set.end(), another_set.begin(), another_set.end(), std::inserter(difference, difference.end()));
	
	for (auto value : difference) std::cout << value << " ";
	std::cout << " " << std::endl;
	std::cout << "Symetric" << std::endl;
	std::set_symmetric_difference(my_set.begin(), my_set.end(), another_set.begin(), another_set.end(), std::inserter(symmetric, symmetric.begin()));

	for (auto value : symmetric) std::cout << value << " ";
	std::cout << " " << std::endl;

}


