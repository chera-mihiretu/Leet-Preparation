#include <bits/stdc++.h>
#include <vector>

void solve(){
	std::vector<char> color;
	std::vector<std::vector<int>> graph;
	int nodes;
	std::cin >> nodes;
	graph.assign(nodes, {});
	for (int i = 0; i < nodes - 1; i ++){
		int from, to;

		std::cin >> from >> to;

		graph.at(from - 1).push_back(to - 1);
		graph.at(to - 1).push_back(from - 1);
		
		
		
	}



	std::string node_vals;

	std::cin >> node_vals;

	color.assign(node_vals.begin(), node_vals.end());
	
}

int main (){

	int test_case;
	std::cin >> test_case;
	
	while (test_case){
		
		solve();

		test_case -- ;
	}
}
