class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountain_arr) {
        int n = mountain_arr.length();

        auto locate_peak = [&](this auto& self, int low, int high) -> int {
            if (low == high) return low;
            int mid = low + (high - low) / 2;
            if (mountain_arr.get(mid) < mountain_arr.get(mid + 1)) {
                return self(mid + 1, high);
            }
            return self(low, mid);
        };

        auto search_range = [&](this auto& self, int low, int high, bool ascending) -> int {
            if (low > high) return -1;
            int mid = low + (high - low) / 2;
            int val = mountain_arr.get(mid);
            if (val == target) return mid;
            if ((val < target) == ascending) {
                return self(mid + 1, high, ascending);
            }
            return self(low, mid - 1, ascending);
        };

        int peak = locate_peak(0, n - 1);
        int found = search_range(0, peak, true);
        if (found != -1) return found;
        return search_range(peak + 1, n - 1, false);
    }
};