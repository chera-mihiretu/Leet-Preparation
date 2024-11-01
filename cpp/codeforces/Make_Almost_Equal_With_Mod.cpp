#include <iostream>
#include <vector>
#include <algorithm>

int solve(){
	int length;
	std::cin >> length;
	std::vector<int> array;
	while (length){
		int x;
		std::cin >> x;
		array.push_back(x);
		length --;
	}

	return 2;

}

int main(){
	int testCase;
	std::cin >> testCase;

	for (int i=0; i < testCase; i ++ ){
		std::cout << solve() << std::endl;
	}
	return 0;
}
