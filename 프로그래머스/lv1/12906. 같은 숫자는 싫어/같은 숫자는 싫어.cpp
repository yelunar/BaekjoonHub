#include <bits/stdc++.h>

using namespace std;

vector<int> answer;

vector<int> solution(vector<int> arr) {
    
    answer.push_back(arr[0]);
    
    for(int i=1, j=0; i<arr.size(); i++){
        if (arr[i] == answer[j]) continue;
        else {
            answer.push_back(arr[i]);
        }
        j++;
    }
    
    return answer;
    
}