/*
    This program find time taken by program
*/
#include <iostream>
#include <stdio.h>
#include <time.h>

using namespace std;

void myFunction() {

    for (int i = 0; i < 10000; i++) {
        // cout << "print \n" << i;
    }
}
int main(void) {

    // initialize options
    int options;

    int start_time = clock();
    myFunction();
    int stop_time = clock();

    cout << " time (in milliseconds): " << (stop_time - start_time) << "\n";
    cout << " time (in seconds): " << (stop_time - start_time) / double(CLOCKS_PER_SEC) * 1000 << endl;
}
