# coding: utf-8
MAX_NUMBER = 1000
error_message = '有効な入力は{}までの正の整数です。\n'.format(MAX_NUMBER)


def get_prime_numbers(max_num):
    tmp_prime_number_list = [2]
    for i in range(3, max_num):
        has_prime = False
        for prime_num in tmp_prime_number_list:
            if i % prime_num == 0:
                has_prime = True
                break
        if not has_prime:
            tmp_prime_number_list.append(i)
    return tmp_prime_number_list


def get_prime_factorization(number, prime_number_list):
    tmp_factorization_list = []
    if number == 1:
        tmp_factorization_list.append(int(number))
        return tmp_factorization_list
    while True:
        if number in prime_numbers_list:
            tmp_factorization_list.append(int(number))
            break
        for prime_num in prime_number_list:
            if number % prime_num == 0:
                tmp_factorization_list.append(int(prime_num))
                number /= prime_num
                break
    return tmp_factorization_list


prime_numbers_list = get_prime_numbers(MAX_NUMBER)
while True:
    print('素数か判定したい{}までの正の整数を入力してください。'.format(MAX_NUMBER))
    try:
        number = int(input())
    except ValueError:
        print(error_message)
        continue
    if number < 1:
        print(error_message)
        continue

    if number > MAX_NUMBER:
        print(error_message)
        continue
    if number in prime_numbers_list:
        print('{}は素数です。'.format(number))
    else:
        print('{}は素数ではありません。'.format(number))
        factorization_list = get_prime_factorization(number, prime_numbers_list)
        factorization_numbers = ','.join(map(str,factorization_list))
        print('{}は{}に素因数分解できます。'.format(number, factorization_numbers))
    break
