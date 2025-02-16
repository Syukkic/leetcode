// https://leetcode.com/problems/maximum-average-subarray-i

impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let mut window_sum: i32 = nums[0..k].iter().sum();
        let mut answer = window_sum;

        for i in k..nums.len() {
            window_sum += nums[i] - nums[i - k];
            answer = answer.max(window_sum);
        }

        answer as f64 / k as f64
    }
}
