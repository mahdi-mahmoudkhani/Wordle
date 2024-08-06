# Wordle Solver

This project is a Python implementation of a backtracking algorithm to solve the popular word game "Wordle". The algorithm attempts to guess a 4-letter word based on feedback provided by the user. Note that the guessed word may not necessarily be a meaningful word; it just fits the feedback criteria provided by the user.

## Table of Contents
- [Description](#description)
- [How It Works](#how-it-works)

## Description

The Wordle Solver uses a backtracking algorithm to make guesses and refine those guesses based on feedback from the user. It continues to make guesses until it correctly identifies the word or exhausts the available attempts. Note that the guessed word may not necessarily be meaningful; it just fits the given feedback criteria.

## How It Works

1. **Initialization**:
   - The algorithm starts with an empty guess represented as `['0', '0', '0', '0']`.
   - It maintains a list of alphabets (`ALPHABET`) from 'a' to 'z'.
   - It tracks letters that cannot be in certain positions (`notInPlaces`), initialized as a dictionary where each key corresponds to a position and each value is a list of letters that cannot be in that position.

2. **Feedback Analysis**:
   - The `feedbackAnalisys` function takes user feedback to refine future guesses.
   - Feedback format:
     - `'='` indicates the letter is correct and in the correct position.
     - `'+'` indicates the letter is correct but in the wrong position.
     - `'-'` indicates the letter is not in the word at all.
   - If the feedback is `'===='`, it means the word is correctly guessed.

3. **Backtracking Algorithm**:
   - The `backtrackingWordle` function recursively builds the word by checking each letter from `ALPHABET`.
   - It ensures no repeated letters in positions already guessed.
   - If a valid letter is found for the current position, it proceeds to the next position.
   - If no valid letter is found for a position, it backtracks to the previous position to try a different letter.

4. **Game Loop**:
   - The `display` function controls the game loop, calling the `backtrackingWordle` and `feedbackAnalisys` functions.
   - The game continues until the word is guessed or all chances are used.
