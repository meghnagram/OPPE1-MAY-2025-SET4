


piece_name = {'K': 'King', 'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight'}

moves = input().split()
del moves[::3] # deletes the move numbers

for move in moves:
    if move[0] == 'O':
        print('King')
        print('Rook')
    elif move[0] in piece_name:
        print(piece_name[move[0]])
    else:  
        print("Pawn")

# #Another METHOD


# # write your solution here

# s=input()
# l=[]
# l=s.split()

# for i in l:
#     if '.' in i:
#         pass
#     elif 'K' in i:
#         print("King")
#     elif 'Q' in i:
#         print("Queen")
#     elif 'R' in i:
#         print("Rook")
#     elif 'B' in i:
#         print("Bishop")
#     elif 'N' in i:
#         print("Knight")
#     elif 'O-O' in i:
#         print("King")
#         print("Rook")
#     elif 'O-O-O' in i:
#         print("King")
#         print("Rook")
#     else:
#         print("Pawn")
    
# Print Pieces Moved from Chess Notation string.
# Write a program that reads chess moves in standard algebraic notation and prints out the names of the chess pieces that have been moved. For castling moves, both the king and rook should be printed.

# NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

# Input Format
# The input will be a string of chess moves in format "{move_number} {white_move} {black_move}, where each move is given in standard algebraic notation.
# Output Format
# Print the names of the pieces moved in each move. The output should be each piece's name in separate lines. For castling, print "King" and "Rook".
# Chess Notation Details
# Pieces are represented by their initials:
# K - King
# Q - Queen
# R - Rook
# B - Bishop
# N - Knight
# Pawn (no initial, just represented by move)
# Castling is represented with:
# O-O (kingside castling)
# O-O-O (queenside castling)
# Example

# Input

# 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. O-O Qc7
# Output

# Pawn
# Pawn
# Knight
# Knight
# Bishop
# Pawn
# King
# Rook
# Queen
# Input for Castling

# 1. e4 e5 2. O-O O-O-O
# Output

# Pawn
# Pawn
# King
# Rook
# King
# Rook        
        


