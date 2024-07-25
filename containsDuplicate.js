//
// QUESTION no- 219
// METHODS- Sliding Window, Hash Table, Map
//
var containsNearbyDuplicate = function(nums, k) {

    const hasmap = new Map();
    for (let idx = 0; idx < nums.length; idx++) {
        // Check if the difference betweend duplicates is less than k
        if (idx - hasmap.get(nums[idx]) <= k) {
            return true;
        }
        hasmap.set(nums[idx], idx);
    }
    return false;
};
