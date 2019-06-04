origin = 0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = step + pos
        pos = new_pos
        return new_pos
    return go

t = factory(origin)
print(t(1))
print(t(3))
print(t(5))