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


test1 = solution()
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
