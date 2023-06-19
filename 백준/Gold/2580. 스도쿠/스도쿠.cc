#include <iostream>
#include <vector>

using namespace std;

int arr[9][9]; // 스토두 저장
vector<pair<int, int>> blank; // 빈칸 위치

bool check_row(int x, int num){
	for (int i=0; i<9; i++){
		if (num == arr[x][i]){
			return false;
		}
	}
	return true;
} 

bool check_col(int y, int num){
	for (int i=0; i<9; i++){
		if (num == arr[i][y]){
			return false;
		}
	}
	return true;
} 


bool check_square(int x, int y, int num) {
    int nx = (x / 3) * 3;
    int ny = (y / 3) * 3;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (num == arr[nx + i][ny + j]) {
                return false;
            }
        }
    }
    return true;
}

void DFS(int cnt){
	if (cnt == blank.size()){
		for (int i=0; i<9; i++){
			for (int j=0; j<9; j++){
				cout << arr[i][j] << " ";
			}
			cout << endl;
		}
		exit(0);
	}
	
	for (int i=1; i<=9; i++){
		int x = blank[cnt].first;
		int y = blank[cnt].second;
		
		if (check_row(x, i) && check_col(y, i) && check_square(x, y, i)){
			arr[x][y] = i;
			DFS(cnt+1);
			arr[x][y] = 0; // 백트래킹 
		}
			
		}
	
}

int main(){
	//freopen("input.txt", "r", stdin);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	 
	for(int i=0; i<9; i++){
		for(int j=0; j<9; j++){
			cin >> arr[i][j];
			if (arr[i][j]==0){
				blank.push_back(make_pair(i, j));				
			}
		}
	}
	
	DFS(0);
	
	return(0);
}