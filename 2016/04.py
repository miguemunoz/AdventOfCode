#!/usr/bin/env python3

"""
    AoC2016, 4th day ( https://adventofcode.com/2016/day/4 )
"""

from collections import Counter

def rotate(word, shift):
    
    decrypted = []
    
    for c in word:
        decrypted.append(chr(((ord(c) - ord('a') + int(shift)) % 26) + ord('a')))
    
    return ''.join(decrypted)

def shift_decypher(words, shift):
    
    message = []
    
    for word in words:
        word = rotate(word, shift)
        message.append(word)
    
    return ' '.join(message)

def calculate_checksum(letters):

    # Counter provides a list with each letter and the number of occurrences
    most_common = dict(Counter(letters).most_common(len(letters)))
    
    # Order the dictionary based in the requirements
    most_common = sorted(most_common.items(), key=lambda x: (-x[1],x[0]))[:5]
    
    # Generates the checksum
    checksum = ''.join([x[0] for x in most_common])
    
    return checksum

def aoc2016d4(filename, first_star):

    valid_rooms = []

    for line in open(filename):

        # Extract the letters, the sector ID and the checksum from each of the rooms
        words = (line.split('-')[:len(line.split('-'))-1])
        sectorID = (line.strip().split('-')[-1]).split('[')[0]
        checksum = (line.strip().split('-')[-1]).split('[')[1][:-1]

        # Decypher the room name (only second star)
        if not first_star:
            if shift_decypher(words, sectorID).find("northpole") != -1:
                return int(sectorID)

        letters = ''.join(words)

        # Validates the checksum
        if checksum == calculate_checksum(letters):
            valid_rooms.append(int(sectorID))

    return sum(valid_rooms)

if __name__ == "__main__":
    print(f'aoc2016d4s1: {aoc2016d4("input.txt", True)}')
    print(f'aoc2016d4s2: {aoc2016d4("input.txt", False)}')
