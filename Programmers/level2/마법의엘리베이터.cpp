#include <string>
#include <vector>

using namespace std;

int solution(int storey) {
    int answer = 0;
    int n;
    while (storey != 0) {
        n = storey % 10;
        
        if (n>=6 || n==5 && (storey / 10) % 10 >= 5) {
            storey += 10 - n;
            answer += 10 - n;
        }
        else {
            answer += n;
        }
        storey = storey / 10;
    }
    return answer;
}
