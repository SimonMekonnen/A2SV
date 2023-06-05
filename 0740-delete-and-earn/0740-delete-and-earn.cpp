class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        const int sz = 10001;
        int dp[sz] = {0};
        for(int num:  nums) {
            dp[num] += num;
        }
        
        
        int ans = 0;
        for(int i = 3; i < sz; i++) {
            dp[i] += max(dp[i-2], dp[i-3]);
            ans = max(ans, dp[i]);
        }
        
        return ans;
        
    }
};