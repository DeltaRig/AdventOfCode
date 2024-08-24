
Input: "S_n = \sum_{i=0}^{n} x^{i}"
Than should print the steps
"S_{n+1} = \sum_{i=0}^{n+1} x^{i}"
"S_n + x^{n+1} = \sum_{i=0}^{n+1} x^{i}"
"S_{n}+x^{n+1} = x^0 + \sum_{i=1}^{n+1} x^{i}"
"S_{n}+x^{n+1} = 1 + \sum_{i=0}^{n} x^{i+1}"
"S_{n}+x^{n+1} = 1 + x * S_{n}"
Isolation
"x*S_{n}-S_{n}=x^{n+1}-1"
"S_{n}*(x-1)=x^{n+1}-1"
"S_{n}=\frac{x^{n+1}-1}{(x-1)}"

Other sample:
Input: "S_n = \sum_{i=1}^{n} 2^{i}"
Than should print the steps
"S_{n+1} = \sum_{i=1}^{n+1} 2^{i}"
"S_{n} + 2^{n+1} = \sum_{i=1}^{n+1} 2^{i}"
"S_{n}+2^{n+1} = x^1 + \sum_{i=2}^{n+1} 2^{i}"
"S_{n}+2^{n+1} = 2 + \sum_{i=1}^{n} 2^{i+1}"
"S_{n}+2^{n+1} = 2 + 2 * S_{n}"
Isolation
"2*S_{n}-S_{n}=2^{n+1}-2"
"S_{n}=2^{n+1}-2"

Input: S_n = \sum_{i=0}^{n} a*x^{i}
S_{n+1} = \sum_{i=0}^{n+1} a*x^{i}
S_n + (a*x^{n+1}) = \sum_{i=0}^{n+1} a*x^{i}
S_n + (a*x^{n+1}) = (a*(x^{0})) + \sum_{i=1}^{n+1} a*x^{i}
S_n + (a*x^{n+1}) = (a*(x^{0})) + \sum_{i=0}^{n} a*x^{i+1}
S_n + (a*x^{n+1}) = (a*(x^{0})) + a*x * \sum_{i=0}^{n} a*x^{i}
S_n + (a*x^{n+1}) = (a*(x^{0})) + a*x * S_n
Isolation
a*x * S_n - S_n = (a*x^{n+1}) - (a*(x^{0}))
S_n = \frac{(a*x^{n+1}) - (a*x^{0})}{(a*x) - 1}
S_n = \frac{(a*x^{n+1}) - (a*1)}{(a*x) - 1}

Step 1 verify the regex
                  1                        2          3       4         5
pattern = r'S_(([a-zA-Z]))\s*=\s*\\sum_{([a-zA-Z])=(\d+)}\^\{(n)\}\s*(\w+)+\s*'
Step 2 create the groups
# Extract the starting index and the summation term
size = match.group(1) should be quals to match.group(4)
start_letter = match.group(2)  # Letter index of the summation (i, k, etc.)
start_index_l = match.group(3)  # Letter index of the summation 
start_index_i = int(match.group(3))  # Start index of the summation 
term = int(match.group(5))  # The summation term (e.g., 'a*x^i', 'x^i', 'i*2^{i-1}', etc.)

Step 3 Organize the calcule adding +1 at n like
"S_{n+1} = \sum_{i=0}^{n+1} x^{i}"

Step 4 From left side remove the +1 at the n considering that "S_{n} = \sum_{i=0}^{n} x^{i}", se if we are removing the last one will be:
"S_{n} + x^{n+1} = \sum_{i=0}^{n+1} x^{i}"
For step 4 you can check at term where the start index appears to know what replace to n+1

Step 5. Change the value of the start index sum -1 then resume the first part of the summation like bellow:
"S_{n}+x^{n+1} = x^0 + \sum_{i=1}^{n+1} x^{i}"
Using x^0 in this sample because before was i=0, that could be reduce to 1 because any value elevado a 0 will be 1 (use a method to verify this reductions)
If i=1 then it result at x^1
In general way use the information where the start index appears at term to know what replace to start_index_i

Step 6. Reduce 1 at indexs (start and end) and add +1 where is the index letter at the term, like bellow:
"S_{n}+x^{n+1} = 1 + \sum_{i=0}^{n} x^{i+1}"

Step 7. Remove the plus 1 from the index and move the value to out the summation, if is an multiplication it could be moved multipling, because x^{i+1} = x^{i} * x
"S_{n}+x^{n+1} = 1 + x * \sum_{i=0}^{n} x^{i}"

Step 8. Reconize that "S_{n} = \sum_{i=0}^{n} x^{i}" and replace
"S_{n}+x^{n+1} = 1 + x * S_{n}"

Isolation, we will try isolate the S_{n}
"x*S_{n}-S_{n}=x^{n+1}-1"
"S_{n}*(x-1)=x^{n+1}-1"
If you have multiplication it will generate an fraction in the other side to isolate for complete
If you have fraction it will generate an fraction in the other side to isolate for complete
If you have and plus it will generate and sum in the other side
If you have and minimization it will generate and plus in the other side
"S_{n}=\frac{x^{n+1}-1}{(x-1)}"

