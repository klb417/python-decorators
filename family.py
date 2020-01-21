def kids(func):
    def append_kids():
        return f"{func()} by the kids"

    return append_kids


def mom(func):
    def append_mom():
        return f"{func()} by Mom"

    return append_mom


def dad(func):
    def append_dad():
        return f"{func()} by Dad"

    return append_dad


@kids
def laundry():
    return "The dirty laundry was cleaned"


@mom
def garbage():
    return "The garbage was taken out"


@dad
def dust():
    return "The house was dusted"


@kids
def groom():
    return "The dog was brushed"


result = garbage()
print(result)

result = laundry()
print(result)

result = dust()
print(result)

result = groom()
print(result)
