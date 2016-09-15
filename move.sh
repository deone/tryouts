# Define directories
org="origin"
dest="dest"

# Set counter
counter=0

if [ "$(ls -A $dest 2> /dev/null)" == "" ]; then
    while [ $counter -lt 100 ];
    do
	file=`ls $org | head -1`
	mv $org/$file $dest
	let counter=counter+1
    done
fi
