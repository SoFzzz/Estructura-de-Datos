class Manager:
    ## """Manages Visual Novel quick saves""" ##
    def __init__(self, max_saves=5):
        self.save_stack = []
        self.max_saves = max_saves

    def is_empty(self):
        return len(self.save_stack) == 0

    def push(self, state):
        if len(self.save_stack) >= self.max_saves:
            self.save_stack.pop(0)
        self.save_stack.append(state)
        print(f"--> Quick Save Created: {state}")

    def pop(self):
        if self.is_empty():
            print("--> Error: No quick saves available to load")
            return None
        loaded_state = self.save_stack.pop()
        print(f"--> Quick Load Successful: Restoring to {loaded_state}")
        return loaded_state

    def top(self):
        if self.is_empty():
            return None
        return self.save_stack[-1]

    