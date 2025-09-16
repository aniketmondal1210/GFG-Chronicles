#include <vector>
#include <algorithm>

class Solution {
public:
    void customSort(int phy[], int chem[], int math[], int N) {
        // Create a vector of tuples: (phy, chem, math, original_index)
        std::vector<std::tuple<int, int, int, int>> students;
        for (int i = 0; i < N; i++) {
            students.emplace_back(phy[i], chem[i], math[i], i);
        }

        // Custom comparator based on the problem statement
        auto comp = [](const auto &a, const auto &b) {
            if (std::get<0>(a) != std::get<0>(b))
                return std::get<0>(a) < std::get<0>(b); // Physics ascending
            if (std::get<1>(a) != std::get<1>(b))
                return std::get<1>(a) > std::get<1>(b); // Chemistry descending
            return std::get<2>(a) < std::get<2>(b);     // Math ascending
        };

        // Sort students vector with custom comparator
        std::sort(students.begin(), students.end(), comp);

        // Update the original arrays according to the sorted order
        for (int i = 0; i < N; i++) {
            phy[i] = std::get<0>(students[i]);
            chem[i] = std::get<1>(students[i]);
            math[i] = std::get<2>(students[i]);
        }
    }
};
