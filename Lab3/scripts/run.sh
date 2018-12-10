#! bin/env bash

HCopy -A -D -C ../resources/hcopy.conf -S ../resources/hcopy.scp

for file in ../resources/mfcc/*
do
    Hlist $file > $file.txt
done 

python3 main.py