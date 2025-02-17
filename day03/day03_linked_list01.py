# day03_linked_list01.py
# 단순 연결리스트 응용예제01-사용자가 입력한 정보 관리하기

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    curr = start
    if current == None:
        return
    print(curr.data, end='')
    while curr.link != None:
        curr = curr.link
        print(curr.data, end='')
    print()

def makeSimpleLinkedList(nameEmail):
    global memory, head, curr, prev

    node = Node()
    node.data = nameEmail
    memory.append(node)
    if head == None:    # 첫번째 노드
        head = node
        return
    
    if head.data[1] > nameEmail[1]:
        node.link = head
        head = node
        return
    
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.dat[1] > nameEmail[1]:
            prev.link = node
            node.link = curr
            return
        
    curr.link = node

## 전역 변수 선언 부분 ##
memory = []
head, curr, prev = None, None, None

## 메인 코드 부분
if __name__ == '__main__':

    while True:
        name = input('이름--> ')
        if name == '' or name == None:
            break
        email = input('이메일--> ')
        makeSimpleLinkedList([name, email])
        printNodes(head)