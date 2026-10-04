def main():
    field = []
    n, m = map(int, input().split())
    for _ in range(n):
        row = list(map(int, input().split()))
        field.append(row)

    for j in range(n):
        for i in range(m):
            if i==0 and j==0:
                continue
            elif j==0:
                field[j][i] += field[j][i-1]
            elif i==0:
                field[j][i] += field[j-1][i]
            else:
                field[j][i] += min(field[j][i-1], field[j-1][i])
    print(field[n-1][m-1])

if __name__ == '__main__':
    main()