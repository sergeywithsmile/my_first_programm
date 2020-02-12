class Node:
    def __init__(self, key, prev=None, _next=None):
        self.key = key
        self.next = _next
        self.prev = prev

class DoubleList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        new = Node(key, _next=self.head)
        if self.head:
            self.head.prev = new
        self.head = new


    def insert_by_index(self, key, index):
        i = 0
        new = Node(key, _next=None)
        if self.head:
            cur = self.head
        while i != index:
            cur = cur.next
            i = i + 1
        if i == index:
            if cur.next and cur.prev:
                new.next = cur
                new.prev = cur.prev
                cur.prev = new
                cur.prev.prev.next = new
            else:
                if cur.prev:
                    cur.next = new
                    new.prev = cur
                else:
                    cur.prev = new
                    new.next = cur
                    self.head = new


    def search(self, key):
        cur = self.head
        while cur and cur.key != key:
            cur = cur.next
        return cur

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev

    def print(self):
        cur = self.head
        while cur.next:
            print(cur.key)
            cur = cur.next
        print(cur.key)

    def pop_all(self):
        cur = self.head
        while cur.next:
            yield cur.key
            cur = cur.next
        yield cur.key

    def load_from_file(self, path):
        with open(f'{path}', 'r') as file:
            for line in file.readlines():
                self.insert(int(line))

    def save_in_file(self, path):
        with open(f'{path}', 'w',
                  newline='') as file_1:  # создаётся новый файл для записи в указанном пути
            for user in self.pop_all():
                file_1.writelines(str(user) + '\n')
            print(f'Файл в сохранён в {path}.')



