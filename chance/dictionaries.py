#!/usr/bin/python
dict = {}
dict
dict['one'] = 'uno'
dict
print dict['one']
dict['two'] = "dos"
dict
dict = {'two': 'dos', 'one': 'uno'}
print dict
dict = {'two': 'dos', 'one': 'uno', 'three':'tres'}
print dict
dict = {'two': 'dos', 'one': 'uno', 'three':'tres','quatro'}
print dict['dos']
dict['one']='adin'
len(dict)
dict.keys()
dict.values()
dict.items()
dict.has_key('one')
opposites = {'up':'down', 'right':'wrong', 'true':'false'}
alias=opposites
copy=opposites.copy()
opposites['right']='left'
print opposites
print alias
print copy
alias['right']='wrong'
print alias
print opposites
print copy
copy['right']='privilege'
print copy
print alias
print opposites