#輸入英文單字，記算單字數量，按字母排序


from collections import Counter
word= input("請輸入英文單字:")

mydict=Counter(word)

print(sorted(mydict.items(), key=lambda x:x[0]))
