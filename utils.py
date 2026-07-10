import string

from snowflake import SnowflakeGenerator
from config import settings

# Define the alphabet: 0-9, a-z, A-Z (or any order, but must be consistent)
BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase

_gen = SnowflakeGenerator(settings.MACHINE_ID)

def b62_encode(num: int, alphabet=BASE62) -> str:
    """Encode a positive number into Base62."""
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return "".join(arr)


def b62_decode(string: str, alphabet=BASE62) -> int:
    """Decode a Base62 string into a number."""
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
    for char in string:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base**power)
        idx += 1
    return num


def generate_id() -> int | None:
    return next(_gen, None)
