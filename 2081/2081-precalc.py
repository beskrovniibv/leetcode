BASE = "0123456879"


def to_base(number, base):
    result = ""
    while number:
        result += BASE[number % base]
        number //= base
    ff = result[::-1] or "0"
    bw = result.lstrip("0")
    return ff, bw


def check(number):
    d = str(number)
    r = d[::-1].lstrip("0")
    return d, r


def palindrome_generator():
    length = 1
    while True:
        if length % 2 == 0:
            half_len = length//2
        elif length == 1:
            half_len = 1
        else:
            half_len = length//2
        start = 10**(half_len - 1)
        end = 10**(half_len)

        for half in range(start, end):
            half_str = str(half)
            if length % 2 == 0:
                pal_str = half_str + half_str[::-1]
            elif length == 1:
                yield int(half_str)
                continue
            else:
                for middle_digit in range(10):
                    pal_str = half_str + str(middle_digit) + half_str[::-1]
                    yield int(pal_str)
                continue
            yield int(pal_str)
        length += 1


def main():
    result = {}
    lens = [0]*10
    palindromes = palindrome_generator()
    while True:
        i = next(palindromes)
        for j in range(2, 10):
            dk, rk = to_base(i, j)
            if dk == rk:
                result[j] = result.get(j, [])
                if len(result[j]) == 30:
                    continue
                result[j].append(i)
                lens[j] += 1
        if sum(lens) == 240:
            break
    print(result)


if __name__ == "__main__":
    main()
