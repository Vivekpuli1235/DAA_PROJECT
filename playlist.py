class Node:
    def __init__(self, song):
        self.song = song
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.current = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def remove_song(self, song):
        temp = self.head
        while temp:
            if temp.song == song:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                if temp == self.current:
                    self.current = self.head
                return True
            temp = temp.next
        return False

    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
        return self.current.song if self.current else "No songs"

    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
        return self.current.song if self.current else "No songs"

    def get_current_song(self):
        return self.current.song if self.current else "No song playing"

    def get_all_songs(self):
        songs = []
        temp = self.head
        while temp:
            songs.append(temp.song)
            temp = temp.next
        return songs
