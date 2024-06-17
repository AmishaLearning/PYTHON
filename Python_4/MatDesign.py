# N = int(input("Enter the number : "))
# M = N ** 3
# print(M)
 
# for i in range(1,N):
#     for j in range(i + 1):
#         print("-", end="")
# print(".|.", end="")
# for i in range(1,N):
#     for j in range(i + 1):
#         print("-", end="")

def door_mat_pattern(rows, columns):
    # Upper part of the door mat
    for i in range(rows // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(columns, '-'))

    # Welcome line
    print("WELCOME".center(columns, '-'))

    # Lower part of the door mat
    for i in range(rows // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(columns, '-'))

if __name__ == '__main__':
    N, M = map(int, input().split())
    door_mat_pattern(N, M)