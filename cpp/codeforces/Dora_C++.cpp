#include <bits/stdc++.h>
#include <vector>
#include <cmath>
#include <algorithm>
void solve(){
	int length, a, b;
	std::vector<int> array;
	std::cin >> length >> a >> b;
	int d = std::gcd(a, b);
	for (int i = 0; i < length; ++i){
		int item;
		std::cin >> item;
		array.push_back(item % d);
	}
	std::sort(array.begin(), array.end());
	int answer = array.at(length - 1) - array.at(0); 
	for (int j = 1; j < length; ++j){
		answer = std::min(answer, ((array.at(j-1) + d) - array.at(j)));
	} 

	std::cout << answer << std::endl;

}

int main (){
	int test_case;
	std::cin >> test_case;
	while (test_case){
		solve();
		test_case -- ;
	}
}
