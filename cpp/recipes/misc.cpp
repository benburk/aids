#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <iostream>
#include <string>
#include <array>

int main() {
    // construct a vector and print it
    std::vector<int> arr = {1, 2, 3};
    for (auto c : arr) {
        std::cout << c << " ";
    }
    std::cout << std::endl;

    // construct an array
    std::array<int, 3> arr2 = {1, 2, 3};
}