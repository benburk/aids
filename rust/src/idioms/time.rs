use std::time::{SystemTime, UNIX_EPOCH};

/// Gets the current time in microseconds
pub fn current_time_micros() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .expect("Time went backwards")
        .as_micros() as u64
}
