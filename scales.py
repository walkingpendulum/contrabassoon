from main import A, Scale


if __name__ == '__main__':
    print('\nminor scales table:')
    for interval in range(12):
        print(f'\t{Scale(A + interval).minor()}')

    print('\nmajor scales table:')
    for interval in range(12):
        print(f'\t{Scale(A + interval).major()}')
