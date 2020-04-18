class MyQueue:

    """
    Simple queue implementation using two stacks
    """

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []


    def __len__(self):
        return len(self.stack_push) + len(self.stack_pop)

    
    def push(self, element):
        self.stack_push.append(element)

    
    def pop(self):
        if not self.stack_pop:
            self.stack_pop = self.stack_push[::-1]
            self.stack_push = []
        return self.stack_pop.pop()
