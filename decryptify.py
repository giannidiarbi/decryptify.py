#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:13:46 2023

@author: giannidiarbi

Gianni Diarbi
 DS2000
 Spring 2023
 HW 6 Problems 2 & 3
 decryptify.py
 
"""

VIGENERE_FILE = "vigenere.csv"

KEYS_FILE = "keys.txt"

HEADER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          '.', '-', ';', ':', '/', '\\']

ENCRYPTED = "hldrko\bfpkauzjxfw/hkjgl"

COL_POS = 0

def make_decryption(lst):
    ''' Function: make_decryption
        Parameters: 2d list (result of reading in a CSV file)
        Returns: a dictionary
        Does: isolates column 0, makes each element of this column a key of 
        the dictionary, and the value being the rest of the row
    '''
    
    dct = {}
    
    for item in lst:
        key = item[COL_POS]
        values = item[1:]
        dct[key] = values
    return dct

    
def decrypt_word(header, dct, encrypted, key):
    ''' Function: decrypt_word
        Parameters: header (1d list)
                    dictionary
                    encrypted string
                    key (string)
        Returns: string
        Does: decrypts a word using Vigenere cypher
    '''
    
    decrypted = ""
    
    for i in range(len(key)):
       
        key_letter = key[i]
        lst = dct[key_letter]
        
        word_letter = encrypted[i]
        pos = lst.index(word_letter)
        
        decrypted_letter = header[pos]
        decrypted += decrypted_letter
    
    return decrypted

def main():
    
    # Gather data - prompt user for the string input, an encrypted message
    encrypted_msg = input("What is the encrypted message?\n")
    
    # Create an empty list to append keys to
    keys = []
    
    # Read in the keys file, appending each line (key) to the list
    with open (KEYS_FILE, "r") as infile:
        for line in infile:
            line = line.strip()
            keys.append(line)
    
    # Create an empty list to append individual vigenere rows (lists) to 
    lst = []
    
    # Read in the vigenere cipher file  
    with open (VIGENERE_FILE, "r") as infile:
        for line in infile:
            line = line.strip()
            
            # Make each row in the file its own line
            vigenere = line.split(",")
            
            # Append each row list to larger list
            lst.append(vigenere)
        
    # Computations - create a decryption dictionary 
    dct = make_decryption(lst)
  
    # Decrypt the user's input string, trying each key from file
    for key in keys:
        decrypted = decrypt_word(HEADER, dct, encrypted_msg, key)  
        
        # Look for the start of the link in the decrypted string
        if decrypted.startswith("https://bit.ly") == True:
            
            # Communication - report the results (proper link) to the user!
            print("The correct link is:", decrypted)           
 
main()
