// https://leetcode.com/problems/merge-strings-alternately

impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let merged_string_length = word1.len() + word2.len();
        let mut merged_string = String::with_capacity(merged_string_length);
        let mut i = 0;
        let mut j = 0;
        let chars1: Vec<char> = word1.chars().collect();
        let chars2: Vec<char> = word2.chars().collect();

        while i < chars1.len() && j < chars2.len() {
            merged_string.push(chars1[i]);
            merged_string.push(chars2[j]);

            i += 1;
            j += 1;
        }

        if i < chars1.len() {
            merged_string.push_str(&word1[i..]);
        }

        if j < chars2.len() {
            merged_string.push_str(&word2[j..]);
        }

        merged_string
    }
}
