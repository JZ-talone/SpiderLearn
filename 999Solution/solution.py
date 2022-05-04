from functools import cmp_to_key
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        points.sort(key=cmp_to_key(lambda l1,l2 :l1[0]-l2[0] if l1[0]!=l2[0] else l1[1]-l2[1]))
        for point in points:
            if len(ans)==0:
                ans.append(point)
            else:
                last = ans[-1]
                if last[1]>=point[0]:
                    ans[-1] = [point[0],last[1] if last[1]<=point[1] else point[1]]
                else:
                    ans.append(point)
        return len(ans)

    #https://leetcode.cn/problems/rabbits-in-forest/
    def numRabbits(self, answers: List[int]) -> int:
        map = {}
        answers.sort()
        for x in answers:
            if map.keys().__contains__(x) :
                v = map[x]
                map[x] = v + 1
            else:
                map[x] = 1

        count=0
        for k in map.keys():
            v = map[k]
            count+=((k+1)*(v//(k+1) if v%(k+1)==0 else v//(k+1)+1))
        return count

test1 = solution()
print(test1.numRabbits([1,1,2]))
print(test1.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
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
