'''
--- PART ONE ---
'''

# read in input file
def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read().rstrip()
        return data

# convert string of hex into bin (each hex digit -> 4 bin digits)
def to_binary(hexa):
    bin_ret = ''

    for digit in hexa:
        bin_ret += bin(int(digit, 16))[2:].zfill(4)

    return bin_ret

# handle case when have id type 4 packet
def literal_value_packet(bin, iter, ver_deci, id_deci):
    last_grouped = False
    digit_offset = iter + 6 # offset in the orig binary
    literal_bin = ''
    packets = []

    # while there are still groups of bin digits to process
    while not last_grouped:

        curr_group = bin[digit_offset : digit_offset+5]
        digit_offset += 5

        # reached last group
        if curr_group[0] == '0':
            last_grouped = True

        literal_bin += curr_group[1:] # build up literal value binary

    literal_deci = int(literal_bin, 2)

    packets.append(
        {'version': ver_deci, 'id': id_deci, 'value': literal_deci}
    )

    return digit_offset, packets

# handle case when have operator packet
def operator_packet(bin, iter, ver_deci, id_deci):
    digit_offset = 6 + iter # offset in the orig binary
    packets = []
    subpackets = []

    length_type_id = bin[digit_offset]
    length_type_id_deci = int(length_type_id, 2)
    digit_offset += 1

    # length type 0
    if length_type_id_deci == 0:
        length_bin = bin[digit_offset:digit_offset+15]

        if len(length_bin) == 0: # if invalid, then should not continue to process
            packets.append(
                {'version': ver_deci, 'id': id_deci, 'length': length_type_id_deci, 'subpackets': subpackets}
            )
            return digit_offset, packets

        length_deci = int(length_bin, 2)

        subpacket_bin = bin[digit_offset+15: digit_offset+15+length_deci] # subpacket binary
        digit_offset = digit_offset+15+length_deci

        subpackets.extend(separate_packets(subpacket_bin, True))

    # length type 1
    elif length_type_id_deci == 1:
        num_bin = bin[digit_offset:digit_offset+11]
        num_deci = int(num_bin, 2)

        digit_offset = digit_offset+11

        for i in range(num_deci):

            # shortest packet is 11
            if len(bin[digit_offset:]) < 11:
                break

            sub_ver = bin[digit_offset : digit_offset+3]
            sub_id = bin[digit_offset+3 : digit_offset+6]

            if len(sub_ver) < 3 or len(sub_id) < 3: # if no ver/id, then invalid package to process
                break

            sub_ver_deci = int(sub_ver, 2)
            sub_id_deci = int(sub_id, 2)

            # literal value
            if sub_id_deci == 4:
                output = literal_value_packet(bin[digit_offset:], 0, sub_ver_deci, sub_id_deci)
                digit_offset += output[0]
                subpackets.extend(output[1])
            # operator
            else:
                output = operator_packet(bin[digit_offset:], 0, sub_ver_deci, sub_id_deci)
                digit_offset += output[0]
                subpackets.extend(output[1])

    else:
        print('ERROR: invalid length type id')

    packets.append(
        {'version': ver_deci, 'id': id_deci, 'length': length_type_id_deci, 'subpackets': subpackets}
    )

    return digit_offset, packets

# separate packet binary input into list of packets
# given hex
def separate_packets_hexa(hexa):
    bin = to_binary(hexa)
    return separate_packets(bin, False)

# separate packet binary input into list of packets
# given binary
def separate_packets(bin, is_subpacket):
    packets = []
    iter = 0

    # iterate through input binary
    while iter < len(bin):

        # shortest packet is 11
        if len(bin[iter:]) < 11:
            break

        ver = bin[iter : iter+3]
        id = bin[iter+3 : iter+6]

        if len(ver) < 3 or len(id) < 3: # if no ver/id type then invalid package to process
            break
        
        ver_deci = int(ver, 2)
        id_deci = int(id, 2)

        new_offset = 0

        # literal value
        if id_deci == 4:
            output = literal_value_packet(bin, iter, ver_deci, id_deci)
            new_offset = output[0]
            packets.extend(output[1])

        # operator
        else:
            output = operator_packet(bin, iter, ver_deci, id_deci)
            new_offset = output[0]
            packets.extend(output[1])

        if is_subpacket:
            iter += new_offset
        else:
            iter = new_offset + (new_offset % 4)
    
    return packets

# get sum of versions from list of packets
def version_sum(packets):
    packet_list = separate_packets_hexa(packets)
    ver_sum = 0

    for packet in packet_list:
        ver_sum += packet['version']
        sub_search = []

        if 'subpackets' in packet.keys():
            sub_search = packet['subpackets']

        # if have subpackets, continue processing all encountered subpackets
        while len(sub_search) > 0:
            curr_packet = sub_search.pop(0)

            ver_sum += curr_packet['version']

            # check subpackets
            if 'subpackets' in curr_packet.keys():
                sub_search.extend(curr_packet['subpackets'])

    return ver_sum

packets = read_file('shorter.txt')
print(version_sum(packets))
