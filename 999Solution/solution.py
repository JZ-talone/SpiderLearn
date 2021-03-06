import collections
from collections import deque
from functools import cmp_to_key
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    list = []
    index = 0

    def __init__(self, root: TreeNode):
        self.process(root)
        self.list.insert(0, self.list[0] - 1)

    def next(self) -> int:
        self.index += 1
        return self.list[self.index]

    def hasNext(self) -> bool:
        nextindex = self.index + 1
        return nextindex < len(self.list)

    def process(self, root):
        if root is None:
            return
        self.process(root.left)
        self.list.append(root.val)
        self.process(root.right)


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


class solution:
    # 不能用乘除 if else for 等语句求等差和
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

    # 判断赢家
    def PredictTheWinner(self, nums: List[int]) -> bool:
        f1 = self.xian(nums, 0, len(nums) - 1)
        f2 = self.hou(nums, 0, len(nums) - 1)
        return f1 >= f2

    def xian(self, nums, start, end):
        if start == end:
            return nums[start]
        f1 = nums[start] + self.hou(nums, start + 1, end)
        f2 = nums[end] + self.hou(nums, start, end - 1)
        if f1 >= f2:
            return f1
        else:
            return f2

    def hou(self, nums, start, end):
        if start == end:
            return 0
        f1 = self.xian(nums, start + 1, end)
        f2 = self.xian(nums, start, end - 1)
        if f1 >= f2:
            return f2
        else:
            return f1

    # https://leetcode.cn/problems/sum-lists-lcci/

    # % 取余 / 除 // 除取整
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNumbersfun(l1, l2, None, 0)

    def addTwoNumbersfun(self, l1, l2, ans, jw):
        if l1 is None and l2 is None and jw == 0:
            return None

        h = (0 if l1 is None else l1.val) + jw + (0 if l2 is None else l2.val)
        ans = ListNode(h % 10)
        ans.next = self.addTwoNumbersfun(None if l1 is None else l1.next, None if l2 is None else l2.next, None,
                                         h // 10)

        return ans

    # https://leetcode.cn/problems/LGjMqU/
    # 所有单链表都可以考虑试试快慢指针
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找中点
        curm = head
        curk = head

        while curk.next is not None and curk.next.next is not None:
            curm = curm.next
            curk = curk.next.next
        if curk.next is not None:
            curk = curk.next
            tmp = curm.next
            curm.next = None
            curm = tmp

        # 单链表反转
        self.revertNode(curm)
        curm.next = None

        # 链表合并
        curt = head
        curw = curk
        while curt and curw:
            tmp = curt.next
            tmp1 = curw.next
            curt.next = curw
            curt = tmp

            curw.next = curt
            curw = tmp1

    def revertNode(self, head):
        if head is not None:
            self.revertNode(head.next)
            if head.next is not None:
                head.next.next = head

    # https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        ans = []
        # python 的比较器写法
        # points.sort(key=lambda l1: l1[0])
        points.sort(key=cmp_to_key(lambda l1, l2: l1[0] - l2[0] if l1[0] != l2[0] else l1[1] - l2[1]))
        for point in points:
            if len(ans) == 0:
                ans.append(point)
            else:
                last = ans[-1]
                if last[1] >= point[0]:
                    ans[-1] = [point[0], last[1] if last[1] <= point[1] else point[1]]
                else:
                    ans.append(point)
        return len(ans)

    # https://leetcode.cn/problems/rabbits-in-forest/
    def numRabbits(self, answers: List[int]) -> int:
        map = {}
        answers.sort()
        for x in answers:
            if map.keys().__contains__(x):
                v = map[x]
                map[x] = v + 1
            else:
                map[x] = 1

        count = 0
        for k in map.keys():
            v = map[k]
            count += ((k + 1) * (v // (k + 1) if v % (k + 1) == 0 else v // (k + 1) + 1))
        return count

    # https: // leetcode.cn / problems / subarray - product - less - than - k /
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda l1: l1)
        cjnums = []
        curcj = 1
        for num in nums:
            curcj *= num
            cjnums.append(curcj)

        return self.processNumSubarrayProductLessThanK(cjnums, k)

    # 连续子数组！所以不是递归套路
    # 用前缀和
    # [10, 5, 2, 6]
    # 10 50 100 600
    # 10 50 5 10 2 60 12 6
    # 比较慢 但能过 用滑动窗口很快！
    def processNumSubarrayProductLessThanK(self, cjnums, k):
        total = 0
        for i in range(0, cjnums.__len__()):
            if cjnums[i] >= k:
                if i - 1 >= 0:
                    for j in range(i - 1, -1, -1):  # range 倒序
                        # print(cjnums[j])
                        if cjnums[i] // cjnums[j] < k:
                            total += 1
                        else:
                            break
            else:
                total += (i + 1)

        return total

    # https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ljp = self.findlj(root, p)
        ljq = self.findlj(root, q)
        i = 0
        while True:
            if i == len(ljp) or i == len(ljq) or ljp[i] != ljq[i]:
                return ljp[i - 1]
            else:
                i += 1

    def findlj(self, root, fn):
        if root is None:
            return None
        if root.val == fn.val:
            return [fn]
        else:
            lj = self.findlj(root.left, fn)
            if lj:
                lj.insert(0, root)
                return lj
            else:
                lj = self.findlj(root.right, fn)
                if lj:
                    lj.insert(0, root)
                    return lj

    # https: // leetcode.cn / problems / binary - tree - maximum - path - sum /
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.processMaxPathSum(root)
        return self.cur

    cur = -10000

    def processMaxPathSum(self, root):

        if root is None:
            return None
        else:
            x = self.processMaxPathSum(root.left)
            y = self.processMaxPathSum(root.right)
            # 经过root的最大长度
            a = root.val + (0 if x is None else x) + (0 if y is None else y)
            # root作为头的最大长度
            b = max(root.val, root.val + (0 if x is None else x), root.val + (0 if y is None else y))
            self.cur = max(self.cur, a, b)
            return b

    pathWayNum = 0

    # https://leetcode.cn/problems/6eUYwP/submissions/ 可以用前缀和 省去很多重复计算
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.processPathSum(root, targetSum, True)
        return self.pathWayNum

    def processPathSum(self, root, targetSum, canNotUseHead):
        if root is None:
            return
        if canNotUseHead:
            self.processPathSum(root.left, targetSum, True)
            self.processPathSum(root.right, targetSum, True)

        if targetSum - root.val == 0:
            self.pathWayNum += 1
        self.processPathSum(root.left, targetSum - root.val, False)
        self.processPathSum(root.right, targetSum - root.val, False)

    # https://leetcode.cn/problems/minimum-index-sum-of-two-lists/
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minIndex = 2001
        minL1Index = []
        map = {}
        for i in range(0, len(list1)):
            map[list1[i]] = i
        for k in range(0, len(list2)):
            if map.get(list2[k]) is not None:
                if k + map.get(list2[k]) < minIndex:
                    minIndex = k + map.get(list2[k])
                    minL1Index = [map.get(list2[k])]
                elif k + map.get(list2[k]) == minIndex:
                    minL1Index.append(map.get(list2[k]))
        ans = []
        for x in minL1Index:
            ans.append(list1[x])
        return ans

    # https://leetcode.cn/problems/implement-strstr/ 经典kmp
    def strStr(self, haystack: str, needle: str) -> int:
        # needle
        if needle is None or len(needle) == 0:
            return -1
        if len(needle) > len(haystack):
            return -1

        i = 0
        j = 0
        str1 = haystack
        str2 = needle
        next = self.kmpNext(str2)
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = next[j]
        if j == len(str2):
            return i - j
        else:
            return -1

    def kmpNext(self, str2):
        if len(str2) == 1:
            return [-1]
        else:
            next = [-1, 0]
            i = 2
            cn = 0
            while i < len(str2):
                if str2[i-1] == str2[cn]:
                    cn += 1
                    next.append(cn)
                    i += 1
                elif cn > 0:
                    cn = next[cn]
                else:
                    next.append(0)
                    i += 1
            return next

    def removeOccurrences(self, s: str, part: str) -> str:
        index = self.strStr(s,part)
        if index<0:
            return s
        else:
            s =s[0:index]+s[index + len(part):len(s)]
            return self.removeOccurrences(s,part)

    # https: // leetcode.cn / problems / minimum - genetic - mutation /
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = deque()
        q.append((start,0))
        while len(q) != 0:
            gene,step = q.popleft()
            if gene==end:
                return step
            else:
                for x in range(len(gene)):
                    for rp in 'ACGT':
                        newgene = gene[:x]+rp+gene[x+1:]
                        if newgene!=gene and newgene in bank:
                            step+=1
                            q.append((newgene,step))
                            bank.remove(newgene)
        return -1

    # https://leetcode.cn/problems/trapping-rain-water/
    def trap(self, height: List[int]) -> int:
        stack = list()
        total = 0
        i=0
        while i in range(len(height)):
            if len(stack)==0 or stack[-1][0]>height[i]:
                stack.append([height[i],i])
                i+=1
            elif stack[-1][0]==height[i]:
                stack[-1][1] = i
                i+=1
            else:
                x = stack.pop()
                if len(stack)>0:
                    total += (min(stack[-1][0],height[i])-x[0])*(i-stack[-1][1]-1)
                if len(stack)==0 or stack[-1][0]>height[i]:
                    stack.append([height[i], i])
        return total

    #https://leetcode.cn/problems/minimum-absolute-difference/
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minposition = []
        minscore = None
        arr.sort()
        for i in range(0, len(arr)-1):
            if minscore is None :
                minscore = arr[i+1]-arr[i]
                minposition.append(i)
            else:
                if arr[i+1]-arr[i]==minscore:
                    minposition.append(i)
                elif arr[i+1]-arr[i]<minscore:
                    minscore = arr[i + 1] - arr[i]
                    minposition = []
                    minposition.append(i)
        ans = []
        for i in minposition:
            ans.append([arr[i],arr[i+1]])
        return ans

    # https://leetcode.cn/problems/number-of-good-leaf-nodes-pairs/ 递归返回该节点的对数及小于distanse的各节点个数
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = self.processCountPairs(root,distance)
        return ans[0]

    def processCountPairs(self, root, distance):
        if root is None:
            return [None,None]

        leftL = self.processCountPairs(root.left,distance)
        leftR = self.processCountPairs(root.right,distance)
        if leftL[0] is None and leftR[0] is None:
            return [0,{1:1}]
        if leftL[0] is None and leftR[0] is not None:
            map = {}
            for k in leftR[1].keys():
                if k+1<distance:
                    map[k+1] = leftR[1][k]
            return [leftR[0],map]
        if leftL[0] is not None and leftR[0] is  None:
            map = {}
            for k in leftL[1].keys():
                if k+1<distance:
                    map[k+1] = leftL[1][k]
            return [leftL[0],map]
        if leftL[0] is not None and leftR[0] is not None:
            map = {}
            for k in leftL[1].keys():
                if k + 1 < distance:
                    map[k + 1] = leftL[1][k]
            for k in leftR[1].keys():
                if k + 1 < distance:
                    map[k + 1] = leftR[1][k] + (map[k+1] if map.__contains__(k+1)  else 0)
            c = leftR[0]+leftL[0]
            for k in leftL[1].keys():
                for k1 in leftR[1].keys():
                    if k+k1<=distance:
                        c += (leftL[1][k]*leftR[1][k1])
            return [c,map]

    # https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 会超时 用dp即可
        # fz = []
        # maxCount = 0
        #
        # for i in arr:
        #     fz.append(0)
        # for index in range(0, len(arr)):
        #     if len(arr)-index < maxCount:
        #         break
        #     if fz[index] ==0:
        #         curCount = 0
        #         before = None
        #         use = []
        #         for index1 in range(index,len(arr)):
        #             if index1==index:
        #                 curCount =curCount+1
        #                 before = arr[index1]
        #                 use.append(index1)
        #             else:
        #                 if arr[index1]-difference==before:
        #                     if fz[index1] ==0:
        #                         curCount =curCount+1
        #                         before = arr[index1]
        #                         use.append(index1)
        #                     else:
        #                         curCount = curCount+fz[index1]
        #                         break
        #         for index in range(0, len(use)):
        #             fz[use[index]] = curCount-index
        #
        #         maxCount = max(maxCount,curCount)
        # return maxCount
        dp = collections.defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())

    # https://leetcode.cn/problems/ZVAVXX/
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        l = 0
        r = 0
        ret = 0
        t = 1
        while r < len(nums):
            t = t * nums[r]
            while t >= k and l <= r:
                t //= nums[l]
                l += 1
            if l <= r:
                ret = ret + r - l + 1
            r += 1
        return ret

    # https://leetcode.cn/problems/delete-node-in-a-linked-list/
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # https: // leetcode.cn / problems / minimum - distance - to - the - target - element /
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return self.processgetMinDistance(nums,target,start,0)

    def processgetMinDistance(self, nums, target, start, d):
        l = start - d if start-d>=0 else 0
        r = start +d if start+d<len(nums) else len(nums)-1
        if nums[l]==target:
            return start-l
        if nums[r]==target:
            return r-start
        return self.processgetMinDistance(nums,target,start,d+1)



test1 = solution()
test1.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
test1.longestSubsequence([1,5,7,8,5,3,4,2,1],-2)
c1 = TreeNode(1)
c2 = TreeNode(2)
c3 = TreeNode(4)
c4 = TreeNode(3)
c1.left = c2
c2.right = c3
c1.right = c4
test1.countPairs(c1,3)

print(test1.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(test1.minMutation(start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))
print(test1.removeOccurrences(s = 'daabcbaabcbc', part = 'abc'))
print(test1.kmpNext('abcabcaabcabx'))
print(test1.strStr('abcabcaabcabx','bcabcaa'))
test1.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
t1 = TreeNode(-10)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
print(test1.maxPathSum(t1))
print(test1.findlj(t1, t1))
print(test1.findlj(t1, t2))
print(test1.findlj(t1, t3))
print(test1.findlj(t1, t4))
print(test1.lowestCommonAncestor(t1, t2, t3).val)

t5 = TreeNode(1)
obj = BSTIterator(t5)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())

print(test1.numSubarrayProductLessThanK([10, 5, 2, 6, 1000], 100))

print(test1.numRabbits([1, 1, 2]))
print(test1.findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
print(test1.sumNums(3))
print(test1.sumNums(9))

l1 = ListNode(3)
l2 = ListNode(4)
l2.next = l1
l3 = ListNode(2)
l3.next = l2

l4 = ListNode(4)
l5 = ListNode(6)
l5.next = l4
l6 = ListNode(5)
l6.next = l5
print(test1.addTwoNumbers(l3, l6))

l3 = ListNode(5)

l4 = ListNode(5)
print(test1.addTwoNumbers(l3, l4))

t1 = ListNode(1)
t2 = ListNode(2)
t1.next = t2
t3 = ListNode(3)
t2.next = t3
t4 = ListNode(4)
t3.next = t4
# t5 = ListNode(5)
# t4.next = t5
print(test1.reorderList(t1))
