/******************************************************************************

q-Write a C++ function that counts the number of words in a given sentence (string).

note : better documentation is comming time management problem

prerequisite consepts
> The getline() function extracts characters from the input stream
> for (char ch : sentence): This is a range-based for loop in C++, 
which iterates over each character (char) in the string sentence.
It automatically iterates through each character in the string without the need for explicit index management.



*******************************************************************************/

#include <iostream>

using namespace std;

int main() {
    string sentence;
    int wordCount = 0;
    bool inWord = false;

    cout << "Enter a sentence: ";
    getline(cin, sentence);

    for (char ch : sentence) {
        if (ch == ' ') {
            if (inWord) {
                wordCount++;
                inWord = false;
            }
        } else {
            inWord = true;
        }
    }

    if (inWord) {
        wordCount++;
    }

    cout << "Number of words: " << wordCount << endl;

    return 0;
}
