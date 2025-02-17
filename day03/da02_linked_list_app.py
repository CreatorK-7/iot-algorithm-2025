# da02_linked_list_app.py
# 단순 연결 리스트 응용

## 클래스와 함수 선언 부분##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    curr = start
    if curr == None: return
    print(curr.dat, end = '')
    while curr.link != None:
        curr = curr.link
        print(curr.data, end = '')
    print()

def makeSimpleLinkedList(namePhone):
    global memory, head, curr, prev
    printNodes(head)

    node = Node()
    node.dat = namePhone
    memory.append(node)
    if head == None:    # 첫 번째 노드일 때
        head = node
        return
    
    if head.data[0] > namePhone[0]:  # 첫 번째 노드보다 작을 때
        node.link = head
        head = node
        return
    
    # 중간 노드로 삽입하는 경우
    curr = head
    while curr.link != None:
        prev = curr
        curr = curr.link
        if curr.data[0] > namePhone[0]:
            prev.link = node
            node.link = curr
            return
        
    # 삽입하는 노드가 가장 큰 경우
    curr.link = node

## 전역 변수 선언 부분 ##
memory = []
head, curr, prev = None, None, None
dataArray = [['지민', '010-1111-1111'], ['정국', '010-2222-2222'], ['뷔', '010-3333-3333'],
             ['슈가', '010-4444-4444'], ['진', '010-5555-5555']]

## 메인 코드 부분 ##
if __name__ == '__main__':

    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)