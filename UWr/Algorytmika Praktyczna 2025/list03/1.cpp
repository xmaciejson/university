#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<long long> nums(N); 
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    int blockSize = sqrt(N);
    vector<long long> blockSum(blockSize + 1, 0); 

    for (int i = 0; i < N; i++) {
        blockSum[i / blockSize] += nums[i];
    }

    while (Q--) {
        int z, a, b;
        cin >> z >> a >> b;

        if (z == 1) {
            a--;
            int blockIndex = a / blockSize;
            long long difference = b - nums[a]; 
            nums[a] = b;
            blockSum[blockIndex] += difference;
        } else {
            a--;
            b--;
            long long sum = 0; 
            int leftBlock = a / blockSize;
            int rightBlock = b / blockSize;

            if (leftBlock == rightBlock) {
                for (int i = a; i <= b; i++) {
                    sum += nums[i];
                }
            } else {
                for (int i = a; i < (leftBlock + 1) * blockSize; i++) {
                    sum += nums[i];
                }

                for (int i = leftBlock + 1; i < rightBlock; i++) {
                    sum += blockSum[i];
                }

                for (int i = rightBlock * blockSize; i <= b; i++) {
                    sum += nums[i];
                }
            }

            cout << sum << endl;
        }
    }

    return 0;
}