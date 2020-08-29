from .collections import OrderedSet


class ProcessorMeta(type):
    def __new__(cls, name, bases, cls_dict):
        processors = OrderedSet()
        for base in bases:
            for processor in getattr(base, 'processors', []):
                processors.add(processor)
        for processor in cls_dict.pop('processors', []):
            processors.add(processor)
        cls_dict['processors'] = processors
        return super().__new__(cls, name, bases, cls_dict)
