/// Gets input string from user
pub fn input(msg: &str) -> String {
    let mut stdout = io::stdout().lock();
    stdout.write_all(msg.as_bytes()).unwrap();
    stdout.flush().expect("error: unable to flush stdout");
    let mut buf = String::new();
    io::stdin()
        .read_line(&mut buf)
        .expect("error: unable to read user input");

    if buf.ends_with('\n') {
        buf.pop();
        if buf.ends_with('\r') {
            buf.pop();
        }
    }
    buf
}