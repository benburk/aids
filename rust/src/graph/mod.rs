use std::collections::HashMap;

mod dfs;
mod topological_sort;

pub type Graph<T> = HashMap<T, Vec<T>>;