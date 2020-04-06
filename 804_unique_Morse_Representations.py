# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:12:48 2018

@author: Evan_He
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.",
                 "--.","....","..",".---","-.-",".-..",
                 "--","-.","---",".--.","--.-",".-.",
                 "...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        def bet_to_morse(word):
            morse_word = ''
            for alpha in word:
                morse_word+=morse[alphabet.index(alpha)]
            return morse_word
        morse_list =[bet_to_morse(word) for word in words]
        return len(set(morse_list))
                