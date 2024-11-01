#include <iostream>
#include <vector>

int main (){
	
	int length;
	std::cin >> length;

	std::vector<int> student_report;
	std::vector<int> student_caught;

	for (int i =0; i < length; ++i){
		int item;
		std::cin >> item;
		student_report.push_back(item);
		student_caught.push_back(0);
	}
	
	for (int j =0; j < length; ++j){
		int answer = j;
		std::vector<int> copy_array = student_caught;
		while (copy_array[answer] < 2){
			copy_array[answer] ++;
			answer = student_report.at(answer) - 1;
		}
		std::cout << answer + 1 << std::endl;
		
	}
	 
	return 0;
}
