class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

# דוגמה לשימוש במחסנית
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # יודפס: 3
print(stack.peek())  # יודפס: 2
print(stack.size())  # יודפס: 2
"""
הסבר:
- הקוד מגדיר מחלקה בשם Stack שמייצגת מחסנית.
- במחלקה יש פעולות כמו push להוספת איבר למחסנית, pop להוצאת האיבר העליון, peek לצפייה באיבר העליון ו-size לקביעת גודל המחסנית.
- בדוגמה נוצרת מחסנית, מתווספים אליה ערכים ומודפסים תוצאות של הפעולות על המחסנית.
"""