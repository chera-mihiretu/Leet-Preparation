#include <bits/stdc++.h> 
#include <vector>

int solve(){
	
	int n, k;
	std::vector<std::pair<int, int>> array;
	std::unordered_map<int, int> map;
	std::cin >> n >> k;
	array.assign(k, {});
	int res = 0;
	
	for (int i = 0; i < k;++ i){
		std::cin >> array.at(i).first >> array.at(i).second;
		if (map.find((array.at(i).first)) != map.end()){
			map[array.at(i).first] += 0;
		
		}
		map[array.at(i).first] += array.at(i).second;
	}


	std::vector<int> answer;

	for (auto map_val : map){
		answer.push_back(map_val.second);
	}

	std::sort(answer.begin(), answer.end());
	std::reverse(answer.begin(), answer.end());
	
	for (int i =0; i < n; ++i) {
		if (i >= answer.size()) break;
		res += answer.at(i);
	}


	return res;


}

int main (){
	int test;
	std::cin >> test;
	while (test -- ) {
		std::cout << solve() << std::endl;
	}
}
