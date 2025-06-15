from hashlib import md5


def mining_coins(secret_key: str) -> int:
    key_number = 1

    while True:
        input_hash = bytes(secret_key + str(key_number), encoding="utf-8")
        output_hash = md5(input_hash).hexdigest()

        if output_hash.startswith("0" * 5):
            return key_number

        else:
            key_number += 1
