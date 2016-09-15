while read line;
do
    first=`echo $line | cut -d '.' -f 1`
    second=`echo $line | cut -d '.' -f 2`
    third=`echo $line | cut -d '.' -f 3`

    mv $line "$first.$second.$third"
done < $1
