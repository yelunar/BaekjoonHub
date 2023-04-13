/*
input: 첫째 줄에 선을 그은 횟수 N  다음 N개의 줄에는 선을 그을 때 선택한 두 점의 위치 x, y 
output: 그은 선의 총 길이
*/

#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <unordered_map>

using namespace std;
typedef pair<int, int> P;

P arr[1000001]; // 선의 위치 정보를 저장하는 배열
int n, from, to, l, r, ret; // 입력값, 왼쪽 끝, 오른쪽 끝, 결과값을 저장하는 변수
int main() {
	ios_base::sync_with_stdio(false); // C++ 표준 입출력 속도 향상
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n; // 선을 그은 횟수 입력
	for (int i = 0; i < n; i++) {
		cin >> from >> to; // 선을 그을 때 선택한 두 점의 위치 입력
		arr[i] = P(from, to);  // 배열에 저장
	}
	sort(arr, arr + n); // 배열을 시작점 오름차순으로 정렬
	l = arr[0].first; // 첫번째 선 왼쪽 끝 초기화
	r = arr[0].second;  // 첫번째 선 오른쪽 끝 초기화
	for (int i = 1; i < n; i++) {
		if (r < arr[i].first) { // 현재 선의 왼쪽 끝이 이전 선의 오른쪽 끝보다 크면
			ret += (r - l); // 이전 선의 길이를 결과값에 더함
			l = arr[i].first; // 왼쪽 끝 갱신
			r = arr[i].second; // 오른쪽 끝 갱신
		}
		else if (arr[i].first <= r && arr[i].second >= r) { // 현재 선이 이전 선을 포함하면
			r = arr[i].second; // 오른쪽 끝 갱신
		}
	}
	ret += r - l; // 마지막 선의 길이를 결과값에 더함
	cout << ret << '\n';

}