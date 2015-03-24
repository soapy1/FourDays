class Map: 

    def __init__(self):
        self.mappola = None

    def genMap(self):
        root = {'cond': 'You need to wake up to get to work', 'act':[]}
        root_o1 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 7am', 'next':{}}
        root_o2 = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 6am', 'next':{}}
    
        e2 = {'cond':'are you going to walk or run', 'act':[]}
        e2_o1 = {'opt':1, 'health':-2, 'money':0, 'outcome':'Manager is mad. You get beat', 'val':'walk', 'next':{}}
        e2_o2 = {'opt':2, 'health':-1, 'money':0, 'outcome':None, 'val':'run', 'next':{}}
        e2_o3 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'walk', 'next':{}}

        sorry_c = {'cond':'challenge', 'word':'sorry', 'times':10, 'next':{}}
        work_c = {'cond':'challenge', 'word':'work', 'times':10, 'next':{}}
        work2_c = {'cond':'challenge', 'word':'electronics', 'times':10, 'next':{}}
        clothes_c = {'cond':'challenge', 'word':'clothes', 'times':10, 'next':{}}

        root['act'].append(root_o1)
        root['act'].append(root_o2)
        e2_1 = e2.copy()
        e2_2 = e2.copy()
        e2_1['act'].append(e2_o1)
        e2_1['act'].append(e2_o2)
        e2_2['act'] = []
        e2_2['act'].append(e2_o3)
        e2_2['act'].append(e2_o2)
        
        e2_o1['next'] = sorry_c
        
        root_o1['next'] = e2_1
        root_o2['next'] = e2_2

        self.mappola = root
