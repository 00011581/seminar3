def decimaltobinary(value):
    result = str()
    while value >= 1:
        remainder = value % 2
        value = value // 2
        result += str(remainder) 
    return result[::-1]

def decimaltooct(value):
    result = str()
    while value >= 1:
        remainder = value % 8
        value = value // 8
        result += str(remainder)
    return result[::-1]


def decimaltohex(value):
    in_letters= {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    result = str()
    while value >= 1:
        remainder = value % 16
        value = value // 16
        if remainder >= 10:
            result += in_letters[remainder]
        else:
            result += str(remainder)
    return result[::-1]