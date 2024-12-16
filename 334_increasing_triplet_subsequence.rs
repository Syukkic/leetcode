// https://leetcode.com/problems/increasing-triplet-subsequence

impl Solution {
    // Greedy algorithm
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        if nums.len() < 3 {
            return false;
        }

        let mut smallest = i32::MAX;
        let mut middle = i32::MAX;

        for &num in &nums {
            if num <= smallest {
                smallest = num;
            } else if num <= middle {
                middle = num;
            } else {
                return true;
            }
        }

        false
    }
}
