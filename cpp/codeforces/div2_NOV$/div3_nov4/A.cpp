#include <bits/stdc++.h> 
bool solve(){
	int length;
	std::cin >> length;
	std::vector<int> array;
	for (int i =0 ; i < length; ++i) {
		int item;
		std::cin >> item;
		array.push_back(item);
	}

	for (int j = 1; j < length;++j ){
		int diff = std::abs(array.at(j) -  array.at(j-1));
		if (diff != 5 && diff != 7){
			return false;
		}
	}
	return true;
}	


int main (){
	int test;

	std::cin >> test;

	while (test -- ){

		if (solve()){
			std::cout << "YES" << " ";
		}else{
			std::cout << "NO" << " ";
		}
	}
	std::cout << std::endl;
}
