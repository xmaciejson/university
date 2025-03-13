#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N, Q;
    cin >> N >> Q;
    vector<int> nums(N);
    vector<int> prefix(N+1, 0);
    for (int i=0; i<N; i++){
        cin >> nums[i];
    }

    for (int i=1; i<=N; i++){
        prefix[i] = prefix[i - 1] + nums[i - 1]; 
    }
    
    while (Q--){
        int z, a, b;
        cin >> z >> a >> b;

        if (z == 1){
            int difference = b - nums[a - 1];
            nums[a - 1] = b;

            for (int i=a; i<=N ; i++){
                prefix[i] += difference;
            }
        }
        else{
            cout << prefix[b] - prefix[a - 1] << endl;
        }
    }
    return 0;
}