#createIndex(){
#        for ((i=$1; i<=$2; i++))
#        do
#                pdf2txt.py -p $i $3 >> $4
#        done            
#}

#>index1
#>index2
#>index3
#>notice
#>noticetmp

#createIndex 1 1 $1 index1
#createIndex 2 8 $1 index2
#pdf2txt.py -m 9999 $1 >> index3
#pdf2txt.py -p1 -t tag $1 >> noticetmp
echo $1
#xsltproc --param name "'${1}'" notice.xslt noticetmp >> notice
#rm noticetmp