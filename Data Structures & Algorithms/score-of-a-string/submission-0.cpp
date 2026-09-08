#include <string>
#include <stdlib.h>
class Solution {
public:
    int scoreOfString(string s) {
        // cout << s[0] << endl;
        int total = 0;
        for(int i = 0; i < s.length() -1; i++){
            total += abs((int)s[i] - (int)s[i+1]);

        }
        cout << total;
        return total;
    }

    // return int 1;

};