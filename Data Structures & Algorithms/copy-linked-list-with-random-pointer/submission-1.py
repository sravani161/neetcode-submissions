class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy = {}
        cur = head
        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            copy[cur].next = copy.get(cur.next)
            copy[cur].random = copy.get(cur.random)
            cur = cur.next
        return copy[head]