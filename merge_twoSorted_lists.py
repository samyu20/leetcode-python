"""Problem: #21. Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list.
The merged list should be created by splicing together the nodes
of the first two lists.
Return the head of the merged linked list.

Example:
Input : list1 = [1,2,4], list2 = [1,3,4] ,Output: [1,1,2,3,4,4]"""

# Algorithm:
# Create a dummy node to store the merged list
# Use a current pointer to build the merged list
# Compare nodes from both linked lists
# Attach the smaller node to current.next
# Move the corresponding list pointer forward
# Move current forward
# Attach remaining nodes after loop ends
# Return dummy.next as the merged list head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_list(list1,list2):

    dummy = ListNode()                      #temporary node
    current = dummy                         #storing merged list

    #list1 = [1,2,4], list2 = [1,3,4]

    while list1 and list2:                  # Loop will run as long as the lists have nodes
        if list1.val < list2.val:           # 1< 1=F , 1<3=T , 2<3=T   ,4<3=F    , 4<4=F
            current.next = list1            # c.n= 1, (1 ,2) , (1,1,2)
            list1 = list1.next              # list1 =   2     , 4
        else:
            current.next = list2            #c.n= 1   ,                (1,1,2,3) ,(1,1,2,3,4)
            list2 = list2.next              #list2 =3                  , 4       , None -> loop will exist

        current = current.next              #c=1,2,3,4

   # adding remaining nodes
    current.next = list1 or list2           #list1-> still has 4 , it will added into current , c.n = 1,1,2,3,4,4

    return dummy.next                       #return the values to dummy, it is the real head

# Input Section
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = merge_two_list(list1,list2)

# Printing the merged linked list
while result:
    if result.next:
        print(result.val,end=",")
    else:
        print(result.val)
    result=result.next

# Time Complexity  : O(n + m) — traverses both linked lists once
# Space Complexity : O(1) — no extra linked list created