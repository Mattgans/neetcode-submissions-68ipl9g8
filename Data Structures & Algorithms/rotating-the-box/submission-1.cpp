class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        vector<vector<char>> m(boxGrid[0].size(), vector<char>(boxGrid.size(), '.'));
        for(int i = 0; i < boxGrid.size(); i++){
            for (int j = 0; j < boxGrid[0].size(); j++){
                m[j][boxGrid.size() - 1 - i] = boxGrid[i][j];
            }
        }
        for(int col = 0; col < m[0].size(); col++){
            for (int row = m.size()-1; row >= 0; row--){
                if (m[row][col] != '.') continue;
                int grab = row-1;
                while (grab >= 0){
                    if (m[grab][col] == '*') break;
                    if (m[grab][col] == '#'){
                        m[row][col] = '#';
                        m[grab][col] = '.';
                        break;
                    } else {
                        grab--;
                    }
                }
            }
        }
        return m;
    }
};