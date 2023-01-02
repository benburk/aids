use std::{collections::HashSet, hash::Hash};

const SIZE: usize = 9;

fn contains_duplicates<T: Eq + Hash>(slice: impl Iterator<Item = T>) -> bool {
    let mut set = HashSet::new();
    for item in slice {
        if !set.insert(item) {
            return true;
        }
    }
    false
}

struct Sudoku {
    grid: [u8; SIZE * SIZE],
}

impl Sudoku {
    fn rows(&self) -> impl '_ + Iterator<Item = impl Iterator<Item = &u8>> {
        self.grid.chunks(SIZE).map(|row| row.iter())
    }

    fn cols(&self) -> impl '_ + Iterator<Item = impl Iterator<Item = &u8>> {
        (0..SIZE).map(move |col| self.grid[col..].iter().step_by(SIZE))
    }

    fn squares(&self) -> impl '_ + Iterator<Item = impl Iterator<Item = &u8>> {
        (0..SIZE).map(move |square| {
            let x = (square / 3) * 3 * SIZE + (square % 3) * 3;
            let y = x + SIZE;
            let z = y + SIZE;
            let a = self.grid[x..square + 3].iter();
            let b = self.grid[y..y + 3].iter();
            let c = self.grid[z..z + 3].iter();
            a.chain(b.chain(c)).into_iter()
        })
    }

    fn is_valid(&self) -> bool {
        !self.rows().any(contains_duplicates)
            && !self.cols().any(contains_duplicates)
            && !self.squares().any(contains_duplicates)
    }
}

fn is_valid(grid: &[[char; 9]; 9]) -> bool {
    let mut rows: [HashSet<char>; 9] = Default::default();
    let mut cols: [HashSet<char>; 9] = Default::default();
    let mut squares: [HashSet<char>; 9] = Default::default();
    for i in 0..9 {
        for j in 0..9 {
            let c = grid[i][j];
            if c == '.' {
                continue;
            }
            let square = (i / 3) * 3 + j / 3;
            if !rows[i].insert(c) || !cols[j].insert(c) || !squares[square].insert(c){
                return false;
            }
        }
    }
    true
}

#[cfg(test)]
mod test {

    #[test]
    fn test_flags() {
        assert_eq!(true, true);
    }
}
