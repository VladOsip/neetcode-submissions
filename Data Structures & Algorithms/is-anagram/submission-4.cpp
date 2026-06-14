class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.length() != t.length()) return false;

        std::vector<int> countS(26,0);
        std::vector<int> countT(26,0);
        for (int i = 0; i < s.length(); i++){
            countS[s[i] - 'a']+=1;
            countT[t[i] - 'a']+=1;
        }
        return (countS == countT); 
    }
};
