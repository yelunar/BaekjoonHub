#include <iostream>

using namespace std;

int main() {
    // freopen("input.txt", "r", stdin); // 입력 파일 사용시 주석 해제
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, x;
    
    cin >> n >> x; // 방문자 수와 기간 입력
    
    int arr[250000];
    for (int i = 0; i < n; i++) {
        cin >> arr[i]; // 방문자 수 입력
    } 
    
    long long sum = 0;
    long long max_length = 0;
    long long max_value = 0;
    
    // 초기 기간의 합과 최대값 초기화
    for (int i = 0; i < x; i++) {
        sum += arr[i]; // 누적합 계산
    }
    max_value = sum;
    max_length = 1;
    
    // 기간을 한 칸씩 옮겨가며 최대값을 찾음
    for (int i = x; i < n; i++) {
        sum += arr[i]; // 다음 칸의 값 더하기
        sum -= arr[i - x]; // 기간에서 가장 먼저 들어온 값 빼기
        
        if (sum > max_value) { // 새로운 최대값인 경우
            max_value = sum;
            max_length = 1;
        } else if (sum == max_value) { // 기존 최대값과 같은 경우
            max_length++;
        }
    } 
    
    if (max_value != 0) { // 최대값이 0이 아닌 경우
        cout << max_value << "\n"; // 최대값 출력
        cout << max_length << "\n"; // 최대값을 가지는 기간 수 출력
    } else { // 최대값이 0인 경우
        cout << "SAD" << "\n"; // SAD 출력
    }
    
    return 0;
}
