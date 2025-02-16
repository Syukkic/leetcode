// https://leetcode.com/problems/k-radius-subarray-averages

impl Solution {
    pub fn get_averages(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = nums.len();
        let mut average = vec![-1; n];

        if 2 * k as usize + 1 > n {
            return average;
        }

        // 初始窗口计算，计算 nums[0..2k+1]
        let mut sum_of_window: i32 = nums.iter().take(2 * k as usize + 1).sum();
        // 第一个有效中心平均数
        average[k] = sum_of_window / (2 * k + 1) as i32;

        for i in k + 1..=n - k - 1 {
            // 移动窗口
            sum_of_window -= nums[i - k - 1];
            sum_of_window += nums[i + k];
            average[i] = sum_of_window / (2 * k + 1) as i32;
        }

        average
    }
}
