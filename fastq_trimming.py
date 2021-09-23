#! /usr/bin/env python3

#Anne-Sophie Denommé-Pichon
#AGPLv3

import sys

def trimmsample(size):
    """
    size: size of the read you want
    """
    try:
        while True: # boucle infinie pour lire les lignes 4 par 4
            title_line = next(sys.stdin).rstrip()
            sequence_line = next(sys.stdin).rstrip()
            plus_line = next(sys.stdin).rstrip()
            quality_line = next(sys.stdin).rstrip()
            print(title_line)
            print(sequence_line[:size])
            print(plus_line)
            print(quality_line[:size])

    except StopIteration: # quand erreur StopIteration, arrêter
        pass
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        trimmsample(int(sys.argv[1]))
    else:
        print("Usage: fastq_trimming.py <size> < input.fastq > output.fastq", file=sys.stderr)
        sys.exit(1)
    
