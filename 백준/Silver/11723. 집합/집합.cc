#include <iostream>
#include <string>
using namespace std;
 
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    unsigned int s = 0;
    int m, n;
    string a ="";
    cin >> m;
    while(m--){
        cin >> a;
        if(a=="add"){
            cin >> n;
            s |= (1 << n);
        }else if(a == "remove"){
            cin >> n;
            s &= ~(1 << n);
        }else if(a== "check"){
            cin >> n;
            if(s & (1<<n)){
                cout << 1 << '\n';
            }else{
                cout << 0 << '\n';
            }
        }else if(a=="toggle"){
            cin >> n;
            s ^= (1<<n);
        }else if(a=="all"){
            s = (1 << 21) - 1;
        }else if(a == "empty"){
            s = 0;
        }
    }
    return 0;
}