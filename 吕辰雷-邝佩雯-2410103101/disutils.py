def is_string(s):
    return isinstance(s, str)

def is_sequence(seq):
    if is_string(seq):
        return False
    try:
        len(seq)
    except Exception:
        return False
    return True