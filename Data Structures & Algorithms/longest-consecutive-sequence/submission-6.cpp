class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int>mpp;
        for(int i : nums){
            mpp[i]++;
        }
        int maxi = 0;
        for(int i = 0; i < nums.size(); i++){
            int val = nums[i];
            int cnt = 1;
            while(mpp.find(val+1) != mpp.end()){
                cnt++;
                val++;
            }
            maxi=max(maxi,cnt);
        }
        return maxi;
    }
};
