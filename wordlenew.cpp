#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <random>
#include <ctime>

using namespace std;

// Function to generate a random word of 4 unique letters
string generate_random_word() {
    string letters = "abcdefghijklmnopqrstuvwxyz";
    random_device rd; // Random device to obtain a random seed
    mt19937 g(rd()); // Mersenne Twister engine seeded with rd

    shuffle(letters.begin(), letters.end(), g); // Shuffle all letters
    return letters.substr(0, 4); // Return the first 4 letters as the random word
}

// Function to check whether it has duplicate letters
bool has_duplicate_letters(const string& word) {
    set<char> seen;
    for (int i=0 ; i<word.length(); i++ ) {
        if (seen.count(word[i])) {
            return true;
        }
        seen.insert(word[i]);
    }
    return false;
}

// Function to generate feedback based on the guess and secret
string generate_feedback(const string& guess, const string& secret) {
    string feedback = "----"; // Initialize feedback with all wrong
    for (int i = 0; i < 4; ++i) {
        if (guess[i] == secret[i]) {
            feedback[i] = '=';
        } else if (secret.find(guess[i]) != string::npos) {
            feedback[i] = '+';
        } else {
            feedback[i] = '-';
        }
    }
    return feedback;
}

// Function to filter out candidates that reuse unsuccessful letters
vector<string> filter_candidates(const vector<string>& candidates, const string& current_guess, const string& feedback) {
    vector<string> filtered_candidates;
    set<char> incorrect_letters;

    // Collect incorrect letters from the current guess
    for (int i = 0; i < 4; ++i) {
        if (feedback[i] == '-') {
            incorrect_letters.insert(current_guess[i]);
        }
    }

    // Filter candidates based on incorrect letters
    for (const string& candidate : candidates) {
        bool valid_candidate = true;
        for (char c : incorrect_letters) {
            if (candidate.find(c) != string::npos) {
                valid_candidate = false;
                break;
            }
        }
        if (valid_candidate) {
            filtered_candidates.push_back(candidate);
        }
    }

    return filtered_candidates;
}

// Backtracking algorithm to find the word
bool backtracking(const string& secret) {
    set<string> previous_guesses;
    vector<string> candidates;
    string current_guess = "abcd"; // Initial guess
    int attempt = 1;

    while (attempt <= 10) { // Till 10 tries we can still guess
        string feedback = generate_feedback(current_guess, secret);
        cout << "Attempt " << attempt << ": Guess : " << current_guess << ", Feedback : " << feedback << endl;

        if (feedback == "====") {
            cout << "Found the secret word: " << current_guess << endl;
            return true;
        }

        // Generate new candidates based on feedback
        if (candidates.empty()) {
            // Generate initial set of candidates
            for (char c1 = 'a'; c1 <= 'z'; ++c1) {
                for (char c2 = 'a'; c2 <= 'z'; ++c2) {
                    for (char c3 = 'a'; c3 <= 'z'; ++c3) {
                        for (char c4 = 'a'; c4 <= 'z'; ++c4) {
                            string candidate = string(1, c1) + c2 + c3 + c4;
                            if (!has_duplicate_letters(candidate) && previous_guesses.find(candidate) == previous_guesses.end()) {
                                candidates.push_back(candidate);
                            }
                        }
                    }
                }
            }
        } else {
            // Filter candidates based on incorrect letters from the previous attempt
            candidates = filter_candidates(candidates, current_guess, feedback);
        }

        if (candidates.empty()) {  // If there is no suitable guess
            return false;
        }

        // Randomly select the next guess from candidates
        random_device rd;
        mt19937 g(rd());
        shuffle(candidates.begin(), candidates.end(), g);

        current_guess = candidates[0]; // Take the first candidate as the next guess
        previous_guesses.insert(current_guess);
        attempt++;
    }

    return false;
}

int main() {
    srand(time(0));

    // Make a random word
    string secret = generate_random_word();
    cout << "Secret word selected: " << secret << endl;

    // Start the backtracking algorithm
    if (!backtracking(secret)) {
        cout << "Failed to find the secret word in 10 attempts." << endl;
        cout << "It was " << secret << endl;
    }

    return 0;
}
