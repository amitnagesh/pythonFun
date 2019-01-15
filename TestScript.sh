#!/bin/bash

#path to script and run first shell
./VectorTest.sh

# verify last call was successfull 
if [[ $? -eq 0 ]] 
then
    echo "Success"
else
    echo "Fail"
fi