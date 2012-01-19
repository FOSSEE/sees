for i in *.mp3
do 
  mv $i `echo $f|tr -s " " "-"|cut -d - -f 2-`
done
