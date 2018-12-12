/*
    This program will get list of files from given path and type and then print sorted filenames
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

#define MAX_LENGTH          7

char path[] = "/Users/anagesh/Desktop/Ava";
char cset[] = ".xml";

// function prototypes
int c_string_comparator(const void *a, const void *b);
char** get_filenames_from_directory();

int main(void) {
    
    char ** filenamelist = get_filenames_from_directory();
    
    printf("\n***Before sorting***\n\n");
    for(int i=0; i<MAX_LENGTH; i++) {
        printf("%s \n", filenamelist[i]);
    }

    // sort list
    qsort(filenamelist, MAX_LENGTH, sizeof(char *), c_string_comparator);
    
    printf("\n***After sorting***\n\n");    
    for(int i=0; i<MAX_LENGTH; i++){
        printf("%s \n", filenamelist[i]);
    }
    
    free(filenamelist);
    return 0;
}

int c_string_comparator(const void *a, const void *b) {
    
    const char **aptr = (const char **)a;
    const char **bptr = (const char **)b;

    return strcmp(*aptr, *bptr);
}

char ** get_filenames_from_directory() {
    
    int i = 0;
    char **filenames = (char**)malloc(MAX_LENGTH*sizeof(char*));
    for(i = 0; i < MAX_LENGTH; i++){
        filenames[i] = (char*)malloc(50*sizeof(char));
    }

    // Pointer for directory entry 
    struct dirent *de;  

    // opendir() returns a pointer of DIR type.  
    DIR *dr = opendir(path); 
  
    // opendir returns NULL if couldn't open directory 
    if (dr == NULL) { 
        printf("Could not open current directory" ); 
        return 0; 
    } 
  
    i = 0;

    // loop through directory and sub-directory
    while ((de = readdir(dr)) != NULL) {
        
        // store current filename
        char *filename = de->d_name; 
        
        // check regular file and actual file set 
        if( (de->d_type == 8) && (i<MAX_LENGTH) && (strstr(filename, cset) != NULL) ) { 
            // printf("%s\n", de->d_name);
            strcpy(filenames[i++], filename);
        }
    }

    closedir(dr);

    return filenames;
}