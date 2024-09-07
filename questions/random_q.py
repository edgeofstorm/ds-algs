"""
A function received a string input such as "aabbbcccc"

The expected output would be a string such as "a2b3c4". The letter found in the string followed by a digit that represented the number of repeated occurrences of that letter.

is it sorted ?
"""

str = "aabbbcccc"


count = {}
for char in str:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

output = ""
for char, occurance in count.items():
    output += f"{char}{occurance}"

print(output)


# if sorted without hashmap
output = f"{str[0]}1"
for i in range(1, len(str)):
    if str[i] not in output:
        output += f"{str[i]}1"
    if str[i] == str[i - 1]:
        output = output[:-1] + f"{int(output[-1]) + 1}"
print(output)
