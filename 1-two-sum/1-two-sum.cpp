class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> another;
        for (int i = 0 ; i < nums.size(); i ++){
            another.push_back(make_pair(nums[i],i));
           
}
        
        sort(another.begin(),another.end());
        int left = 0;
        int right = nums.size() - 1;
        while (left < right){
            if ((another[left].first + another[right].first)== target){
                return {another[left].second,another[right].second};
            }
            else if (another[left].first + another[right].first > target){
                right -= 1;
            }
            else{
                left += 1;
            }
        }
        return {};
    }
};