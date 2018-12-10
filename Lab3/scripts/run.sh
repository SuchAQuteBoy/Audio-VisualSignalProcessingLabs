#! bin/env bash

HCopy -A -D -C ../resources/hcopy.conf -S ../resources/hcopy.scp -T 1

for file in ../resources/mfcc/*
do
    Hlist -r $file > $file.txt
done 
