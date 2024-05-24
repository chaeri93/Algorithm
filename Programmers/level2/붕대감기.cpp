#include <string>
#include <vector>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int time = attacks.back()[0];
    int recoveryTime = bandage[0];
    int recoveryHealth = bandage[1];
    int recoveryBonus = bandage[2];
    int max_health = health;

    int midx = 0;
    int count = 0;
    for (int i = 1; i < time + 1; i++) {
        if (attacks[midx][0] == i) {
            count = 0;
            health -= attacks[midx][1];

            if (health <= 0) return -1;
            if (midx < attacks.size()) {
                midx++;
            }
        }
        else {
            count++;
            health += recoveryHealth;
            if (recoveryTime == count) {
                count = 0;
                health += recoveryBonus;
            }
            if (health > max_health) {
                health = max_health;
            }

        }
    }
    return health;
}