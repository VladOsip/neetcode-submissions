#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(std::string s) {
        int start = 0;
        int end = s.length() - 1;

        while (start < end) {
            while (start < end && !std::isalnum(static_cast<unsigned char>(s[start]))) {
                start++;
            }
            while (start < end && !std::isalnum(static_cast<unsigned char>(s[end]))) {
                end--;
            }

            if (std::tolower(static_cast<unsigned char>(s[start])) != 
                std::tolower(static_cast<unsigned char>(s[end]))) {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }
};
