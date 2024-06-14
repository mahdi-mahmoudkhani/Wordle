
#include <iostream>
#include <string>
#include <vector>
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

//function to check wether it has duplicate letter
bool has_duplicate_letters(const string& word) {
    for (size_t i = 0; i < word.length(); ++i) {
        for (size_t j = i + 1; j < word.length(); ++j) {
            if (word[i] == word[j]) {
                return true;
            }
        }
    }
    return false;
}

// function to respond guessing
string generate_feedback(const string& guess, const string& secret) {
    string feedback = "----"; // we initialize the first one which is empty is all wrong
    for (int i = 0; i < 4; ++i) {
        if (guess[i] == secret[i]) {
            feedback[i] = '=';
        } else if (secret.find(guess[i]) != string::npos) {  //string::npos is returned by .find() when the substring (or character) is not found within the string.
            feedback[i] = '+';                                 // but with ! we say it was found
        } else {
            feedback[i] = '-';
        }
    }
    return feedback;
}

// backtracking algo to find the word 
bool backtracking(const string& secret) {
    vector<string> candidates;
    string current_guess = "abcd"; // this is the inital guess
    int attempt = 1;

    while (attempt <= 10) { //till 10 tries we can still guess
        string feedback = generate_feedback(current_guess, secret);
        cout << "Attempt " << attempt << ": Guess = " << current_guess << ", Feedback = " << feedback << endl;

        if (feedback == "====") {
            cout << "Found the secret word: " << current_guess << endl;
            return true;
            break;
        }

        // guessing new candidates based on feedbacks
        vector<string> new_candidates;
        for (char c1 = 'a'; c1 <= 'z'; ++c1) { 
            for (char c2 = 'a'; c2 <= 'z'; ++c2) {
                for (char c3 = 'a'; c3 <= 'z'; ++c3) {
                    for (char c4 = 'a'; c4 <= 'z'; ++c4) {
                        string candidate = string(1, c1) + c2 + c3 + c4; //making a string by a copy of char1 and rest to make 4 letters
                        if (!has_duplicate_letters(candidate) && generate_feedback(current_guess, candidate) == feedback) {
                            new_candidates.push_back(candidate);  // Check if candidate has no duplicate letters and if the feedback matches the expected feedback.
                        }
                    }
                }
            }
        }

        candidates = std::move(new_candidates); 

        if (candidates.empty()) {  //if there is no satisfied guess
            return false;
        }

        current_guess = candidates[0]; // take first candidate as the next guess
        attempt++;
    }

    return false;
}

int main() {
    srand(time(0));

    //make a random word
    string secret = generate_random_word();
    cout << "Secret word selected: " << secret << endl;

    // start the backtracking algo
    if (!backtracking(secret)) {
        cout << "Failed to find the secret word in 10 attempts." << endl;
        cout<<"It was "<< secret;
    }

    return 0;
}
