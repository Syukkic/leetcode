// https://leetcode.com/problems/range-sum-query-immutable/


// Prefix Sum
// https://en.wikipedia.org/wiki/Prefix_sum
struct NumArray {
    prefix_sum: Vec<i32>,
}

impl NumArray {
    fn new(nums: Vec<i32>) -> Self {
        let mut prefix_sum = vec![0; nums.len() + 1];
        for i in 0..nums.len() {
            prefix_sum[i + 1] = prefix_sum[i] + nums[i];
        }
        Self { prefix_sum }
    }

    fn sum_range(&self, left: i32, right: i32) -> i32 {
        let left = left as usize;
        let right = right as usize;
        self.prefix_sum[right + 1] - self.prefix_sum[left]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */