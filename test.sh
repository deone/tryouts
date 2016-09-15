. $(pwd)/vars

echo $TEST
A=$PTH/indio.py
echo $A
BASEDIR=$(dirname $0)
echo $BASEDIR

date=`date +%B" "%Y`
echo $date

if [ "$OSTYPE" == "darwin13" ]; then
    echo "Yes"
fi

echo $@

if date -v -1m > /dev/null 2>&1; then
    DATE=`date -v -1m +%B`
else
    DATE=`date +%B -d last-month`
fi

echo "This ->" $DATE

year=`date +%Y`
month_number=`date -v -1m +%m`

if [ "$month_number" == "12" ]; then
    year=`date -v -1y +%Y`
fi

echo $year

echo ${year}${month_number}

a="bbb"
eval $a="ccc"
echo $bbb

d="me"
e="you"$d
echo $e

flag="-v -1d"
date $flag +"%Y%m"
