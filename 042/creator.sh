#!/bin/bash
echo "Enter excercise number: "
read num
mkdir ../$num && cp notes.txt ../$num/notes.txt && cp creator.sh ../$num/creator.sh && cd ../$num && touch ../$num/ex$num.py
