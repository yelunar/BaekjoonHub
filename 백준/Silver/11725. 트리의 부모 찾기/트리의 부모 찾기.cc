#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

/*

*/
int n;
int arr[100001];
bool visited[100001];
vector<int> tree[100001];

void dfs(int x){
	visited[x] = true;
	for (int i=0; i<tree[x].size(); i++){
		int next = tree[x][i];
		if (!visited[next]){
			arr[next] = x;
			dfs(next);
		}
	}
}


int main(){
	cin >> n;
	
	for (int i=0; i<n; i++){
		int a, b;
		cin >> a >> b;
		tree[a].push_back(b);
		tree[b].push_back(a);
		
	}
	dfs(1);
	
	for (int i=2; i<=n; i++){
		cout << arr[i]<< "\n";
	}
}

