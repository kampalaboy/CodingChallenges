#s and t where shortest substring of s contains all characters of t
from collections import Counter
def window(s,t):
    n, m = len(s), len(t)
    if m > n or t =="":
        return ""
    freqt = Counter(t)
    start, end = 0, n
    qauli = 0
    freqs = Counter()
    l = 0
    for r in range(n):
        freqs[s[r]] += 1
        if s[r] in freqt and freqs[s[r]] == freqt[s[r]]:
            qauli +=1
        if qauli == len(freqt):
            while s[l] not in freqt or freqs[s[l]] > freqt[s[l]]:
                freqs[s[l]] -= 1
                l +=1
            if r-l+1 < end-start+1:
                start, end = l,r
    return s[start:end+1] if end-start+1 <= n else "" 