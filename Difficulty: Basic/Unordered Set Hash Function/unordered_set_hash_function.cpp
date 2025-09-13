// User function Template for C++

// Complete the function
#include <unordered_set>
#include <string>
using namespace std;

// Complete the function
long int HashMe(unordered_set<string> myset, string str) {

    // Using std::hash to compute hash value of the input string 'str'
    std::hash<string> hash_fn;
    long int hash_value = (long int) hash_fn(str);
    
    return hash_value;
}
