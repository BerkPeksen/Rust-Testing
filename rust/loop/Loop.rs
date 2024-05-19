

use std::time::{Instant};

fn main() {
    let start_time = Instant::now();
    
    let mut count = 0;
    for _ in 0..200_000_000 {
        count+=1;
        
    }

    let elapsed_time = start_time.elapsed();
    println!("Time taken: {:?} to count: {:?} ", elapsed_time,count);
}