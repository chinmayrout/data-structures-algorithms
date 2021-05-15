#Python program to convert snake case to camel case
#camelCase
#snake_case
#kebab-case
#PascalCase

#snake_case to camelCase
name = 'chinmayRoutIsTheBest'

print(name)

def camel_to_snake(s):
    result = ""
    c = s[0]
    result = result + c.lower()

    for i in range(1, len(s)):
        ch = s[i]
        if(ch.isupper()):
            result = result + '_'
            result = result + ch.lower()
        else:
            result = result + ch
    return result



print(camel_to_snake(name))

def snake_to_camel(strr):
    words = strr.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].capitalize()

    return "".join(words)

str = "snake_case_chinmay_rout"
print(snake_to_camel(str))