#include <bits/stdc++.h>
#include <algorithm>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>



typedef __gnu_pbds::tree<int, __gnu_pbds::null_type, std::less<int>, __gnu_pbds::rb_tree_tag, __gnu_pbds::tree_order_statistics_node_update> pbds;

void solve(){
	int length;
	std::vector<std::pair<int, int>> array;
	pbds ordered_set;	
	std::cin >> length;
	array.assign(length, {});

	for (int i =0; i < length; ++ i ){

		std::cin >> array.at(i).first >> array.at(i).second;
	}

	std::sort(array.begin(), array.end());
	long long answer = 0;
	for (int i = 0; i < length; ++ i ) {
			
		answer += ordered_set.size() - ordered_set.order_of_key(array.at(i).second);
	 
		ordered_set.insert(array.at(i).second);	
	}

	std::cout << answer << std::endl;
	


}

int main(){
	int test_case;
	std::cin >> test_case;
	while (test_case){
		solve();

		test_case -- ;
	}	
}


