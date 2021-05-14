#Python program to convert snake case to camel case
#camelCase
#snake_case
#kebab-case
#PascalCase

#snake_case to camelCase
name = 'snake_case_name'
name = ''.join(word.title() for word in name.split('_'))
print(name)

def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')

print(camel_to_snake(name))