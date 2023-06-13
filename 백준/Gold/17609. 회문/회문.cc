#include <bits/stdc++.h> 

using namespace std;

// 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2

int palindrome(string s, int cnt){
	
	int left = 0;
	int right = s.size()-1; // 인덱스는 글자수-1이니까  
	
	while (left < right){
		if (s[left] != s[right]){ 
			
			if (cnt == 0){ // 아직 지워진 문자가 없을 때 
				
				int length = right - left;
				// 현재 문자열에서 왼쪽 문자를 지우거나 오른쪽 문자를 지웠을 때 회문인지 확인
				if (palindrome(s.substr(left+1, length),1) == 0 || palindrome(s.substr(left, length),1) == 0) return 1;
				else return 2;
			}
		else return 2; // 이미 문자가 지워진 상태에서 다른 문자가 다를 경우
		}
		
		left ++;
		right --;
	}
	return 0; // 회문인 경우
}


int main(){
	// freopen("input.txt", "r", stdin);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int t; // 문자열의 개수
	cin >> t;
	
	for(int i=0; i<t; i++){
		string s;
		cin >> s;
		cout << palindrome(s, 0) << "\n";
			
	}
	return 0;
}