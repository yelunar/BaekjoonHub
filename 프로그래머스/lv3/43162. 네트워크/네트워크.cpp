#include <string>
#include <vector>
#include <queue>

using namespace std;

int visited[201];

int solution(int n, vector<vector<int>> computers) {
    int cnt = 0;
    queue <int> q;
    
    for (int k=0; k<n; k++){
        if (visited[k] == 0){
            cnt ++;
            visited[k] = cnt;
            q.push(k);
        }
    
        while(!q.empty()){
            int cur = q.front();
            q.pop();
            
            for (int i=0; i<n; i++){
                if (computers[cur][i] != 0 && i!=cur){
                    if (visited[i] == 0){
                        visited[i] = cnt;
                        q.push(i);
                    }
                }
            }
            
        }
    }
    
    return cnt;
}