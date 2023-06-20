#include<iostream>

using namespace std;

/*
 음수를 배우지 않았고, 20을 넘는 수는 모른다
 왼쪽부터 계산할 때, 중간에 나오는 수가 모두 0 이상 20 이하
 더하기 빼기 등호만 사용  
 ans => 올바른 등식의 개수 
*/

int n; // 숫자의 개수
int arr[100]; 
long long dp[100][21];

int main(){
	//freopen("input.txt","r",stdin);
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> arr[i];
	}
	
	int ans = arr[n-1]; // 나와야하는 숫자
	dp[0][arr[0]] = 1; // 제일 첫번째 숫자는 계산하지 않고 그냥 들어감
	
	for(int i=1; i<n-1; i++){ // i=0은 처리했고 i=n-1은 나와야하는 숫자 
		for (int j=0; j<=20; j++){ // 0부터 20까지의 숫자가 나올 수 있음			
			if(j+arr[i] <=20){
				dp[i][j+arr[i]] += dp[i-1][j];
			}
			if(j-arr[i] >=0){
				dp[i][j-arr[i]] += dp[i-1][j];
			}
		}
		 
	} 
	
	long long cnt;
	cnt = dp[n-2][ans];
	cout << cnt << "\n";

	return 0;
	
}
