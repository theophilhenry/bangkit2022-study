#!/bin/bash

files=$(grep ' jane ' 'list.txt' | cut -d' ' -f 3-)

cd ..

for file in $files; do
    if test -e "$PWD$file"; then
        echo "$PWD$file" >> "scripts/oldFiles.txt" # Because we are outside now cd..
    fi
done

# You can use $HOME aswell