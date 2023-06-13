#include <bits/stdc++.h>

using namespace std;

vector<int> vec;

int main(){
	//freopen("input.txt", "r", stdin);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
		
	int n, m;
	cin >> n >> m;
	
	for(int i=0; i<n; i++){
		int tmp;
		cin >> tmp;
		vec.push_back(tmp);
	}
	
	sort(vec.begin(), vec.end());
	
	int left = 0;
	int right = vec.size()-1;
	int ans = 0;
	
	while(left < right){
		int tmp = vec[left] + vec[right];
		
		if (tmp<=m){
			left ++;
		}
		else {
			ans ++;
			left ++;
			right --;
		}
		
	}
	cout << ans;
	return 0;
	
}