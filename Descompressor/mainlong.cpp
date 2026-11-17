// 2026 March 22
// Daniela Rigoli
// C++
// 

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <set>
#include <vector>
#include <chrono>

using namespace std;

unordered_map<char, string> dic;
unordered_map<char, unsigned long long> memo;

set<char> keys;
set<char> appearsInValue;

// recursive function
unsigned long long descompress(const string text) {
    unsigned long long result = 0;

    for (char ch : text) {
        if (dic.count(ch)) { // used to check for the presence of a specific key within the container
            if (memo.count(ch)) { // already descompress before
                result += memo[ch];
            } else {
                unsigned long long expanded = descompress(dic[ch]);
                memo[ch] = expanded;
                result += expanded;
            }
        } else {
            result += 1l;
        }
    }
    return result;
}

int main(int argc, char* argv[]) {
    string filename = (argc > 1) ? argv[1] : "input.txt";
    ifstream file(filename);

    if (!file.is_open()) {
        cerr << "Error opening file\n";
        return 1;
    }

    string line;
    string text = "";

    // read file line by line
    while (getline(file, line)) {
        // split by space
        stringstream ss(line);
        string key, value;
        ss >> key >> value;

        if (!key.empty() && !value.empty()) {
            dic[key[0]] = value;

            keys.insert(key[0]);

            // root node
            // mark which one does not appear in values
            for (char c : value) {
                appearsInValue.insert(c);
            }
        }
    }

    file.close();

    // count time
    auto start = chrono::high_resolution_clock::now();
    char root;

    for (char k : keys) {
        if (!appearsInValue.count(k)) {
            root = k;
            break;
        }
    }

    if (!root) {
        cout << "No Root Found" << endl;
    }

//    cout << "Here " << (dic.count('m') ? "true" : "false") << endl;


    unsigned long long result = descompress(string(1, root));
    // end time
    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end - start);

    // print in table format
    cout << "| " << filename << " | " << duration.count() << " | " << result << " | " << root << " | " << endl;

    return 0;
}
#include <chrono>