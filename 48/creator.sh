#!/bin/bash
echo "Enter excercise number: "
read num
prevnum=$num-1
mkdir ../$num &&;
cp notes.txt ../$num/notes.txt &&;
cp creator.sh ../$num/creator.sh &&;
cp -R projects/* ../$num &&;
cd ../$num &&;
mv projects/skeleton/ex$prevnum projects/skeleton/ex$num &&;
mv projects/skeleton/tests/ex$prevnum\_tests.py projects/skeleton/tests/ex$num\_tests.py &&;
touch ../$num/ex$num.py
