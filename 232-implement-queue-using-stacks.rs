// https://leetcode.com/problems/implement-queue-using-stacks

struct MyQueue {
    primary_stack: Vec<i32>,
    auxiliary_stack: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        Self { primary_stack: Vec::new(), auxiliary_stack: Vec::new() }
    }
    
    fn push(&mut self, x: i32) {
        // Enqueue
        // Pushes element x to the back of the queue.
        self.primary_stack.push(x)
    }
    
    fn pop(&mut self) -> i32 {
        // Dequeue
        // Removes the element from the front of the queue and returns it.
        if self.auxiliary_stack.is_empty() {
            while let Some(element) = self.primary_stack.pop() {
                self.auxiliary_stack.push(element)
            }
        }

        self.auxiliary_stack.pop().unwrap()
    }
    
    fn peek(&mut self) -> i32 {
        // Returns the element at the front of the queue.
        if self.auxiliary_stack.is_empty() {
            while let Some(element) = self.primary_stack.pop() {
                self.auxiliary_stack.push(element)
            }
        }

        *self.auxiliary_stack.last().unwrap()
    }
    
    fn empty(&self) -> bool {
        self.primary_stack.is_empty() && self.auxiliary_stack.is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
