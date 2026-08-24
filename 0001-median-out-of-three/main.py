def main():
    a = str(input())
    s = a.split(" ")
    for i in range(len(s)):
        s[i] = int(s[i])
    s.sort()
    print(s[1])


if __name__ == '__main__':
    main()