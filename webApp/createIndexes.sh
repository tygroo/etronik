createIndex(){
	for ((i=$1; i<=$2; i++))
	do
		pdf2txt.py -p $i $3 >> $4
	done		
}

>index1
>index2
>index3

createIndex 1 1 $1 index1
createIndex 2 8 $1 index2
pdf2txt.py -m 9999 $1 >> index3
 

