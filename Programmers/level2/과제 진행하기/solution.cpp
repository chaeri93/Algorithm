#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(vector<string> &t1, vector<string>&t2) {
    return t1[1] < t2[1];
}

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    vector<pair<string,int>> waitTesk;
    sort(plans.begin(), plans.end(), cmp);
    int time = 0;
    for (auto plan: plans) {
        int new_time = 60 * stoi(plan[1].substr(0,2)) + stoi(plan[1].substr(3,5));
        while (time < new_time) {
            if (waitTesk.size()>0) {
                waitTesk.back().second--;
                if (waitTesk.back().second == 0) {
                    answer.push_back(waitTesk.back().first);
                    waitTesk.pop_back();
                }
            }
            time++;
        }
        waitTesk.push_back(make_pair(plan[0],stoi(plan[2])));
    }
    while(waitTesk.size()>0){
        answer.push_back(waitTesk.back().first);
        waitTesk.pop_back();
    }
    return answer;
}