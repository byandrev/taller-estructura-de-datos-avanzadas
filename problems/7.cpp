class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> salida = score;
        vector<string> s(score.size());
        sort(salida.rbegin(), salida.rend());        
        for(int i = 0; i < salida.size(); i++){
            for(int j = 0; j < score.size(); j++){           
                if(salida[i] == score[j]){
                    if(i == 0){
                        s[j] = "Gold Medal";
                    }else if(i == 1){
                        s[j] = "Silver Medal";
                    }else if(i == 2){                        
                        s[j] = "Bronze Medal";
                    }else{
                        s[j] = to_string(i+1);
                    }
                    break;
                }
            } 
        }
        return s;
    }
};

