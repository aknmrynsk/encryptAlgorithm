from ex_euclid import exEuclidExp


def main():
    # 問題番号を入力
    num = int(input())
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    result = exEuclidExp(a, b)
    # print(f' ({num}) gcd({a}, {b}) = {result}')
    print(f'({num})')
    print(f'{a = }')
    print(f'{b = }')
    print(f'd = ax+by = {result[0]}')
    print(f'x = {result[1]}')
    print(f'y = {result[2]}')
    return result


if __name__ == '__main__':
    main()
