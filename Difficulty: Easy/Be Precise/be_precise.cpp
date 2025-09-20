#include <iostream>
#include <iomanip> // for std::setprecision and std::fixed

class Solution {
  public:
    void divideAndPrint(float a, float b) {
        float result = a / b;
        std::cout << std::fixed << std::setprecision(3) << result << std::endl;
    }
};
