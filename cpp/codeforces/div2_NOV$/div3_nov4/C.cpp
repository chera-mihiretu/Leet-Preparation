#include <bits/stdc++.h>
#include <vector>
int checkThem(std::vector<char> &actual, int i, int n){
	if (i < 0) return false;
	if (i + 3 >= n) return false;
	std::string compare = "1100";
	for(int j = 0; j < 4; ++ j){
		if (compare[i] != actual[j + i]){
			return false;
		} 
	}
	return true;
}

void solve(){

	int count = 0;
	std::string bit;
	std::cin >> bit;
	int length = bit.length();
	std::vector<char> bits(bit.begin(), bit.end());

	// Build the count 
	for (int i = 0; i < length; ++ i) {

		count += checkThem(bits, i, length);
	}


	// This is the number of queries
	
	int q;
	std::cin >> q;

	while (q -- ){
		int index, change;
		std::cin >> index >> change;
		index --;
		if (bits.at(index) != '0' + change){
			bool after = checkThem(bits, index, length) ||  checkThem(bits, index - 1, length) || checkThem(bits, index-2, length) || checkThem(bits, index-3, length);
			

			bits.at(index) = '0' + change;
			bool before = checkThem(bits, index, length) ||checkThem(bits, index-1, length)  || checkThem(bits, index-2, length) || checkThem(bits, index-3, length);

			count += before - before;
		}

		if (count ) {
			std::cout << "YES" << std::endl;
		}else{
			std::cout << "NO" << std::endl;
		}
	}

}


int main (){
	int test;
	std::cin >> test;
	while (test -- ){
		solve();
	}
}
