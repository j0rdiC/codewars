# 6 kyu


def is_valid_walk(walk):
    
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
    
    plan = {
        'n': 0,
        's': 0,
        'e': 0,
        'w': 0
    }

    for d in walk:
        if d in plan:
            plan[d] += 1
    
    return True if len(walk) == 10 and plan['n'] == plan['s'] and plan['e'] == plan['w'] else False



is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])#, 'should return True'
is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])#, 'should return False'
is_valid_walk(['w'])#, 'should return False'
is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])#, 'should return False'