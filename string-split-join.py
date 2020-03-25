"""
Here's a challenge called 'String split join' from hackerrank to warm us up.

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input

this is a string   
Sample Output

this-is-a-string


To solve this its more straightforward as the nuances of what you need to do are more obvious.
Here's my solution:

It's all about learning and using the split method which is common practice when you would
like to modify strings since they are immutable. I created a new variable to do this. Then, split the
varaible by the spaces and then rejoined them at those spaces with a hyphen. Notice I also created
another variable after new which is result. This is also necessary because of immutability. 

"""

def split_and_join(line):
    # write your code here
    new = line.split(' ')
    result = '-'.join(new)
    return result