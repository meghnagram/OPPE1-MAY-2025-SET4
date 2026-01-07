

m, n = map(int, input().split())
board = [input() for _ in range(m)]

border = '+' + ('-+' * n)
for row in board:
    print(border)
    print('|' + '|'.join(row) + '|')
print(border)

#Another Method

# Write your code here to read input and print the formatted board

x,y=map(int,input().split())

m=[]

for i in range(x):
    m.append(input())
    
for i in range(x):
    print('+-'*y +'+')
    for j in range(y):
        print('|',end='')
        print(m[i][j],end='')
    print('|')
print('+-'*y +'+')

Format Tic-Tac-Toe Board
You are given a tic-tac-toe board of size m x n containing characters:

'X' for player X
'O' for player O
' ' (space) for empty cells
Your task is to print this board with borders using the characters +, -, and |.
The border format must be as follows:

Each row is wrapped in | separators for each column.
Horizontal lines made of + and - separate each row, including the top and bottom.
NOTE: This is an I/O type problem. You must write the complete code for taking input and printing the output.

Input Format

The first line contains two integers, m and n, denoting the number of rows and columns of the board.
The next m lines each contain a string of n characters from 'X', 'O', or ' '(space).
Output Format

The board printed with borders using +, -, and |.
Example

Input

3 4
O XO
XO
O  X

Output

+-+-+-+-+
|O| |X|O|
+-+-+-+-+
|X|O| | |
+-+-+-+-+
|O| |X| |
+-+-+-+-+


