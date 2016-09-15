#!/bin/bash

# Check that 3 arguments are given
if [ $# -lt 3 ]; then
    echo "Usage: $0 option pattern filename"
    exit
fi

# Check the given file exists
if [ ! -f $3 ]; then
    echo "Filename given \"$3\" doesn't exist"
fi

case "$1" in
# Count number of lines that match pattern
-i) echo "Number of lines matches with the pattern $2 :"
    grep -c -i $2 $3
    ;;
# Count number of words that match pattern
-c) echo "Number of words matches with the pattern $2 :"
    grep -o -i $2 $3 | wc -l
    ;;
# print all matched lines
-p) echo "Lines that match with the pattern $2 :"
    grep -i $2 $3
    ;;
# Delete all the lines that match pattern
-d) echo "After deleting lines that match pattern $2 :"
    sed -n "/$2/!p" $3
    ;;
*)  echo "Invalid option"
    ;;
esac
