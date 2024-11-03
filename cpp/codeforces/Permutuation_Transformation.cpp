#include <bits/stdc++.h>
#include <vector>

void recursion(int depth, int left, int right, std::vector<int> &ans, std::vector<int> &arr){
	if (left == right) return;
	int pick_max = left;
	for(int i = left; i < right; ++i){
		if (arr.at(i) > arr.at(pick_max)){
			pick_max = i;
		}
	}

	ans[pick_max] = depth;

	recursion(depth + 1, left, pick_max, ans, arr);
	recursion(depth + 1, pick_max + 1, right, ans, arr);
}


void solve(){
	int length;
	std::cin >> length;
	std::vector<int> permutation;

	for (int i=0; i < length; ++ i){
		int item;
		std::cin >> item;
		permutation.push_back(item);
	
	}
		
	std::vector<int> answer;
	for (int i = 0; i < length; ++i) answer.push_back(0);
	recursion(0, 0, permutation.size(), answer, permutation);

	for(int i = 0; i < length; ++i) std::cout << answer.at(i) << " ";
	std::cout << std::endl;

	
}

int main(){

	int test_case;
	std::cin >> test_case;

	while (test_case){
		solve();
		test_case --;
	}

}
