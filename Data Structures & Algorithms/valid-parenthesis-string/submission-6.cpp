class Solution {
public:
    bool checkValidString(string s) {
        vector<int> l = {};
        vector<int> x = {};
        for (int i = 0; i < s.size(); i++){
            if (s[i] == '('){
                l.push_back(i);
            } else if (s[i] == '*'){
                x.push_back(i);
            } else if (s[i] == ')'){
                if (l.size() > 0){
                    l.pop_back();
                } else if (x.size() > 0){
                    x.pop_back();
                } else{
                    return false;
                }
            }
        }
        if (l.size() > x.size()){
            return false;
        }
        for (int i = l.size()-1; i > 0; i--){
            if (l[i] > x[i]){
                return false;
            }
        }
        return true;
        // cout << l[0] << endl;
        // cout << x[0] << endl;
        // // return l <= x;
        // return true;        
    }
};
