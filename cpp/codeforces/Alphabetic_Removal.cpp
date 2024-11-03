#include <bits/stdc++.h>

#include <unordered_map>
#include <algorithm>

int main(){
	int length, k;
	std::cin >> length >> k;

	std::string str;
	std::cin >> str;
	std::unordered_map<char, int> map;
	for (int i=0; i < length; ++ i) {
		if (map.find(str[i]) != map.end()){
			map[str[i]] ++;
		}else{
			map[str[i]] = 1;
		}
	}	

	int start = static_cast<int>('a'), end = static_cast<int>('z');

	for (int iterate = start; iterate <= end; ++iterate){
		char current = static_cast<char>(iterate);
		
		if(k > 0){
			if (map.find(current) != map.end()){
				if (map[current] > k){
					map[current] -= k;
					k = 0;
				}else{
					k -= map[current];
					map[current] = 0;
				}
			}
		}
	}


	std::string answer = "";

	for (int i = length - 1; i >= 0; --i){	
		if(map[str[i]] > 0) {
			// std::cout << str[i] << "Count " << map[str[i]] << "Index" << i << std::endl;
			answer += str[i];
			map[str[i]] --;		
		} 
		
	}
	
	// std::cout << answer << std::endl;
	std::reverse(answer.begin(), answer.end());

	std::cout << answer << std::endl;
}

