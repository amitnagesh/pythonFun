#!/bin/bash

#compile and create .o file
g++ VectorSorting.cpp -o VectorSorting.o

#execute file
./VectorSorting.o

#validate
if [[ $? -eq 0 ]] 
then
    echo "Success"
else
    echo "Fail"
fi