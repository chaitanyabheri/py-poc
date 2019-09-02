

daily_balances = [107.92, 108.67, 109.86, 110.15]


#for i in daily_balances:
    #print(i)

#print (daily_balances[1:2])

#print(daily_balances[::-1])


# reverse string
def reverse(x):
    if x > 0:
        s = str(x)
        r = s[::-1]

        for pos in range(len(s)):
            x = s[pos]
    print(x)

# reverse integer




### Execution results

#print(reverse(123))







def reverseString(s):
    r = (s[::-1])
    for pos in range(len(r)):
        s[pos] = r[pos]


s= ['h','e','l']

reverseString(s)



class Solution:
    @staticmethod

    def reverseStringChar(s):
        """
        reverse string with array of characters

        """
        r = (s[::-1])
        for pos in range(len(r)):
            s[pos] = r[pos]
        print(s)

    def reverseString(s):
        l = len(s)
        r = s[::-1]

        print(r)

    def reverseStrings2(s):
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]

    def reverse32SignedInt(num):
        r=0
        if num >0:
           r=str(num)[::-1]
        else:
            r = '-' + str(num)[1::][::-1]

        if int(r) < -2**31:
            return(0)
        elif int(r ) > 2**31 +1:
            return(0)
        else:
            return(int(r))

    def FirstUniqLowerStringChar(s):
        if s.islower():
            for index in range(0,len(s)):
                if (s.count(s[index])==1):
                    return index
                    break
                elif index == len(s)-1:
                    return -1
        else:
            return -1

    def isAnagram(s1, s2):
        def isAnagram(self, s: str, t: str) -> bool:
            if (sorted(list(s)) == sorted(list(t))):
                return True
            else:
                return False

    def isPalindrome (s):
        l = [letter.lower() for letter in s if letter.isalnum()]
        print(l)
        return l[::-1]==l

    def isPlaindromeSol2(s):
        l=[]
        for letter in s:
            if letter.isalnum():
                l.append(letter.lower())
        print(l)
        return l[::-1]==l

    def myAtoi(s):
        s= s.lstrip()
        pos_st = -1
        res = ''

        if len(s)<=1 and not s.isnumeric():
            return 0
        else:

            for index in range(0,len(s)):
                if -1 < pos_st < index and not s[index].isnumeric():
                    break

                if s[index].isnumeric():
                    if pos_st == -1:
                        pos_st = index

                    res = res + s[index]

            if s[pos_st -1]=='-':
                res = '-' + res

        return int(res)

    def LongestCommonPrefixOS(strs):
        import os
        return os.path.commonprefix(strs)

    def LongestCommonPrefix(self, strs):
        longest_pre = ""
        if not strs: return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i + 1]) for x in strs]):
                longest_pre = shortest_str[:i + 1]
            else:
                break
        return longest_pre

    def ReverseString2(l):
        '''
        convert to string
        split the split
        reverse each part
        append values for each word until end of words
        :return:
        '''
        s = ''
        r = ''

        for i in range(0, len(l)):
            s = s + l[i]
            # print (l[i])

        r = (s[::-1])

        # print(r)
        l[:] = []

        for word in r.split(' '):
            (l.extend(list(word[::-1])))
            l.extend(' ')

        print('method-',l.pop())
        #return l

    def twoSum(self, nums , target):
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                idx = nums.index(target - nums[i])
                if i == idx:
                    pass
                else:
                    return [i, idx]

    def maxSubArrayLen(self, nums, k):
        """
        https://nb4799.neu.edu/wordpress/?p=2219
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        max_res = 0
        # key: sum of all elements so far, value: the index so far
        sum_map = dict()

        for i, n in enumerate(nums):
            sum += n
            if sum == k:
                max_res = i + 1
            elif sum_map.get(sum - k, None) is not None:
                max_res = max(max_res, i - sum_map[sum - k])
            # if sum already exists in sum_map, its index should be
            # smaller than the current index. Since we want to find
            # the maximum length of subarray, the smaller index
            # should be kept.
            if sum_map.get(sum, None) is None:
                sum_map[sum] = i

        return max_res

    def compareVersion(self,  version1,   version2):
        '''
        https://blog.csdn.net/coder_orz/article/details/51313015
        :param version1:
        :param version2:
        :return:
        '''
        if version1 == version2:
            return 0

        ind_1 = version1.find('.')
        ind_2 = version2.find('.')
        part_1 = version1[0:ind_1] if ind_1 != -1 else version1
        part_2 = version2[0:ind_2] if ind_2 != -1 else version2

        if int(part_1) == int(part_2):
            remain_1 = version1[len(part_1) + 1:] if version1[len(part_1) + 1:] != '' else '0'
            remain_2 = version2[len(part_2) + 1:] if version2[len(part_2) + 1:] != '' else '0'
            return self.compareVersion(remain_1, remain_2)
        else:
            return 1 if int(part_1) > int(part_2) else -1

    def findKthLargest(self, nums, k) :

        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return (nums[-k])

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        blocks = IP.split('.')
        if len(blocks) == 4:
            for i in range(len(blocks)):
                if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
                        (blocks[i][0] == '0' and len(blocks[i]) > 1):
                    return "Neither"
            return "IPv4"

        blocks = IP.split(':')
        if len(blocks) == 8:
            for i in range(len(blocks)):
                if not (1 <= len(blocks[i]) <= 4) or \
                        not all(c in string.hexdigits for c in blocks[i]):
                    return "Neither"
            return "IPv6"
        return "Neither"

    def isValidIP(inp):
        if '.' in inp and len(inp.split('.')) == 4 and all(
                c.isdigit() and str(int(c)) == c and int(c) in range(0, 256) for c in inp.split('.')):
            return True
        else:
            return False

    def majorityElement(self, nums):
        '''
        http://bookshadow.com/weblog/2015/06/29/leetcode-majority-element-ii/
        :param nums:
        :return:
        '''
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1, c2 = c1 - 1, c2 - 1
        size = len(nums)
        return [n for n in (n1, n2)
                if n is not None and nums.count(n) > size / 3]

#### Duplicates
    def remove_dup(s):
        r = []
        for i in s:
            print(i)
            if i not in r:
                r.append(i)
            print(r)
        print(r)

    def remove_dup_by_comprehension(s):
        res = []
        [res.append(x) for x in test_list if x not in res]

    def remove_dup_set(s):
        return list(set(s))

    def remove_dup_dict(s):
        d = {}
        for i in s:
            if i in d.keys():
                s.pop(i)
            else:
                d[i] = i
            # print(i,d,s)
        return (s)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))

    def isPrime(n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True

            # This is checked so that we can skip
            # middle five numbers in below loop
        if (n % 2 == 0 or n % 3 == 0):
            return False

        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6

        return True

        #print(s)

    def consecutive_dups(test_list):
        #https://www.geeksforgeeks.org/python-remove-consecutive-duplicates-from-list/
        from itertools import groupby

        # initializing list
        test_list = [1, 4, 4, 4, 5, 6, 7, 4, 3, 3, 9]

        # printing original list
        print("The original list is : " + str(test_list))

        # using groupby() + list comprehension
        # removing consecutive duplicates
        res = [i[0] for i in groupby(test_list)]

        # printing result
        print("The list after removing consecutive duplicates : " + str(res))

    def remove_non_values(l):
        #https: // www.geeksforgeeks.org / python - remove - none - values -
        #from
        #-list /

        #
        res = []
        for val in test_list:
            if val != None:
                res.append(val)

    def remove_non_values_filter(l):
        res = list(filter(None, l))

    def remove_all_digits(s):
        from string import digits

        list = [''.join(x for x in i if x.isalpha()) for i in list]

        return list

        # Driver code

        list = ['4geeks', '3for', '4geeks']
        print(remove(list))

    def remove_last_k_elements(s):
        res = test_list[: -K or None]





s=[2,2, 4, 10, 20, 5, 2, 20, 4]
print(s)
Solution.remove_dup(s)
print(s)




#print ('-----end of line')
'''
l = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(l)
(Solution.ReverseString2(l))

#print(l)







if s[0]=='-':
    s = s[1::]

l = [letter for letter in s if letter != ' ']

print(l)
'''
'''

# 1st to last check




########## Execution results ##########
print('\n-------- Execution Results ------')

'''
##Palindrome example
print (Solution.isPlaindromeSol2('rannar'))

print (Solution.isPlaindromeSol1('A man, a plan, a canal: Panama'))


s='llbbdd'
print('Print 1st Unique Char-->\ninput:',s,', Output:', Solution.FirstUniqLowerStringChar(s))


s= ['h','e','l','l']
#print ('\nReverse String--->\nInput-\n',s, '\nOutput-'), Solution.reverseStringChar(s)
s = 'Hello'
#print ('\nReverse String--->\nInput-\n',s, '\nOutput-'), Solution.reverseString(s)

num_list = [123,-123,120,-525,-120, 12345678999, -123456789]
print ('Reverse 32 singed int')
for n in num_list:
    num = int(n)
    print ('input:', num , 'output:',Solution.reverse32SignedInt(num))
'''





