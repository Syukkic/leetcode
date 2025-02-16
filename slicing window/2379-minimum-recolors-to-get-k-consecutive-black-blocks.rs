// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let n = blocks.len();
        let k = k as usize;
        let blocks: Vec<char> = blocks.chars().collect();

        let mut white_count = blocks.iter().take(k).filter(|&c| *c == 'W').count();
        let mut min_recolor = white_count;
        if min_recolor == 0 {
            return 0;
        }
        for i in 1..=n - k {
            if blocks[i - 1] == 'W' {
                white_count -= 1
            }
            if blocks[i + k - 1] == 'W' {
                white_count += 1;
            }
            min_recolor = min_recolor.min(white_count);
        }

        min_recolor as i32
    }
}
