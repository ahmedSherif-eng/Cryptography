import textwrap

import conversion
import misc
import permutations


def encrypt(text, key):
    binary_text = misc.text_to_bits(text)
    binary_text = textwrap.wrap(binary_text, 64)
    last_text_part = binary_text[len(binary_text) - 1]
    binary_text[len(binary_text) - 1] = last_text_part + ''.zfill(64 - len(last_text_part))
    print(binary_text[len(binary_text) - 1])
    subkeys = conversion.primary_key_to_subkeys(key)
    print(len(subkeys))
    for part_num, part in enumerate(binary_text):
        print("round no :",part_num)
        part = permutations.permutation(part, "initial")
        lpt, rpt = part[:int(len(part) / 2)], part[int(len(part) / 2):]
        for i in range(16):
            new_lpt = rpt
            new_rpt = misc.XOR(lpt, function(rpt, subkeys[i]))
            lpt, rpt = new_lpt, new_rpt
        binary_text[part_num] = permutations.permutation(rpt + lpt, "inverse")
    return hex(int(''.join(binary_text), 2))[2:]

def function(rpt, subkey):
    rpt = permutations.permutation(rpt, "expansion")
    rpt = misc.XOR(rpt, subkey)
    rpt = permutations.sBox_permutation(rpt)
    rpt = permutations.permutation(rpt, "pBox")
    return rpt
