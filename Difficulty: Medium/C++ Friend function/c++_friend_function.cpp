class Solution {
public:
    string check_name(student k) {
        // Add your code here.
        string firstName = k.first_name;
        string lastName = k.last_name;
        
        sort(firstName.begin(), firstName.end());
        sort(lastName.begin(), lastName.end());
        
        if (firstName == lastName) {
            return "ANAGRAM";
        } else {
            return "NOT ANAGRAM";
        }
    }
};
