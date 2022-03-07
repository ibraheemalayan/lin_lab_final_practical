# !/bin/bash

input_file='Student_Record.txt'
output_file='student_state.txt'

if [ ! -e $input_file ];
then;
    echo "\nInput file '$input_file' does not exist !\n"
    exit 1;
fi;

if [ -e $output_file ];
then;
    echo "\n Output file '$output_file' already exists this will overwrite it !\n";
    echo "" > $output_file;
fi;

echo "\n > reading file $input_file ...\n"

cat $input_file | while read line;
do;
    echo " - processing line :  $line ";

    name=`echo $line | cut -d " " -f 1`;

    # remove name field
    line=`echo $line | cut -d " " -f 2-`;
    
    count=0;
    sum=0;

    echo $line | tr " " "\n" | while read mark;
    do;
        count=$(( count + 1 ));
        sum=$(( sum + mark ));
    done;

    avg=$(( sum / count ));

    echo "$name $count $avg" >> $output_file;

done;

