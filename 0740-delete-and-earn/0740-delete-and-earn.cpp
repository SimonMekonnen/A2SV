class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> dp(10000+1);
        for(int num:  nums) {
            dp[num] += num;
        }
        
        
        int ans = 0;
        for(int i = 3; i < dp.size(); i++) {
            dp[i] += max(dp[i-2], dp[i-3]);
            ans = max(ans, dp[i]);
        }
        
        return ans;
        
    }
};