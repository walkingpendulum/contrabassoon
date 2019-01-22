from itertools import product


DIESE = '♯'
BEMOL = '♭'
NAMES = 'A.BC.D.EF.G.'
MINOR_SCALE_INTERVALS = (0, 2, 3, 5, 7, 8, 10)
MAJOR_SCALE_INTERVALS = (0, 2, 4, 5, 7, 9, 11)


def get_note_names(note):
    ind = note.n
    names = []

    left = NAMES[(ind - 1) % 12]
    if left != '.':
        names.append(f'{left}{DIESE}')

    current = NAMES[ind % 12]
    if current != '.':
        names.append(f'{current}')

    right = NAMES[(ind + 1) % 12]
    if right != '.':
        names.append(f'{right}{BEMOL}')

    return tuple(sorted(names, key=len))


class Note:
    def __init__(self, n):
        self.n = n % 12

    def __add__(self, other):
        try:
            return self.__class__(self.n + other)
        except TypeError as e:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(other).__name__}'")

    def __sub__(self, other):
        try:
            return self.__class__(self.n - other)
        except TypeError as e:
            raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(other).__name__}'")

    def __repr__(self):
        return f'{get_note_names(self)[0]}'


class Scale:
    def __init__(self, note):
        self.tonic = note

    def minor(self):
        return ''.join(f'{x:^4}' for x in make_scale(self.tonic, MINOR_SCALE_INTERVALS)).strip()

    def major(self):
        return ''.join(f'{x:^4}' for x in make_scale(self.tonic, MAJOR_SCALE_INTERVALS)).strip()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.tonic})'


def scale_all_names(tonic, scale_intervals):
    return set(product(*[get_note_names(tonic + interval) for interval in scale_intervals]))


def make_scale(tonic, scale_intervals):
    scale_names = scale_all_names(tonic, scale_intervals)
    diversed = [scale_name for scale_name in scale_names if len(set(note_name[0] for note_name in scale_name)) == 7]
    alterations_count = lambda note_names: sum(len(note_name) == 2 for note_name in note_names)

    return sorted(diversed, key=alterations_count)[0]


A, B, C, D, E, F, G = map(Note, MINOR_SCALE_INTERVALS)
