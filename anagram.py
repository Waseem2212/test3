# anagram problem
def anagram(strs):
    anagram_dic = {}
    for i in strs:
        sorted_str = "".join(sorted(i))
        if sorted_str in anagram_dic:
            anagram_dic[sorted_str].append(i)
        else:
            anagram_dic[sorted_str] = [i]
    return list(anagram_dic.values())

str1 = ['eat','tea','tan','nat']
res = anagram(str1)
print(res)