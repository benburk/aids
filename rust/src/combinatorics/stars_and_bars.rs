/// Stars and bars algorithm.
/// https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
/// https://stackoverflow.com/a/69140296/9518712
/// Constraints k >= 1
pub fn stars_and_bars(n: u64, k: u64) -> Vec<Vec<u64>> {
    assert!(k > 0);
    let mut result = Vec::new();
    let mut bins = vec![0; k as usize];
    bins[0] = n;
    loop {
        result.push(bins.clone());
        if bins.last().unwrap() == &n {
            return result
        }
        if bins[0] > 0 {
            bins[0] -= 1;
            bins[1] += 1;
        } else {
            let mut i = 1;
            while bins[i] == 0 {
                i += 1;
            }
            bins[0] = bins[i] - 1;
            bins[i + 1] += 1;
            bins[i] = 0;
        }
    }
}