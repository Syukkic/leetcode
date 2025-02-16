// https://leetcode.com/problems/is-subsequence

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut s_chars = s.chars();
        let mut current = s_chars.next();

        for c in t.chars() {
            if Some(c) == current {
                current = s_chars.next();
            }
        }

        current.is_none()
    }
}
