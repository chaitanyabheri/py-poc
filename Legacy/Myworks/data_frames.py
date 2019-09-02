## Pour water
#class Solution:
def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
    for i in range(V):
        if self.checkFallLeft(heights,K) > -1:
            heights[self.checkFallLeft(heights,K)]+=1
        elif self.checkFallRight(heights,K) > -1:
            heights[self.checkFallRight(heights,K)]+=1
        else: heights[K]+=1
    return heights


def checkFallLeft(self, heights, K):
    minHeight, position = heights[K], -1
    for i in range(K, -1, -1):
        if minHeight>heights[i]:
            minHeight = heights[i]
            position = i
        elif minHeight<heights[i]:
            break
    return position

def checkFallRight(self, heights, K):
    minHeight, position = heights[K], -1
    for i in range(K, len(heights), +1):
        if minHeight>heights[i]:
            minHeight = heights[i]
            position = i
        elif minHeight<heights[i]:
            break
    return position



# https://leetcode.com/problems/alien-dictionary/discuss/356521/Fast-Python-Solution-with-Explanation
#Alien Dictionary

def alienOrder(self, words: List[str]) -> str:
    next_chars = {}

    for i in range(len(words)):
        for j in range(len(words[i])):
            next_chars[words[i][j]] = set()

    for i in range(1, len(words)):

        # in two consecutive words, if their first letter is not equal, then add (first letter of the
        # first word) -> (first letter of the second word) to the graph

        if words[i - 1][0] != words[i][0]:
            next_chars[words[i - 1][0]].add(words[i][0])

        # if the first letters are equal, we should look for the first non-equal characters to be added to             # the graph
        else:
            char_counter = 0
            while char_counter < len(words[i - 1]) and char_counter < len(words[i]) and words[i - 1][char_counter] == \
                    words[i][char_counter]:
                char_counter += 1

            if char_counter >= len(words[i - 1]) or char_counter >= len(words[i]):
                char_counter -= 1
            if words[i][char_counter] != words[i - 1][char_counter]:  # for words like "wrt" and"wrtb"
                next_chars[words[i - 1][char_counter]].add(words[i][char_counter])

    # Now, let's apply topological sort
    st = []
    in_degree = {}

    # recording in_degrees for each character
    for c in next_chars:
        in_degree[c] = 0
    for c in next_chars:
        for val in next_chars[c]:
            in_degree[val] += 1
    '''
    for topological sort: find a letter in graph with 0 in_degree (no incoming edge), add it to the final string, remove all of its outgoing edges (meaning that if these edges are going to the other nodes, the in_degree of those nodes needs to be reduced), and delete the node from the graph. 
    Continue doing this until all letters are added to the graph
    if this looks vague watch the topological sort video from here: https://www.youtube.com/watch?v=71eHuQvSwc0&feature=youtu.be
    '''
    while next_chars:
        target = self.findIndegreeZero(in_degree)
        if not target:
            return ""
        st.append(target)
        for m in next_chars[target]:
            in_degree[m] -= 1
        del next_chars[target]
        del in_degree[target]

    return ''.join(st)


# returns a character that has 0 as in_degree and if it can't find such a letter, it will return None
def findIndegreeZero(self, in_degree):
    for k in in_degree:
        if in_degree[k] == 0:
            return k
    return None


#Text justification

#https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.


#IP to CIDR
#https://leetcode.com/problems/ip-to-cidr/
def ip2number(self, ip):
    numbers = list(map(int, ip.split(".")))
    n = (numbers[0] << 24) + (numbers[1] << 16) + (numbers[2] << 8) + numbers[3]
    return n

def number2ip(self, n):
    return ".".join([str(n >> 24 & 255), str(n >> 16 & 255), str(n >> 8 & 255), str(n & 255)])

def ilowbit(self, x):
    for i in range(32):
        if (x & (1 << i)):
            return i

def lowbit(self, x):
    return 1 << self.ilowbit(x)

def ipToCIDR(self, ip, n):
    number = self.ip2number(ip)
    result = []
    while n > 0:
        lb = self.lowbit(number)
        while lb > n:
            lb = lb // 2

        n = n - lb

        result.append(self.number2ip(number) + "/" + str(32 - self.ilowbit(lb)))
        number = number + lb;
    return result

#787. Cheapest Flights Within K Stops
#

def findCheapestPrice(self, n, flights, src, dst, K):
    graph = collections.defaultdict(list)
    pq = []

    for u, v, w in flights: graph[u].append((w, v))

    heapq.heappush(pq, (0, K+1, src))
    while pq:
        price, stops, city = heapq.heappop(pq)

        if city is dst: return price
        if stops>0:
            for price_to_nei, nei in graph[city]:
                heapq.heappush(pq, (price+price_to_nei, stops-1, nei))
    return -1

#291 word pattern
#Use dictionary to store patterns, and backtrack when mismatch happens.
#https://leetcode.com/problems/word-pattern-ii/
def wordPatternMatch(self, pattern, str):
    return self.dfs(pattern, str, {})

def dfs(self, pattern, str, dict):
    if len(pattern) == 0 and len(str) > 0:
        return False
    if len(pattern) == len(str) == 0:
        return True
    for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
        if pattern[0] not in dict and str[:end] not in dict.values():
            dict[pattern[0]] = str[:end]
            if self.dfs(pattern[1:], str[end:], dict):
                return True
            del dict[pattern[0]]
        elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
            if self.dfs(pattern[1:], str[end:], dict):
                return True
    return False

#324. Wiggle Sort II
#https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
def wiggleSort(self, nums):
    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


#212 workd search
#https://leetcode.com/problems/word-search-ii/

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp


# 1st missing postive
#https://leetcode.com/problems/first-missing-positive/submissions/

 def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n) time

        for i in xrange(len(nums)):
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

    # O(nlgn) time
    def firstMissingPositive(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res