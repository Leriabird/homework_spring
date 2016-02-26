# import sys
#
# data = sys.stdin.read().split('\n')

# a = '3.a b c.4.c ex1 ex2.b ex3 _.a ex2 _.c ex3 ex3.ex3'
# data = a.split('.')


stack_size = int(input())
stack_contents = input().split()
m_foo_lines = int(input())
data = list()
for i in range(0, m_foo_lines):
    data.append(input())
current_exeption = input()

behavior = dict()

for char in data:
    line = char.split()
    if not line[0] in behavior:
        behavior[line[0]] = {line[1]: line[2]}
    else:
        behavior[line[0]][line[1]] = line[2]
stack_reverse = stack_contents[::-1]

for char in stack_reverse:
    elt = behavior[char]
    if current_exeption not in elt:
        stack_contents.pop()
    elif elt[current_exeption] != "_":
        current_exeption = elt[current_exeption]
        stack_contents.pop()
    else:
        break

print(' '.join(stack_contents))
