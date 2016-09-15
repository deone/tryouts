#/bin/bash

while read line
    do
	awk '($7 == "")' $@ >> new.txt
    done
