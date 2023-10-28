class Solution:
    def reverseVowels(s: str) -> str:
        length = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        v_in_word = []
        pos = []

        for i in range(length):
            if s[i].lower() in vowels:
                pos.append(i)
                v_in_word.append(s[i])
        if pos:
            pos_length = len(pos)
            temp = []
            mut_s = list(s)
            for j in range(pos_length):
                rev = pos_length-j-1
                temp.append(pos[rev])
                print(rev)

            for k in range(pos_length):
                mut_s[temp[k]] = v_in_word[k]
            s = "".join(mut_s)
            print(s)
            return s
        else:
            return ""

        # print(v_in_word)
        # print(pos)
        # print(temp)
        # print(s)

    reverseVowels("123456")
    reverseVowels("hello")
