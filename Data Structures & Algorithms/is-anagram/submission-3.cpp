class Solution {
public:
    bool isAnagram(string s, string t) {
        if (t.size() != s.size()){
            return false;
        }
        unordered_map<char,int> map;
        for(char i : s){
            map[i]++;

        }
        for(char j : t){
            if (map.count(j) > 0){
                map[j]--;
                if (map[j] < 0){
                    return false;
                }
            } else {
                return false;
            }
        }

        return true;


    }
};
