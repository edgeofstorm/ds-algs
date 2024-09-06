'''
The second problem was a little more involved. The wanted to me to build up functions that would work with a "memory stack". The memory stack being an array of 30 items which represented 3 memory stacks where each stack contained 10 items.

I had to build functions such as getSizeOfStack(stackNumber), getStack(stackNumber), popStackItem(stackNumber), setStackItem(stackNumber), etc. Basically implement a variety of functions that worked with the stack.
'''


class MemoryStack:
    def __init__(self, *args) -> None:
        self.stacks = {f'ms{i}':arg for i, arg in enumerate(args, start=1)}
    
    def get_size_of_stack(self, stack_number: int) -> int:
        return len(self.stacks[stack_number])

    def get_stack(self, stack_number: int) -> list:
        return len(self.stacks[stack_number])


ms = MemoryStack([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12, 13])

print(ms.get_size_of_stack("ms2"))