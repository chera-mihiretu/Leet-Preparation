#include <bits/stdc++.h>
#include <cstdio>
typedef long long mlong;
mlong n;


std::vector<int> answer;

mlong request(mlong start, mlong end){
	end = std::min(end, n);
	mlong req;
	std::cout << "xor " << start << " " << end << std::endl;
	std::cin >> req;
	return req;
}

void divide(mlong start, mlong end){
	
	if (start > end) return;
	if (start == end) {
		answer.push_back(start);
		return;
	}

	mlong mid = start + (end - start) / 2;

	mlong left_query = request(start, mid);
	mlong right_query = request(mid + 1, end);
	
	if (left_query) divide(start, mid);

	if (right_query) divide(mid + 1, end);
}

void solve(){

	std::cin >> n;
	mlong total = request(1, n);

	if (total) {
		divide(1, n);
	}
	else{
		for (int i = 1; i <= n; i <<= 1){
			mlong req = request(i, (i << 1) - 1);
			if (req){
				answer.push_back(req);
				divide(i << 1, n);
				break;
			}
		}
	}


}

int main (){
	int test;
	std::cin >> test;
	while (test -- ){
		answer.clear();
		solve();
		
		std::cout << "ans " <<  answer.at(0) << " " << answer.at(1) << " " <<  answer.at(2) << std::endl;
		std::cout << std::endl;
	} 
}
