# !/bin/zsh

# 1
# Display a list of all files and sub-directories under the home directory
ls

# 2
# Change the permission of the fine named test.txt to be: read, write, and execute for owner. Read and execute for group. Execute for others.
chmod 751 test.txt

# 3
# Type the command that display the total number of times a string that is three characters starting with capital letter and end with small letters, that appears in a file named test.txt
cat test.txt | egrep --color=auto -o "([A-Z].[a-z])" | wc -l

# 4
# Type the command that display the owner privileges of the files in the current directory. 
ls -la | egrep "^-"
# used grep to filter out directories

# 5
# Type the command that remove all non numeric characters
cat source_file | tr -cd "[:digit:]"

# 6
# Type the command that print the lines that ends with repeated word 
egrep "(.*) \1$"

# 7
# Type the command that return the number of  words that has at least two consecutive occurrence of characters. 
egrep -o "(.)\1" | wc -l

# 8
# Type the command that print the words in a given text line into multiple lines, such that each word appears in a separate line.
tr " " "\n"

# 9
# Find all files with (u=rwx,g=rx,o=r) permission and change their permission to (u=rwx,g=,o=)
find . | egrep "^-rwxr-xr--" | xargs chmod -v 700

# 10
# Type the command that delete the first and last lines in a fine named test.txt
cat test.txt | sed '1d' | sed '$ d' > test.txt
 


# 11 is the same as 9 just changed permissions ?