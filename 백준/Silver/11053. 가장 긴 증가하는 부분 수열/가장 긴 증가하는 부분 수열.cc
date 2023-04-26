#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int dp[1001] = { 0,1 };

int arr[1001];

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, ans = 0;

	cin >> N;

	for (int i = 1; i <= N; i++) {

		cin >> arr[i];

		int max = 0;

		for (int j = 1; j <= i; j++)

			if (arr[i] > arr[j] && dp[j] > max)max = dp[j];

		if ((dp[i] = ++max) > ans)ans = dp[i];

	}

	cout << ans << endl;
}
