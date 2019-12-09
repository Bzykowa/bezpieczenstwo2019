#!/usr/bin/env python3

from streamcypher import Streamcypher
import operator

class Decryptor:

    def __init__(self, data_file):
        #Kryptogramki z pliku
        self.cryptograms = []

        # Nazwa pliku
        self.data_file = data_file

        # dict z częstotliwością znaków (ASCII).
        self.letters_freq = {
            'a': 100, 'i': 83, 'o': 86, 'e': 88, 'z': 65, 'n': 58, 'r': 47, 'w': 47, 's': 50, 't': 40, 'c': 43, 'y': 38,
            'k': 36, 'd': 33, 'p': 31, 'm': 28, 'u': 25, 'j': 23, 'l': 39, 'b': 13, 'g': 15, 'h': 10, 'f': 3, 'q': 1,
            'v': 1, 'x': 1, ' ': 100, ',': 16, '.': 10, '-': 10, '"': 10, '!': 10, '?': 10, ':': 10, ';': 5, '(': 10,
            ')': 10
        }

        # Wielkie litery 1%
        for i in range(65, 91):
            self.letters_freq[chr(i)] = 20

        # Liczby 1%
        for i in range(48, 58):
            self.letters_freq[chr(i)] = 10

    # Czytanie kryptogramów z pliku
    def get_data_from_file(self):
        with open(self.data_file, 'r') as file:
            for line in file:
                self.cryptograms.append(Streamcypher(line))

    # Szukanie klucza
    def find_key(self):
        key = []

        # najdłuższy kryptogram
        longest = 0

        # wyznaczanie najdłuższego kryptogramu
        for crypt in self.cryptograms:
            if len(crypt.chars) > longest:
                longest = len(crypt.chars)

        for i in range(0, longest):
            # Dict ze znakami, które mogą być kluczem
            possible_key = {}

            # Kryptogramy o długości mniejszej niż i
            matching_cryptograms = []

            # Szukanie takich kryptogramów
            for crypt in self.cryptograms:
                if i < len(crypt.chars):
                    matching_cryptograms.append(crypt)

            for crypt in matching_cryptograms:
                for possible in self.letters_freq.keys():

                    # XOR charów kryptogramu z literami alfabetu
                    tmp = (ord(crypt.get_chr(i)) ^ ord(possible), self.letters_freq[possible])

                    # Wsadzenie w dict częstotliwości wyników XOR
                    if tmp[0] not in possible_key.keys():
                        possible_key[tmp[0]] = tmp[1]
                    else:
                        possible_key[tmp[0]] = possible_key.get(tmp[0]) + self.letters_freq.get(possible)

            # Sortowanie kluczów dla szybszego szukanka
            tmp_sorted = sorted(possible_key.items(), key=operator.itemgetter(1), reverse=True)
            possible_key = dict(tmp_sorted)

            best_possible = ord(' ')
            best_counter = 0

            for possible in possible_key.keys():
                counter = 0

                for crypt in matching_cryptograms:
                    # Sprawdzenie czy XOR zwraca znak z alfabetu
                    if (chr(ord(crypt.get_chr(i)) ^ possible)) in self.letters_freq.keys():
                        counter += 1

                # Najlepszy klucz najwięcej razy trafia w znaki z alfabetu
                if counter > best_counter:
                    best_counter = counter
                    best_possible = possible

            key.append(best_possible)

        return key

    # Zapis wyników do pliku
    def output(self):
        key = self.find_key()
        with open('output.txt', 'w') as file:
            for crypt in self.cryptograms:
                for i in range(0, len(crypt.chars)):
                    file.write(chr(ord(crypt.get_chr(i)) ^ key[i]))
                file.write('\n')
