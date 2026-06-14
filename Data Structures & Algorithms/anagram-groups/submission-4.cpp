struct ArrayHash {
    std::size_t operator()(const std::array<uint8_t, 26>& arr) const {
        std::size_t h = 0;
        for (uint8_t v : arr) {
            h ^= std::hash<uint8_t>{}(v) + 0x9e3779b9 + (h << 6) + (h >> 2);
        }
        return h;
    }
};

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::array<uint8_t, 26>, std::vector<std::string>, ArrayHash> key_map;
        key_map.reserve(strs.size());

        for (const std::string& str : strs) {
            std::array<uint8_t, 26> count{};
            for (char c : str) {
                count[c - 'a']++;
            }
            key_map[count].push_back(str);
        }

        std::vector<std::vector<std::string>> values;
        values.reserve(key_map.size());
        
        for (auto& pair : key_map) {
            values.push_back(std::move(pair.second));
        }

        return values;
    }
};