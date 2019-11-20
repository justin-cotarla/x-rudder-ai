from abc import ABC

class Command(ABC):
    LETTER_MAPPING = dict((alpha, num) for (num, alpha) in enumerate([chr(x) for x in range(ord('a'), ord('m') + 1)]))
    REVERSE_LETTER_MAPPING = dict((num, alpha) for (num, alpha) in enumerate([chr(x) for x in range(ord('a'), ord('m') + 1)]))  