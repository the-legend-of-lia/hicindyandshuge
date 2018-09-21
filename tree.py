def tree(label, branches=[]):
    #for branch in branches:
    #    assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def tree_max(t):
    if is_leaf(t):
        return label(t)
    else:
        m = label(t)
        for b in branches(t):
            m = max(tree_max(b), m)
        return m

def height(t):
    if is_leaf(t):
        return 0
    else:
        h = 0
        for b in branches(t):
            h = max(height(b) + 1, h)
        return h

def square_tree(t):
    if is_leaf(t):
        return tree(label(t)**2, [])
    else:
        bs = []
        for b in branches(t):
            bs.append(square_tree(b))
        return tree(label(t)**2, bs)

def print_tree(t,depth = 0):
    if is_leaf(t):
        print('\t' * depth + str(label(t)))
    else:
        print('\t' * depth + str(label(t)))
        for b in branches(t):
            print_tree(b,depth + 1)

def find_path(tree, x):
    if is_leaf(tree):
        return [x] if (x == label(tree)) else None
    else:
        for b in branches(tree):
            p = find_path(b,x)
            if p:
                return [label(tree)] + p
        return None

t = tree(1,
        [tree(3,
            [tree(4),
            tree(5),
            tree(6)]),
        tree(2)])

print(tree_max(t))
print(height(t))

t2 = square_tree(t)
print_tree(t)
print('\n')
print_tree(t2)
print('\n')
print(find_path(t, 6))
