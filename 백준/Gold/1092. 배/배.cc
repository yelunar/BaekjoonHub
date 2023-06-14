#include <bits/stdc++.h>

using namespace std;

/*
항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다
모든 크레인은 동시에 움직임
 
ans => 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력
모든 박스를 배로 옮길 수 없으면 -1을 출력
*/

int n, m; 
int ans;

int main(){
	//freopen("input.txt", "r", stdin);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n; // 크레인 n개
	vector<int> crane;
	for(int i=0; i<n; i++){
		int tmp;
		cin >> tmp;
		crane.push_back(tmp);
	}
	sort(crane.begin(), crane.end(), greater<int>());
	
	cin >> m; // 박스 수 m개
	vector<int> box;
	for (int i=0; i<m; i++){
		int tmp;
		cin >> tmp;
		box.push_back(tmp);
	}
	sort(box.begin(), box.end(), greater<int>());
	
	if (crane[0]<box[0]){ // 박스가 최대 크레인보다 크면 아예 담을수가 없음 
		cout << -1 << "\n";
		return 0;
	}
	while (!box.empty()){
		ans ++;
		for (int i=0; i < crane.size(); i++){
			for (int j=0; j < box.size(); j++){
				if (crane[i] >= box[j]){
					box.erase(box.begin()+j); // erase[a,b) a - b 주소 구간에 해당하는 원소 삭제 
					break; 
				}
			}
		//ans ++;
		}
	}
	cout << ans << "\n";
	return 0;

}