from collections import defaultdict
import heapq

def pairNule(a, b):
    if a == 'U' and (b == 'A' or b == 'G'):
        return True
    if a == 'G' and (b == 'C' or b == 'U'):
        return True
    if a == 'C' and b == 'G':
        return True
    if a == 'A' and b == 'U':
        return True
    return False

#   First Version of Best (has duplication)
def best_dup(sequence, opt=defaultdict(int)):

    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        elif len(sequence) == 0:
            opt[sequence] = (0, '')
        else:
            max_pair, str_pair, l = 0, '', len(sequence)
            #   best(i+1, j-1) + 1
            if pairNule(sequence[0], sequence[l-1]) == True:
                pre_max, pre_res = best_dup(sequence[1:l-1])
                max_pair = 1 + pre_max
                str_pair = '(' + pre_res + ')'
            #   max (best(i,k) + best(k+1,j))
            for k in range(1, l-1):
                pre_max_1, pre_res_1 = best_dup(sequence[:k])
                pre_max_2, pre_res_2 = best_dup(sequence[k:])
                if pre_max_1 + pre_max_2 > max_pair:
                    max_pair = pre_max_1 + pre_max_2
                    str_pair = pre_res_1 + pre_res_2
            opt[sequence] = (max_pair, str_pair)
    return opt[sequence]

#   Second version for best and total
def best(sequence, opt=defaultdict(int)):
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = (0, '.')
        elif len(sequence) == 0:
            opt[sequence] = (0, '')
        else:
            max_pair, str_pair, l = 0, '', len(sequence)
            #   best(i+1, j)
            pre_max, pre_res = best(sequence[1:])
            max_pair = pre_max
            str_pair = '.' + pre_res
            #   max(1+best(1,k)+best(k+1, j))
            for k in range(1, l):
                if pairNule(sequence[0], sequence[k]):
                    pre_max_1, pre_res_1 = best(sequence[1:k])
                    pre_max_2, pre_res_2 = best(sequence[k+1:])
                    if 1 + pre_max_1 + pre_max_2 > max_pair:
                        max_pair = 1 + pre_max_1 + pre_max_2
                        str_pair = '(' + pre_res_1 + ')' + pre_res_2
            opt[sequence] = (max_pair, str_pair)
    return opt[sequence]


def total(sequence, opt=defaultdict(int)):
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = 1
        elif len(sequence) == 0:
            opt[sequence] = 1
        else:
            sum, l = 0, len(sequence)
            #   best(i+1, j)
            sum += total(sequence[1:])
            #   max(1+best(1,k)+best(k+1, j))
            for k in range(1, l):
                if pairNule(sequence[0], sequence[k]):
                    sum += total(sequence[1:k]) * total(sequence[k+1:])
            opt[sequence] = sum
    return opt[sequence]


def kbest(sequence, k, opt=defaultdict(int)):
    if sequence not in opt:
        if len(sequence) == 1:
            opt[sequence] = [(0, '.')]
        elif len(sequence) == 0:
            opt[sequence] = [(0, '')]
        else:

            h, matrix, used, length = [], [], set(), len(sequence)

            arr = kbest(sequence[1:], k)
            heapq.heappush(h, (-arr[0][0], '.'+arr[0][1], 0, 0))
            matrix.append((sequence[1:]))
            used.add((sequence[1:], 0))

            matrix_length = 1
            for l in range(1, length):
                if pairNule(sequence[0], sequence[l]):
                    left_arr = kbest(sequence[1:l], k)
                    right_arr = kbest(sequence[l+1:], k)
                    heapq.heappush(h, (-(left_arr[0][0]+right_arr[0][0]+1), '('+left_arr[0][1]+')'+right_arr[0][1], matrix_length, 0, 0))
                    
                    matrix.append((sequence[1:l], sequence[l+1:]))
 #                   print(sequence[1:l], sequence[l+1:])
                    used.add((sequence[1:l], sequence[l+1:], 0, 0))
                    matrix_length += 1

            res = []
            while(len(res) < k and len(h) != 0):
                obj = heapq.heappop(h)
                res.append((-obj[0], obj[1]))
                matrix_id = obj[2]
                #   in 1-D situation, not matrix
                if matrix_id == 0:
                    idx = obj[3]
                    arr = kbest(matrix[0], k)
                    if idx+1 < len(arr) and (matrix[0], idx+1) not in used:
                        heapq.heappush(h, (-arr[idx+1][0], '.'+arr[idx+1][1], 0, idx+1))
                        used.add((matrix[0], idx+1))
                # in matrix
                else:
                    left_idx, right_idx = obj[3], obj[4]
                    left_arr = kbest(matrix[matrix_id][0], k)
                    right_arr = kbest(matrix[matrix_id][1], k)
                    if left_idx+1 < len(left_arr) and (matrix[matrix_id][0], matrix[matrix_id][1], left_idx+1, right_idx) not in used:
                        heapq.heappush(h, (-(left_arr[left_idx+1][0] + right_arr[right_idx][0] + 1),
                                           '('+left_arr[left_idx+1][1]+')'+right_arr[right_idx][1], matrix_id,
                                           left_idx+1, right_idx))
                        used.add((matrix[matrix_id][0], matrix[matrix_id][1], left_idx+1, right_idx))
                    if right_idx+1 < len(right_arr) and (matrix[matrix_id][0], matrix[matrix_id][1], left_idx, right_idx+1) not in used:
                        heapq.heappush(h, (-(left_arr[left_idx][0] + right_arr[right_idx+1][0] + 1),
                                           '(' + left_arr[left_idx][1] + ')' + right_arr[right_idx+1][1], matrix_id,
                                           left_idx, right_idx+1))
                        used.add((matrix[matrix_id][0], matrix[matrix_id][1], left_idx, right_idx+1))

            opt[sequence] = res
  #  print(opt)
    return opt[sequence]


if __name__ == '__main__':
    '''
    print(best("AU"))
    print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))
    print(best("ACAGU"))
    print(best("GCACG"))
    print(best("UUCAGGA"))
    print(best("AGGCAUCAAACCCUGCAUGGGAGCG"))

    print(total("ACAGU"))
    '''
    # print(kbest("ACGCG", 5))
 #  print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
   # print(kbest("GAUGCCGUGUAGUCCAAAGACUUC",10))
 #   print(kbest("AGGCAUCAAACCCUGCAUGGGAGCG", 10))
