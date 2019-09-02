## Palindrome Pairs

# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

def palindromePairs(words):
    lookup = {w: i for i, w in enumerate(words)}
    res = []
    for i, w in enumerate(words):
        for j in range(len(w) + 1):
            pre, pos = w[:j], w[j:]
            if pre == pre[::-1] and pos[::-1] != w \
                    and pos[::-1] in lookup:
                res.append([lookup[pos[::-1]], i])
            if j != len(w) and pos == pos[::-1] \
                    and pre[::-1] != w and pre[::-1] in lookup:
                res.append([i, lookup[pre[::-1]]])

    return res

# Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.
# O (n^2)
def longestPalindrome(s):  # O(n)
    if len(s) == 0:
        return ""
    maxLen = 1
    start = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen

print(longestPalindrome('babad'))


# longest palindrome

def longestPalindrome(self, s: str) -> int:
    dic = {}
    for char in s:
        dic[char] = dic.get(char, 0) + 1

    length = 0
    has_odd = False
    for key in dic:
        if dic[key] % 2 == 0:
            length += dic[key]
        else:
            has_odd = True
            length += dic[key] - 1

    return length + 1 if has_odd else length

# shortest palindrome
# https://leetcode.com/problems/shortest-palindrome/discuss/60250/My-recursive-Python-solution
def shortestPalindrome(self, s: str) -> str:
    if not s or len(s) == 1:
        return s
    j = 0
    for i in reversed(range(len(s))):
        if s[i] == s[j]:
            j += 1
    return s[::-1][:len(s) - j] + self.shortestPalindrome(s[:j - len(s)]) + s[j - len(s):]

#ispalindrome
def isPalindrome(s):
    l = [letter.lower() for letter in s if letter.isalnum()]
    print(l)
    return l[::-1] == l

## is signed number a palindrome
def isPalindrome(self, x):
    if x < 0:
        return False

    ranger = 1
    while x / ranger >= 10:
        ranger *= 10

    while x:
        left = x / ranger
        right = x % 10
        if left != right:
            return False

        x = (x % ranger) / 10
        ranger /= 100

    return True

# validate palindrome sentence
def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

#validae palindrome (remove character)
#https://leetcode.com/problems/valid-palindrome-ii/
def validPalindrome(self, s: str) -> bool:
    # Time: O(n)
    # Space: O(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True


''''   Paranthesis   '''

#https://leetcode.com/problems/valid-parentheses/submissions/
def isValidParanthesis(s):
# create mapping
# create open bracket set
# for each new open add to stack
# if close check result mapping --> true pop
# false break
# check result with empty
    bracket_map = {'{': '}', '(': ')', '[': ']'}
    open_brac = set(['[', '(', '{'])

    stack = []

    for char in s:
        if char in open_brac:
            stack.append(char)
        elif stack and char == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False

    return stack == []

#remove invalid parathesis
#https://leetcode.com/problems/remove-invalid-parentheses/discuss/75090/Python-DFS-Solution
def removeInvalidParentheses(self, s):
    res = []
    self.visited = set([s])
    self.dfs(s, self.invalid(s), res)
    return res

def dfs(self, s, n, res):
    if n == 0:
        res.append(s)
        return
    for i in range(len(s)):
        if s[i] in ('(', ')'):
            new_s = s[:i] + s[i + 1:]
            if new_s not in self.visited and self.invalid(new_s) < n:
                self.visited.add(new_s)
                self.dfs(new_s, self.invalid(new_s), res)

def invalid(self, s):
    plus = minus = 0
    memo = {"(": 1, ")": -1}
    for c in s:
        plus += memo.get(c, 0)
        minus += 1 if plus < 0 else 0
        plus = max(0, plus)
    return plus + minus



''''' REVERSE String '''
# reverse integer #https://leetcode.com/problems/reverse-integer/
def reverseNumber(self, x):
    if not x:
        return x
    sign = x / abs(x)
    x *= sign
    res = 0
    while x:
        res = res * 10 + x % 10
        x /= 10
    if res < 1 << 31:
        return res * sign
    else:
        return 0

def reverseNumber2(self, x):
    """
    :type x: int
    :rtype: int
    """
    sign = [1, -1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0

#https://leetcode.com/problems/reverse-string/
def reverseString(s):
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]

#https://leetcode.com/problems/reverse-string-ii/
def reverseStringByPosition(self, s, k):
    s = list(s)
    for i in xrange(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)


#revere only letters https://leetcode.com/problems/reverse-only-letters/
def reverseOnlyLetters(self, S: str) -> str:

    """
    :type S: str
    :rtype: str
    """
    S = list(S)
    l, r = 0, len(S) - 1

    while l < r:
        if not S[l].isalpha():
            l += 1
        elif not S[r].isalpha():
            r -= 1
        else:
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
    return ''.join(S)

''''' REVERSE words '''
#https://leetcode.com/problems/reverse-words-in-a-string/
def reverseWordsinString(self, s: str) -> str:
    return ' '.join(s.split()[::-1])


# reverseWordsInString https://leetcode.com/problems/reverse-words-in-a-string-ii/submissions/
def reverseWords( s):
    reverse(s, 0, len(s) - 1)

    beg = 0
    for i in range(len(s)):
        if s[i] == ' ':
            reverse(s, beg, i-1)
            beg = i + 1
        elif i == len(s) -1:
            reverse(s, beg, i)
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

# reverse sentence https://leetcode.com/problems/reverse-words-in-a-string-iii/
def reverseWords(self, s: str) -> str:
    # def reverseWords(self, s: str) -> str
    s = s.split(' ')  # creates a list of words
    reverse = []  # reversed words will be stored here
    for word in s:
        reverse.append(word[::-1])  # adds reversed word to the reverse list
        result = ' '.join(reverse)  # joins words with a space
    return result

#https://leetcode.com/problems/compare-version-numbers/submissions/
def compareVersion(self, version1, version2):
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


'''  swapping ovels '''
#https://leetcode.com/problems/reverse-vowels-of-a-string/
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    L = list(s)
    i = 0
    j = len(L) - 1
    while i < j:
        while i < j and L[i] not in vowels:
            i += 1
        while j > i and L[j] not in vowels:
            j -= 1
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    return ''.join(L)

def removeVowels(self, S: str) -> str:
    s = set('aeiou')
    ret = ""
    for ch in S:
        if ch not in s:
            ret += ch
    return ret

def swap_oval_first_last_letter_while (v1):
    print('\n-------Swap 1st oval with last oval in letter')
    i=0
    l = len(v1)
    vowels = ['a','e','i','o','u']

    while i<l:
        #print ( v1[i] )
        if v1[i] in ('a','e','i','o','u'):
            letter1 = v1[i]
            pos1 = i
            break

        #v2 = v2+ v1[i]
        #print (v2)
        i= i+1

    #2nd oval
    i=-1

    while i>-l:
        #print ( v1[i] )
        if v1[i] in ('a','e','i','o','u'):
            letter2 = v1[i]
            pos2 = i
            break

        #v2 = v2+ v1[i]
        #print (v2)
        i= i-1

    pos2 = l + pos2

    #print ('\n1st oval details ', letter1, pos1)
    #print ('\n2nd oval details ', letter2, pos2)
    #replace values

   # i=-1
    #
   # v2=''
   # i=0

    #while i<l:
    #    #print ( v1[i] )
    #    if i ==pos1:
    #        v2 = v2+letter2
    #    elif i ==pos2:
    #        v2 = v2+ letter1
    #    else:
    #        v2 = v2  +v1[i]
    #    #print (v2, i, pos1,pos2)
#
    #    #v2 = v2+ v1[i]
    #    #print (v2)
    #    i= i+1
#
    #print ('\n1st oval details ', letter1, pos1)
    #print ('\n2nd oval details ', letter2, pos2)
    #print ('\n1st letter ', v1)
    #print ('\n2nd letter ', v2)

    # swap characters

    strlist = list(v1)

    strlist[pos1],strlist[pos2] =strlist[pos2], strlist[pos1]

    #print(strlist)
    v2= ("".join(strlist))
    print ('input', v1)

    return(v2)

def swap_oval_first_last_letter_join(word):
    print('\nSwap 1st oval with last with joins')
    print (word)
    vowels =['a','e','i','o','u']
    vList = []
    word= list(word)

    for letter in word:
        if letter in vowels:
            vList.append(word.index(letter))

    word[vList[0]], word[vList[-1]]=word[vList[-1]], word[vList[0]]

    word = (''.join(word))

    return (word)


# Create utility fn for common prefix between 2 strings
def CommonPrefixUtil(str1, str2):
    result = ''

    i = 0
    j = 0

    while i <= len(str1) - 1 and j <= len(str2) - 1:
        if str1[i] != str2[j]:
            break

        result += str1[i]
        i = i + 1
        j = j + 1

    return (result)

    # common prefix for array or strings

def longestCommonPrefix(strs):
    if (len(strs)) == 0:
        return ''

    prefix = strs[0]
    for i in range(1, len(strs)):
        prefix = CommonPrefixUtil(prefix, strs[i])

    return (prefix)


# characater matching
# https://www.geeksforgeeks.org
# /longest-common-prefix-using-character-by-character-matching/
# get length of min word
# for each character until min length
# for each word in list until that length
# check value matches
# T --> O(N M) N = Number of strings M =  Length of the largest string string
# Space  -->  O(M).
def longestCommonPrefix(strs):
    def findminLen(strs):
        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if (len(strs[i]) < min_len):
                min_len = len(strs[i])

        return (min_len)

    min_l = findminLen(strs)

    result = ''

    for i in range(min_l):
        current = strs[0][i]

        for j in range(1, len(strs)):
            if (strs[j][i] != current):
                return result
        result = result + current

    return (result)


# merge linked list https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1, l2):
    result = ListNode(None)
    temp = result

    while l1 and l2:
        if (l1.val <= l2.val):
            temp.next = l1
            l1 = l1.next
            temp = temp.next
        else:
            temp.next = l2
            l2 = l2.next
            temp = temp.next

    temp.next = l1 or l2
    return result.next



def containsNearbyDuplicate(self, nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False

# Binary Search
def SearchInsert(nums, num):
    return BinarySearch(nums, 0, len(nums) - 1, num)


def BinarySearch(nums, st, end, num):
    if st < end:

        mid = (st + end) // 2

        if nums[mid] == num:
            return mid

        elif nums[mid] > num:
            return BinarySearch(nums, st, mid, num)
        else:
            return BinarySearch(nums, mid + 1, end, num)

    if nums[st] == num:
        return st
    if nums[end] == num:
        return end
    if nums[end] < num:
        return end + 1
    if nums[st] > num:
        return st
    else:
        return st + 1


def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


def FirstUniqLowerStringChar(s):
    if s.islower():
        for index in range(0, len(s)):
            if (s.count(s[index]) == 1):
                return index
                break
            elif index == len(s) - 1:
                return -1
    else:
        return -1


def isAnagram(s1, s2):
    def isAnagram(self, s: str, t: str) -> bool:
        if (sorted(list(s)) == sorted(list(t))):
            return True
        else:
            return False


def myAtoi(s):
    s = s.lstrip()
    pos_st = -1
    res = ''

    if len(s) <= 1 and not s.isnumeric():
        return 0
    else:

        for index in range(0, len(s)):
            if -1 < pos_st < index and not s[index].isnumeric():
                break

            if s[index].isnumeric():
                if pos_st == -1:
                    pos_st = index

                res = res + s[index]

        if s[pos_st - 1] == '-':
            res = '-' + res

    return int(res)


def twoSum(self, nums, target):
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


def findKthLargest(self, nums, k):
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

#remove duplicates from sorted array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def removeDuplicates(nums):
    # Time Complexity : O(n)
    # Auxiliary Space : O(1)  --> constant extra space
    # https://www.geeksforgeeks.org/remove-duplicates-sorted-array/
    l = len(nums)
    pos = 0
    for i in range(l - 1):
        if nums[i] != nums[i + 1]:
            nums[pos] = nums[i]
            pos += 1
    nums[pos] = nums[-1]
    pos = pos + 1
    print(nums, pos)
    return (pos)

def removeDuplicates(nums):
    # Time Complexity : O(n)
    # Auxiliary Space : O(1)  --> Using extra space
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    temp = list(range(len(nums))
    j = 0
    for i in range(0, len(nums) - 1):
        if nums[i] != nums[i + 1]:
        temp[j] = nums[i]
        j + -= 1
    temp[j] = nums[len(nums) - 1]
    j = j + 1
    return (j)

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


def is_prime (n):
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

    # print(s)

## Check Prime number
def IsPrime(num):
    if num <2 or num%2==0:
        return False

    if num >2:
        for i in range(3,num,2):
            if num%i==0:
                return False

    return True



### Number  of Primenumbers
def count_primes(num):

    primes =[2]
    x =3

    if num <2:
        return 0

    while x<=num:
        for y in range(3,x,2):
            if x%y==0:
                x+=2
                break
            else:
                primes.append(x)
                x+=2


    print(primes)
    return len(primes)


def consecutive_dups(test_list):
    # https://www.geeksforgeeks.org/python-remove-consecutive-duplicates-from-list/
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
    # https: // www.geeksforgeeks.org / python - remove - none - values -
    # from
    # -list /

    #
    res = []
    for val in test_list:
        if val != None:
            res.append(val)


def remove_non_values_filter(l):
    res = list(filter(None, l))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums) - 1):

        # nicer looking alternative in commented code
        # if nums[i] == 3 and nums[i+1] == 3:

        if nums[i:i + 2] == [3, 3]:
            return True

    return False


def remove_all_digits(s):
    from string import digits

    list = [''.join(x for x in i if x.isalpha()) for i in list]

    return list

    # Driver code

    list = ['4geeks', '3for', '4geeks']
    print(remove(list))


def remove_last_k_elements(s):
    res = test_list[: -K or None]


#### validate IP address
def IPValidate(IP):
    if '.' not in IP or len(IP.split('.'))!=4:
        return 'Invalid'
    IPSplit=IP.split('.')
    if all(c.isdigit() and int(c) in range(0,256) and str(int(c))==c for c in IPSplit):
        return 'Valid'
    else:
        return 'Invalid'



#Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20


def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1


def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total



def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

def sum_of_values(start, end):
    start = 1  # Start of your range
    end = 10  # End of your range
    num_list = range(start, end + 1)  # List of all numbers in given range
    final_sum = sum(num_list)
    print
    "Final Sum =", final_sum

    # Combining all of it together in a single line
    print
    "Final Sum =", sum(range(start, end + 1))


#combiation sum
# https://leetcode.com/problems/combination-sum/discuss/16554/Share-My-Python-Solution-beating-98.17
def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def dfs(remain, combo, index):
        if remain == 0:
            result.append(combo)
            return
        for i in range(index, len(candy)):
            if candy[i] > remain:
                # exceeded the sum with candidate[i]
                break  # the for loop

            dfs(remain - candy[i], combo + [candy[i]], i)

    candy = sorted(candidates)
    result = []
    dfs(target, [], 0)
    return result

#https://leetcode.com/problems/add-two-numbers/discuss?currentPage=1&orderBy=most_votes&query=
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next


# meeting rooms
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False

    return True

def canAttendMeetings(self, intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False

    return True


# Python program for implementation of MergeSort
# divide and conquer
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

try: float(s)
except ValueError: return False
else: return True



def removeSpaces(self, s):
    n = len(s)
    i = 0
    j = n - 1
    while i < n and s[i] == ' ':
        i += 1
    while j > -1 and s[j] == ' ':
        j -= 1
    return s[i:j + 1]


def isNumber(self, s):
    s = self.removeSpaces(s)
    n = len(s)
    if n == 0:
        return False
    i = 0
    dotFlag = False
    EFlag = False
    hasDigit = False
    hasSign = False
    while i < n:
        if s[i].isdigit():
            i += 1
            hasDigit = True
            hasSign = True
        elif not dotFlag and s[i] == '.':
            i += 1
            dotFlag = True
            hasSign = True
        elif hasDigit and not EFlag and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            dotFlag = True
            EFlag = True
            hasDigit = False
            hasSign = False
        elif not hasDigit and not hasSign and (s[i] == '+' or s[i] == '-'):
            i += 1
            hasSign = True
        else:
            return False
    if hasDigit:
        return True
    else:
        return False

