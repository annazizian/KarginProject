IGNORE_SYMBOLS = set("՜,՞՛;․՝-~.")


def case_insensitive(s):
    return s.lower()


def ignore_symbols(s):
    return ''.join(i for i in s if i not in IGNORE_SYMBOLS)


class ProcessorMeta(type):
    def __new__(metacls, name, bases, cls_dict):
        extra_processors = cls_dict.pop('processors', set())
        for base in bases:
            extra_processors |= getattr(base, 'processors', set())
        cls_dict['processors'] = extra_processors
        return super().__new__(metacls, name, bases, cls_dict)
