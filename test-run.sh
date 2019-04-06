#!/bin/bash

files="./*"
dirs=()
for filepath in $files; do
    if [ -d $filepath ] ; then
        dirs+=("${filepath}")
    fi
done

for dir in ${dirs[@]}; do
    echo ${dir} testing...
    python3 ${dir}/test_main.py
done
