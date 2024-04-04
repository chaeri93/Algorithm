#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> &t1, vector<int> &t2) {
    return t1[1] < t2[1];
}

int solution(vector<vector<int>> targets) {
    int answer = 0, e = -1;
    sort(targets.begin(), targets.end(), cmp);
    for (auto t: targets) {
        if (e <= t[0]) {
            answer++;
            e = t[1];
        }
    }
    return answer;
}