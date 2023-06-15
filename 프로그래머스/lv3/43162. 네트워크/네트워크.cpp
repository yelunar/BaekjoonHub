#include <string>
#include <vector>
#include <queue>

using namespace std;

int visited[201]; 

int solution(int n, vector<vector<int>> computers) {
    int cnt = 0; 
    queue<int> q; 

    for (int k = 0; k < n; k++) {
        if (visited[k] == 0) { // 아직 방문하지 않은 컴퓨터인 경우
            cnt++; // 네트워크 개수 증가
            visited[k] = 1;// 현재 컴퓨터를 방문 체크하고 해당 네트워크 번호로 설정
            q.push(k); // 큐에 현재 컴퓨터를 추가
        }

        while (!q.empty()) { // 큐가 비어있지 않은 동안 반복
            int cur = q.front(); // 큐에서 현재 컴퓨터를 꺼냄
            q.pop();

            for (int i = 0; i < n; i++) {
                if (computers[cur][i] != 0 && i != cur) { // 현재 컴퓨터와 연결된 다른 컴퓨터를 찾음
                    if (visited[i] == 0) { // 아직 방문하지 않은 컴퓨터인 경우
                        visited[i] = 1;// 해당 컴퓨터를 방문 체크하고 현재 네트워크 번호로 설정
                        q.push(i); // 큐에 해당 컴퓨터를 추가하여 다음에 탐색
                    }
                }
            }
        }
    }

    return cnt; // 전체 네트워크 개수 반환
}
