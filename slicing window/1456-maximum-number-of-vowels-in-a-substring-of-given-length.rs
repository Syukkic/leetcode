//https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let s_vec: Vec<char> = s.chars().collect();
        let k = k as usize;
        let mut answer = 0;
        let mut vowel = 0;

        for (i, c) in s_vec.clone().into_iter().enumerate() {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                vowel += 1;
            }

            if i < k - 1 {
                continue;
            }

            answer = answer.max(vowel);

            // remove foreleft element of window
            let out = s_vec[i + 1 - k];
            if out == 'a' || out == 'e' || out == 'i' || out == 'o' || out == 'u' {
                vowel -= 1;
            }
        }
        answer
    }
}
