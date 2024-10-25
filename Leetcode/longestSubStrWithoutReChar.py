# # Medium Leecode
# # 3. Longest SubString Without Repeating Characters 

# def lengthOfLongestSubstring(s: str) -> int:
    
#     store = []
#     lent = len(s)
#     lengthCurr = 0 
#     result = 0 
    
#     def loop(start, lent, store, result, lengthCurr):
#         global res
#         for i in range(start, lent):
#             if s[i] not in store:
#                 lengthCurr += 1
#                 store.append(s[i])
#             else:
#                 break
#         if lengthCurr > result:
#             result = lengthCurr
            
#         if i == lent-1:
#             # print(result) 
#             res = result
#             return 
        
#         lastIdx = i
#         lengthCurr = 0
#         store = []
        
#         while s[i-1] != s[lastIdx]:
#             i = i - 1
#         loop(i, lent, store, result, lengthCurr)

#     loop(start=0, lent=lent, store=store, result=result, lengthCurr=lengthCurr)    
#     return res
            
# print(lengthOfLongestSubstring(s="pwwkew"))
                          # 0123456789

def lengthOfLongestSubstring(s: str) -> int:
 
    store = tuple()
    lent = len(s)
    lengthCurr = 0 
    result = 0
    idx = 0
    
    while True:
        if idx > lent - 1:
            if lengthCurr > result:
                result = lengthCurr
            return result
        
        if s[idx] not in store:
            store += (s[idx],)
            lengthCurr += 1
            idx += 1
        else:
            if lengthCurr > result:
                result = lengthCurr
            store = tuple()
            lengthCurr = 0
                
            idxFind = idx
            while s[idx-1] != s[idxFind]:
                idx = idx - 1
print(lengthOfLongestSubstring("abcabcbbb"))            
         