#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

class TimeMap {
private:
    // Store pairs of {timestamp, value} for each key
    std::unordered_map<std::string, std::vector<std::pair<int, std::string>>> store;

public:
    TimeMap() {}
    
    void set(std::string key, std::string value, int timestamp) {
        store[key].push_back({timestamp, value});
    }
    
    std::string get(std::string key, int timestamp) {
        if (store.find(key) == store.end()) {
            return "";
        }
        
        const auto& history = store[key];
        
        // Target pair for upper_bound (we only care about comparing the timestamp)
        std::pair<int, std::string> target = {timestamp, ""};
        
        // Find the first element strictly greater than the target timestamp
        auto it = std::upper_bound(history.begin(), history.end(), target, 
            [](const std::pair<int, std::string>& a, const std::pair<int, std::string>& b) {
                return a.first < b.first;
            });
        
        // If it points to the beginning, all timestamps are greater than the requested one
        if (it == history.begin()) {
            return "";
        }
        
        // Step back one element to get the largest timestamp <= requested timestamp
        return std::prev(it)->second;
    }
};