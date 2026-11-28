class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int i = 0;
        int j = static_cast<int>(people.size()) - 1;
        int boatsNeeded = 0;

        while (i <= j) {
            int total = people[i] + people[j];
            if (total <= limit) {
                i++;
            }
            j--;
            boatsNeeded++;
        }

        return boatsNeeded;
    }
};