def merge(string,k):
    n=len(string)
    for i in range(0,n,k):
        res_seq = []
        sub_seg=list((string[i:i + k]))
        res_seq.append(sub_seg[0])
        for j in range(1,k):
            if sub_seg[j] not in res_seq:
                res_seq.append(sub_seg[j])
        print(''.join(res_seq))

