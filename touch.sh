org="origin"
counter=0

while [ $counter -lt 150 ];
do
    touch $org/"me$counter"
    let counter=counter+1
done
