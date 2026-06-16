class Solution {
public:
    std::string encode(const std::vector<std::string>& strs) {
        std::string res = "";
        for (const std::string& s : strs) {
            res += std::to_string(s.length()) + "#" + s;
        }
        return res;
    }

    std::vector<std::string> decode(const std::string& s) {
        std::vector<std::string> res;
        int i = 0;

        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            int length = std::stoi(s.substr(i, j - i));            
            i = j + 1;
            res.push_back(s.substr(i, length));
            i += length;
        }

        return res;
    }
};