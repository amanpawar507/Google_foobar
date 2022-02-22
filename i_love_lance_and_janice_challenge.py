def solution(x):
    str_len = len(x)
    my_str=[]
    for i in range (str_len):
        current = x[i]
        if 'a' <= current <= 'z':
            position = ord('z')-ord(current)
            my_str.append(chr(ord('a')+position))
        else:
            my_str.append(current)
    return ''.join(my_str)

if __name__ == "__main__":
    t1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print(solution(t1))

    t2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    print(solution(t2))