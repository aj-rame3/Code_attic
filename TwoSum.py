class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
 
        unordered_map<int, int> hash;              // [11, 8, 4, 6, 9, 20, 15]
        vector<int> result;
        for (int i = 0 ; i < nums.size(); i++){  // run the loop till end of nums
            int numtofind = target - nums[i];    // find the second number
            if(hash.find(numtofind) != hash.end()){   // find second number in hash
                result.push_back(hash[numtofind]);   //put the hash value and index i in result
                result.push_back(i);                
                return result;
            }
            
            hash[nums[i]] = i;    //hash[number pointed by index of nums] = index   e.g hash[6] = 3
        }
        return result;
    }
};
