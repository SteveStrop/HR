

def ali():
    scores = [100, 90, 90, 80, 75, 60]
    alice = [50, 65, 77, 90, 102]

    result=[]
    scores = sorted(set(scores))
    scores.append(-1)
    #print(scores)
    n=0
    for a in alice:
        for i in range(n,len(scores)):
            #print(f'alice: {a} current score {scores[i]}')
            if a <= scores[i]:
                result.append(i+1)
                n=i
                break
    return sorted(result,reverse=True)

print(ali())
