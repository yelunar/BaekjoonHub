/*
무승부가 발생할 경우 경기 진행 순서상 뒤인 사람이 이긴 것으로 간주
이전 경기의 승자와 이전 경기에 참여하지 않은 사람이 경기를 진행해 승자를 결정한
특정 사람이 미리 합의된 승수를 달성할 때 까지 반복
합의된 승수를 최초로 달성한 사람이 우승

2 일 경우에는 i번 손동작이 j번 손동작을 이긴다는 의미이고, 1일 경우에는 비긴다는 의미이고, 0일 경우에는 진다
*/

#include <bits/stdc++.h>
using namespace std;

int arr[9][9];
int b[20], c[20];
vector<vector<int>> vec(3);

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, k;
	cin >> n >> k;

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			cin >> arr[i][j]; // 상성에 대한 정보

	for (int i = 0; i < 20; ++i) {
		int num; cin >> num;
		vec[1].push_back(num - 1);
	}
	for (int i = 0; i < 20; ++i) {
		int num; cin >> num;
		vec[2].push_back(num - 1);
	}

	for (int i = 0; i < n; ++i)
		vec[0].push_back(i);

	bool select = false;
	do {

		int p1 = 0; // p3은 참가안함
		int p2 = 1;
		vector<int> win = { 0,0,0 };
		vector<int> idx = { 0,0,0 };

		while (1) {

			if (p1 > p2) swap(p1, p2);

			if (idx[p1] >= vec[p1].size()) break;
			if (idx[p2] >= vec[p2].size()) break;

			int P1 = vec[p1][idx[p1]];
			int P2 = vec[p2][idx[p2]];

			idx[p1] += 1;
			idx[p2] += 1;

			if (arr[P1][P2] == 2) {
				win[p1] += 1;
				p2 = 3 - p1 - p2;
			}
			else {
				win[p2] += 1;
				p1 = 3 - p1 - p2;
			}
			if (win[0] >= k) {
				select = true;
				break;
			}

			else if (win[1] >= k || win[2] >= k)
				break;
		}

		if (select)
			break;

	} while (next_permutation(vec[0].begin(), vec[0].end()));

	if (select)
		cout << 1 << "\n"; // 우승
	else
		cout << 0 << "\n"; // 못함

	return 0;
}