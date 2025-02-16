// https://leetcode.com/problems/product-of-array-except-self

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut anwser = vec![1; n];

        // Left products
        for i in 1..n {
            anwser[i] = anwser[i - 1] * nums[i - 1];
        }

        // Right products
        let mut right_product = 1;
        for i in (0..n).rev() {
            anwser[i] *= right_product;
            right_product *= nums[i];
        }

        anwser
    }
}
