LINECOUNT=`hdfs dfs -cat $1 | wc -l`
echo NumberofLines=$LINECOUNT