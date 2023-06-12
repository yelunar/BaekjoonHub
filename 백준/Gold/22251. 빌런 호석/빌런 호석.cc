/*
1층부터 N층까지 이용이 가능한 엘리베이터
K자리수, 0-9짜리 숫자가 디스플레이에 보임  

호석이는 LED 중에서 최소 1개, 최대 P개를 반전시킬 계획
반전이란 켜진 부분은 끄고, 꺼진 부분은 켜는 것을 의미
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int arr[10][10] = {
	{1,1,1,1,1,1,0},
	{0,1,1,0,0,0,0},
	{1,1,0,1,1,0,1},
	{1,1,1,1,0,0,1},
	{0,1,1,0,0,1,1},
	{1,0,1,1,0,1,1},
	{1,0,1,1,1,1,1},
	{1,1,1,0,0,0,0},
	{1,1,1,1,1,1,1},
	{1,1,1,1,0,1,1}
};

int n, k, p, x; // 층수, 자리수, 반전가능 최대 수, 현재 층수 

int func(){
	int ans = 0;
	
	for (int i= 1; i <= n; i++){ // 1층부터 n층까지 바꿀 수 있는 층 파악한다 
		if (i==x)
			continue; // 현재 층 나오면 패스 
			
		int cnt = 0; // 바꾼 디스플레이 개수 
		int start = x; // 현재층 
		int end = i; // 바꾸고 싶은 층 
		
		for (int j = 0; j<k; j++){ // k자리수까지 검사 
			for(int m=0; m<7; m++){ // 숫자 하나당 몇개 바꿔야하는지 세줌 
				if(arr[start%10][m] != arr[end%10][m]) cnt ++; 
			}
			start /= 10; // 자리수 바꿔줌 
			end /= 10;
		}
		if (cnt <= p) ans ++; // p번 이하로 바꿨으면 답 +1 
	} 
	return ans;
} 

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> k >> p >> x;
	cout << func() << "\n";
	
    return 0;
}