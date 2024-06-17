def print_pattern(size):
    width = size * 4 - 3
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(1 - size, size):
        line = "-".join(alphabet[size - abs(i):size] + alphabet[size - abs(i) - 1:size][::-1])
        print(line.center(width, "-"))

if __name__ == '__main__':
    size = int(input("Enter the size of the pattern: "))
    print_pattern(size)