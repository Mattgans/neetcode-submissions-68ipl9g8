class Solution {
public:
    bool winnerOfGame(string colors) {
        int count_a = 0;
        int count_b = 0;
        for (int i = 1; i < colors.size()-1; i++){
            if (colors[i] == 'A'){
                if (colors[i-1] == 'A' && colors[i+1] == 'A'){
                    count_a++;
                }
            }
            
            if (colors[i] == 'B'){
                if (colors[i-1] == 'B' && colors[i+1] == 'B'){
                    count_b++;
                }
            }
        }
        if (count_a > count_b){
            return true;
        } else{
            return false;
        }
    }
};
