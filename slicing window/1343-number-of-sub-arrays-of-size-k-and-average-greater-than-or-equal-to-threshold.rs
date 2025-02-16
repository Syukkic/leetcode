// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        let mut sum_of_window: i32 = arr[0..k as usize].iter().sum();
        let mut result: i32 = 0;

        if sum_of_window / k >= threshold {
            result += 1;
        }

        for i in (k as usize)..arr.len() {
            sum_of_window += arr[i] - arr[i - k as usize];

            if sum_of_window / k >= threshold {
                result += 1;
            }
        }

        result as i32
    }
}
