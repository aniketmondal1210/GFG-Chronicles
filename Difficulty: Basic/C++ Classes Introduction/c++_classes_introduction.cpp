#include <iostream>
#include <string>
#include <cctype>  // For tolower()

using namespace std;

class CollegeCourse {
    private:
        string courseID;
        char grade;
        int credits;
        int gradePoints;
        float honorPoints;

    public:
        // Set course ID
        void set_CourseId(string CID) {
            courseID = CID;
        }

        // Set grade and calculate grade points
        void set_Grade(char g) {
            grade = toupper(g); // Convert grade to uppercase to handle case insensitivity
            gradePoints = calculateGradePoints(grade); // Calculate grade points
        }

        // Set credits
        void set_Credit(int cr) {
            credits = cr;
        }

        // Calculate grade points based on grade
        int calculateGradePoints(char g) {
            switch (g) {
                case 'A': return 10;
                case 'B': return 9;
                case 'C': return 8;
                case 'D': return 7;
                case 'E': return 6;
                case 'F': return 5;
                default: return 0; // For invalid grade, though the problem ensures valid grades
            }
        }

        // Calculate honor points as the product of grade points and credits
        float calculateHonorPoints(int gp, int cr) {
            return gp * cr;
        }

        // Display grade points and honor points
        void display() {
            honorPoints = calculateHonorPoints(gradePoints, credits);
            cout << gradePoints << " " << honorPoints << endl;
        }
};
