class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> key_map;

        for (std::string str : strs) {
            std::string my_key(26, '0');
            for (char c : str) {
                my_key[c - 'a'] += 1;
            }
            key_map[my_key].push_back(str);
        }

        std::vector<std::vector<std::string>> values;
        
        for (const auto& value : key_map) {
            values.push_back(value.second); 
        }

        return values;
    }
};