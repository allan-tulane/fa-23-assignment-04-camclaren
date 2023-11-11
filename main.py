import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    length_S = len(S)
    length_T = len(T)
    
    med = []
    for i in range(length_S + 1):
        row = []
        for j in range(length_T + 1):
            row.append(0)
        med.append(row)
    
    for i in range(length_S + 1):
        for j in range(length_T + 1):
            if i == 0:
                med[i][j] = j
            elif j == 0:
                med[i][j] = i
            elif S[i - 1] == T[j - 1]:
                med[i][j] = med[i - 1][j - 1]
            else:
                med[i][j] = 1 + min(med[i][j - 1])
    pass

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    fMED = fast_MED(S, T)
    new_S = []
    new_T = []
    i = len(S)
    j = len(T)
    while True:
      if(i == 0 and j==0):
        break
      else:
        insert = fMED[i][j-1]
        remove = fMED[i-1][j]
        sub = fMED[i-1][j-1]
        minimum = min(insert,remove,sub)
        if(sub == minimum):
          new_S = [S[i-1]] + new_S
          new_T = [T[j-1]] + new_T
          i = i-1                        
          j = j-1
        elif(insert == minimum):
          new_S = ['-'] + new_S
          new_T = [T[j-1]] + new_T
          j = j-1
        elif(remove == minimum):
          new_T = ['-'] + new_T
          new_S = [S[i-1]] + new_S
          i = i-1
    
    s_str = "".join(new_S) 
    t_str = "".join(new_T)
    
    return s_str, t_str

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
