// https://leetcode.com/problems/implement-stack-using-queues/

use std::collections::VecDeque;

struct MyStack {
    primary_queue: VecDeque<i32>,
    auxiliary_queue: VecDeque<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    fn new() -> Self {
        Self {
            primary_queue: VecDeque::new(),
            auxiliary_queue: VecDeque::new()
        }
    }
    
    fn push(&mut self, x: i32) {
        self.auxiliary_queue.push_back(x);
        while let Some(element) = self.primary_queue.pop_front() {
            self.auxiliary_queue.push_back(element);
        }

        std::mem::swap(&mut self.primary_queue, &mut self.auxiliary_queue);
    }
    
    fn pop(&mut self) -> i32 {
        self.primary_queue.pop_front().unwrap()
    }
    
    fn top(&self) -> i32 {
        *self.primary_queue.front().unwrap()
    }
    
    fn empty(&self) -> bool {
        self.primary_queue.is_empty()
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */