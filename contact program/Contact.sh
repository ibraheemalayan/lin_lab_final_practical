#!/usr/bin/bash

# Project Lab Linux                                     thats me : Hammam khaled      1191081
#                                                       Partner  : Ibraheem Elilean   1201180   
#=============================== FUNCTIONS ================================================

verify_phone() {
        read -p 'Enter phone: ' phone
        re1="^[0-9]+$"                          #to check if its just numbers
        if  ! [[ "$phone" =~ $re1 ]]
        then
          echo -e "__Error__ -> Enter just numbers \n"
          verify_phone
        fi
        if test -z "$phone"
        then
          echo "__Error__ -> you can't left phone NULL"
          verify_phone
        fi
        num_of_digits=${#phone}                 # ${#phone} => the number of digits
        if  [ "$num_of_digits" -ne 10 ]
        then
                echo "__Error__ -> Invalid number"
                verify_phone
        else
                echo "    [✓] valid phone"
        fi
}



verify_email() {
           read -p 'Enter email: ' email
           re="^[0-9a-zA-Z.]+\@[a-zA-Z]+\.[a-z]{1,10}$"
          if [[ $email =~ $re ]]; then
            echo "    [✓] valid email"
          else
           echo "NOT valid."
           verify_email
          fi
 }


check_file(){
        read -p 'contact_file: ' file
        FILE="./$file"
        if [ -f "$FILE" ]; then         #CHECK if the file exist
                echo "  {$file} exists."
        else
                echo "  {$FILE} does not exist."
                check_file
        fi
}

save_contact(){
        echo "$f_name ,$l_name, $phone, $email" >> $FILE
        echo "|===> $f_name, $l_name, $phone , $email  __ has been added"
}

read_first_name(){
        read -p 'first name: ' f_name
        if test -z "$f_name"
        then
          echo "you can't left first name NULL"
          read_first_name
        fi
}

add_new_contact(){
        echo -e "\n |--------Add New Contact ------|\n "
        read_first_name
        read -p 'last name: ' l_name
        verify_phone
        verify_email
        #to save this new contact to the file
        save_contact
}

list(){
        echo -e "|-> list based on \n\t1)First Name \n\t2)Last Name"
        read -p 'Enter number:' base
        case "$base" in
        1)
          sort -t','  $FILE;;
        2)
          sort -t',' -k2 $FILE;;
        *)
         sort $FILE
        esac
}

search(){
        echo "|->  search for contact with name"
        read -p 'First name to search: ' searched_f_name
        read -p 'Second name to search: ' searched_l_name
        echo -e "\n"
        egrep "\<$searched_f_name ,$searched_l_name\>" $FILE
}

update(){
        #update specific meaning and save it
        echo -e "What you want to update: \n\t1)First Name \n\t2)Last Name \n\t3)Phone\n\t4)Email"
        read -p 'Enter number of choice:' num_to_change
        case "$num_to_change" in
        1)
          read -p 'Enter first name: ' search
          read -p 'Enter new first name: ' replace
          if [[ $search != "" && $replace != "" ]]; then
            sed -i "s/$search/$replace/" $FILE
          fi;;
        2)
          read -p 'Enter last name: ' search
          read -p 'Enter new last name: ' replace
          if [[ $search != "" && $replace != "" ]]; then
            sed -i "s/$search/$replace/" $FILE
          fi;;
        3)
          read -p 'Enter phone: ' search
          read -p 'Enter new phone: ' replace
          if [[ $search != "" && $replace != "" ]]; then
            sed -i "s/$search/$replace/" $FILE
          fi;;
        4)
          read -p 'Enter Email: ' search
          read -p 'Enter new Email: ' replace
          if [[ $search != "" && $replace != "" ]]; then
            sed -i "s/$search/$replace/" $FILE
          fi
          ;;
        *)
          update
        esac
}


delete(){
        read -p 'Enter first  name of contact to delete:' first_to_delete
        read -p 'Enter second name of contact to delete:' second_to_delete
        sed "/$first_to_delete ,$second_to_delete/d" -i $FILE
}

menu(){

        echo -e "\n\n\t|--<><><><><><><><><><><><><><><><><><>"
        echo -e "\t|\t     MAIN MENU   ";
        echo -e "\t|\t======================";
        echo -e "\t|\t[1] Add a new Contact";
        echo -e "\t|\t[2] List all Contacts";
        echo -e "\t|\t[3] Search for contact";
        echo -e "\t|\t[4] Edit a Contact";
        echo -e "\t|\t[5] Delete a Contact";
        echo -e "\t|\t[0] Exit";
        echo -e "\t|\t======================";
        echo -e "\t|--<><><><><><><><><><><><><><><><><><>\n\n"

        read -p '---> Enter Your choice: ' choice

        case "$choice" in
        1)
         add_new_contact;;
        2)
         list;;
        3)
         search;;
        4)
         update;;
        5)
         delete;;
        0)
         exit 0;;
        *)
         echo " --> invaled input"
        esac

        if test "$choice" -ne 0
        then
          menu
        else
          exit 0
        fi
}
#============================================================
#to let the user to add the file he want and ckeck if it exist
check_file
menu


