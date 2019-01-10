/*
    This program will get list of files from given path and type and then print sorted filenames
*/ 
#include <iostream> 
#include <vector> 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
using namespace std;

int main(void) {
    
    // vector declaration
    vector <string> colour; 
  
    // initialize vector
    colour.push_back("Orange"); 
    colour.push_back("Yellow"); 
    colour.push_back("Blue"); 
    colour.push_back("Red"); 
    colour.push_back("Purple"); 
  
    // print vector before sorting
    for (int i=0; i<colour.size(); i++)     
        cout << colour[i] << "\n";  
    
    // in-built sorting functions
    sort(colour.begin(), colour.end());

    cout << "\n";  
    // print vector after sorting
    for (int i=0; i<colour.size(); i++)     
        cout << colour[i] << "\n";  
    
    return 0;
}