"""Targeted arithmetic verification of one cyclic-routing counterexample."""
def minimum(word, n=1):
    layer=0; result=0; N=len(word)
    for i,ch in enumerate(word):
        if i and word[i-1:i+1]=='ba': result+=9*(N-i)
        if ch=='|': layer+=1
        elif ch=='a': result+=3*n+2+3*layer
        else: result+=6*n+7-3*layer
    return result

w='|bab|'
rotations=[w[i:]+w[:i] for i in range(len(w))]
values=[minimum(v) for v in rotations]
assert values==[55,67,25,40,43]
assert all(v>37 or (37-v)%9 for v in values)
assert (37%3,(1+2+2)%3)==(1,2)
assert 14+8+10+10==42
assert 6+10+10+11==37
print('rotation minima',values,'source 37; branch-specific target 37')
