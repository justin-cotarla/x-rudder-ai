from abc import ABC

class Command(ABC):
    LETTER_MAPPING = dict((alpha, num) for (num, alpha) in enumerate([chr(x) for x in range(ord('a'), ord('m') + 1)]))