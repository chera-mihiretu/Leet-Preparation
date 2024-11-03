#include <bits/stdc++.h>


#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>


typedef __gnu_pbds::tree<int, __gnu_pbds::null_type, std::less<int>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update> pbds;

int main(){

	pbds my_ordered_set;
	std::cout << "Length and Numbers" << std::endl;
	int start;
	std::cin >> start;

	while (start) {
		int item;
		std::cin >> item;

		my_ordered_set.insert(item);

		start --;
	}	
	std::cout << "Query Number Greater" << std::endl;
	int query;

	std::cin >> query;

	while (query){

		int number;
		std::cout << "Number Less Than Your Input" <<  std::endl;
		std::cin >> number;

		std::cout << "Smaller Count is : " << my_ordered_set.order_of_key(number) << std::endl;

		query -- ;
	}

	std::cout << "Number at index should be less than the element" << std::endl;

	std::cin >> query;

	while(query){
		int number;
		std::cin >> number;
		std::cout << "The " << number << "th Value : "<< *my_ordered_set.find_by_order(number) << std::endl;

		query -- ;
	}


	return 0;
}
