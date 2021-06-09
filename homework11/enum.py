class SimplifiedEnum(type):
    """Metaclass to create optimal Enum classes without duplications
    in variables declarations. Instead of duplications new class should
    define enum members as elements of tulpe '__keys' and metaclass
    would create values for this members and would set corresponding
    attribites to the new class.
    """

    def __new__(cls, name, bases, dct):
        cls_instance = super().__new__(cls, name, bases, dct)
        key = "_" + name + "__keys"
        for item in dct[key]:
            setattr(cls_instance, item, item)
        return cls_instance
