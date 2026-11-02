# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:   # You are not allowed to modify this class
    def __init__(self, value=None):  
        self.next = None
        self.value = value

    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__

class Malloc_Library:

    """
    ** This is NOT a comprehensive test sample, test beyond this doctest
        >>> lst = Malloc_Library()
        >>> lst
        <BLANKLINE>
        >>> lst.malloc(5)
        >>> lst
        None -> None -> None -> None -> None
        >>> lst[0] = 23
        >>> lst
        23 -> None -> None -> None -> None
        >>> lst[0]
        23
        >>> lst[1]
        >>> lst.realloc(1)
        >>> lst
        23
        >>> lst.calloc(5)
        >>> lst
        0 -> 0 -> 0 -> 0 -> 0
        >>> lst.calloc(10)
        >>> lst[3] = 5
        >>> lst[8] = 23
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0 -> 0 -> 0 -> 0 -> 23 -> 0
        >>> lst.realloc(5)
        >>> lst
        0 -> 0 -> 0 -> 5 -> 0
        >>> other_lst = Malloc_Library()
        >>> other_lst.realloc(9)
        >>> other_lst[0] = 12
        >>> other_lst[5] = 56
        >>> other_lst[8] = 6925
        >>> other_lst[10] = 78
        Traceback (most recent call last):
            ...
        IndexError
        >>> other_lst.memcpy(2, lst, 0, 5)
        >>> lst
        None -> None -> None -> 56 -> None
        >>> other_lst
        12 -> None -> None -> None -> None -> 56 -> None -> None -> 6925
        >>> temp = lst.head.next.next
        >>> lst.free()
        >>> temp.next is None
        True
    """

    def __init__(self): # You are not allowed to modify the constructor
        self.head = None

    def __repr__(self):  # You are not allowed to modify this method
        current = self.head
        out = []
        while current != None:
            out.append(str(current.value))
            current = current.next
        return " -> ".join(out)

    __str__ = __repr__

    def __len__(self):
        # --- YOUR CODE STARTS HERE
        cur, n=self.head, 0
        while cur:
            n+=1
            cur=cur.next
        return n

    def __setitem__(self, pos, value):
        # --- YOUR CODE STARTS HERE
        if pos<0: raise IndexError
        cur=self.head
        while cur and pos>0:
            cur=cur.next
            pos-=1
        if cur is None: raise IndexError
        cur.value=value

    def __getitem__(self, pos):
        # --- YOUR CODE STARTS HERE
        if self.head is None: return None
        if pos<0: raise IndexError
        cur=self.head
        while cur and pos>0:
            cur=cur.next
            pos-=1
        if cur is None: raise IndexError
        return cur.value

    def malloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.head = None
        current = None
        for _ in range(size):
            new_node = Node()
            if self.head is None:
                self.head = new_node
            else:
                current.next = new_node
            current = new_node


    def calloc(self, size):
        # --- YOUR CODE STARTS HERE
        self.malloc(size)
        cur=self.head
        while cur:
            cur.value=0
            cur=cur.next

    def free(self):
        # --- YOUR CODE STARTS HERE
        while self.head:
            cur=self.head
            self.head=cur.next
            cur.next=None

    def realloc(self, size):
        # --- YOUR CODE STARTS HERE
        if size==0: return self.free()
        if self.head is None: return self.malloc(size)
        cur=self.head
        for i in range(size-1):
            if cur.next is None: cur.next=Node()
            cur=cur.next
        extra=cur.next
        cur.next=None
        while extra:
            cur=extra
            extra=cur.next
            cur.next=None

    def memcpy(self, ptr1_start_idx, pointer_2, ptr2_start_idx, size):
        # --- YOUR CODE STARTS HERE
        if ptr1_start_idx<0 or ptr2_start_idx<0: return
        src, dst=self.head, pointer_2.head
        while src and ptr1_start_idx>0:
            src=src.next
            ptr1_start_idx-=1
        while dst and ptr2_start_idx>0:
            dst=dst.next
            ptr2_start_idx-=1
        while src and dst and size>0:
            dst.value=src.value
            src, dst=src.next, dst.next
            size-=1

def run_tests():
    import doctest
    result=doctest.testmod(verbose=True)
    assert result.failed==0

    a, b=Malloc_Library(), Malloc_Library()
    assert len(a)==0 and str(a)=='' and a[0] is None
    assert a.free() is None and a.head is None
    a.memcpy(0,b,0,5)
    assert a.head is None and b.head is None
    a.realloc(0)
    assert a.head is None

    a.malloc(1)
    assert len(a)==1 and a[0] is None and a.head.next is None
    a[0]='hi'
    assert a[0]=='hi'
    for pos in (-1,1,5):
        try: a[pos]
        except IndexError: pass
        else: raise AssertionError('Invalid read index accepted')
        try: a[pos]=99
        except IndexError: pass
        else: raise AssertionError('Invalid write index accepted')
    assert a[0]=='hi'

    a.calloc(4)
    assert len(a)==4 and str(a)=='0 -> 0 -> 0 -> 0'
    a[0], a[1], a[2], a[3]=10, 20, 30, 40
    first, second, third=a.head, a.head.next, a.head.next.next
    fourth=third.next
    a.realloc(4)
    assert a.head is first and third.next is fourth
    assert str(a)=='10 -> 20 -> 30 -> 40'
    a.realloc(6)
    assert a.head is first and third.next is fourth
    assert str(a)=='10 -> 20 -> 30 -> 40 -> None -> None'
    fifth, sixth=fourth.next, fourth.next.next
    a.realloc(2)
    assert a.head is first and first.next is second and second.next is None
    assert len(a)==2 and str(a)=='10 -> 20'
    assert third.next is fourth.next is fifth.next is sixth.next is None
    a.realloc(0)
    assert a.head is None and first.next is second.next is None
    a.realloc(3)
    assert len(a)==3 and str(a)=='None -> None -> None'

    a[0], a[1], a[2]=7, 8, 9
    b.memcpy(0,a,0,3)
    a.memcpy(0,b,0,3)
    assert str(a)=='7 -> 8 -> 9' and b.head is None
    b.calloc(5)
    first, second=b.head, b.head.next
    a.memcpy(1,b,2,10)
    assert str(b)=='0 -> 0 -> 8 -> 9 -> 0'
    assert b.head is first and first.next is second and len(b)==5
    assert str(a)=='7 -> 8 -> 9'
    a.memcpy(0,b,4,10)
    assert str(b)=='0 -> 0 -> 8 -> 9 -> 7'
    for src, dst in ((3,0),(0,5),(20,0),(0,20)):
        a.memcpy(src,b,dst,3)
        assert str(a)=='7 -> 8 -> 9' and str(b)=='0 -> 0 -> 8 -> 9 -> 7'
    a.memcpy(0,b,0,0)
    assert str(b)=='0 -> 0 -> 8 -> 9 -> 7'
    a.memcpy(0,b,0,1)
    assert str(b)=='7 -> 0 -> 8 -> 9 -> 7'
    b[0]=100
    assert a[0]==7 and a.head is not b.head

    first, second=b.head, b.head.next
    third, fourth=second.next, second.next.next
    fifth=fourth.next
    b.free()
    assert len(b)==0 and b.head is None
    assert first.next is second.next is third.next is fourth.next is fifth.next is None
    b.free()
    b.realloc(1)
    b[0]=a[2]
    assert str(b)=='9' and len(b)==1
    b.malloc(2)
    assert str(b)=='None -> None'
    b.calloc(1)
    assert str(b)=='0' and b.head.next is None
    print('Additional boundary and mixed-operation tests passed.')

if __name__ == "__main__":
     run_tests()
