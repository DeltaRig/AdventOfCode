// 2026 March 22
// Daniela Rigoli
// C++

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

unordered_map<char, string> dic;
unordered_map<char, string> memo;

set<char> keys;
set<char> appearsInValue;

// recursive function
string descompress(const string text) {
    string result = "";

    for (char ch : text) {
        if (dic.count(ch)) { // used to check for the presence of a specific key within the container
            if (memo.count(ch)) { // already descompress before
                result += memo[ch];
            } else {
                string expanded = descompress(dic[ch]);
                memo[ch] = expanded;
                result += expanded;
            }
        } else {
            result += ch;
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

    char root;

    for (char k : keys) {
        if (!appearsInValue.count(k)) {
            root = k;
            break;
        }
    }

    if (root) {
        cout << "Root: " << root << endl;
    } else {
        cout << "No Root Found" << endl;
    }

    cout << "Here " << (dic.count('m') ? "true" : "false") << endl;

    cout << "Dicionario criado" << endl;

    string result = descompress(string(1, root));

    //cout << result << endl;
    cout << "Qnt caracteres " << result.length() << endl;

    return 0;
}
