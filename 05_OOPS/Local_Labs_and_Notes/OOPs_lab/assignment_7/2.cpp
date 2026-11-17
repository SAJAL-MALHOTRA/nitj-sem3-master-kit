#include <iostream>
using namespace std;

int main() {
    int N = 6; 
    int M = 3; 
    int K = 2; 

    cout << "Number of students (N): " << N << endl;
    cout << "Number of subjects (M): " << M << endl;
    cout << "Group size (K): " << K << endl;

    // Dynamically allocating N x M matrix using pointers and new operator
    int** marks = new int*[N];
    for (int i = 0; i < N; i++) {
        marks[i] = new int[M];
    }

    // Sample marks data for 6 students 
    int sampleMarks[6][3] = {
        {80, 85, 90}, 
        {92, 88, 95}, 
        {75, 70, 80}, 
        {88, 90, 86}, 
        {95, 96, 98}, 
        {82, 84, 80}  
    };

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            marks[i][j] = sampleMarks[i][j];
        }
    }

    int* totals = new int[N]; //dynamic array

    cout << "Student Marks Matrix and Total Scores " << endl;
    for (int i = 0; i < N; i++) {
        totals[i] = 0;
        cout << "Student " << (i + 1) << " marks: [ ";
        for (int j = 0; j < M; j++) {
            cout << marks[i][j] << " ";
            totals[i] += marks[i][j];
        }
        cout << "] -> Total: " << totals[i] << endl;
    }

    cout << "Highest Total :" << K << " ===" << endl;
    int groupNum = 1;
    for (int i = 0; i < N; i += K) {
        int bestStudent = i;
        int maxTotal = totals[i];
        int end = (i + K < N) ? (i + K) : N;

        for (int j = i + 1; j < end; j++) {
            if (totals[j] > maxTotal) {
                maxTotal = totals[j];
                bestStudent = j;
            }
        }
        cout << "Group " << groupNum++ << " (Students " << (i + 1) << " to " << end << "): "
             << "Student " << (bestStudent + 1) << " with Highest Total = " << maxTotal << endl;
    }

    for (int i = 0; i < N; i++) {
        delete[] marks[i];
    }
    delete[] marks;
    delete[] totals;
    marks = nullptr;
    totals = nullptr;

    cout << "Entire matrix and totals successfully deallocated row by row." << endl;

    return 0;
}
