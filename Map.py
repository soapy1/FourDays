from Event import Event
from Challenge import Challenge

class Map: 

    def __init__(self):
        self.mappola = None

    def ghettoGen(self):
        root = {'cond': 'You need to wake up to get to work', 'act':[]}
        root_o1 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 7am', 'next':{}}
        root_o2 = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 6am', 'next':{}}
    
        e2 = {'cond':'are you going to walk or run', 'act':[]}
        e2_o1 = {'opt':1, 'health':-2, 'money':0, 'outcome':'Manager is mad. You get beat', 'val':'walk', 'next':{}}
        e2_o2 = {'opt':2, 'health':-1, 'money':0, 'outcome':None, 'val':'run', 'next':{}}
        e2_o3 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'walk', 'next':{}}

        challenge = {'cond':'challenge', 'word':'sorry', 'times':10, 'next':{}}

        root['act'].append(root_o1)
        root['act'].append(root_o2)
        e2_1 = e2.copy()
        e2_2 = e2.copy()
        e2_1['act'].append(e2_o1)
        e2_1['act'].append(e2_o2)
        e2_2['act'] = []
        e2_2['act'].append(e2_o3)
        e2_2['act'].append(e2_o2)

        
        root_o1['next'] = e2_1
        root_o2['next'] = e2_2

        self.mappola = root

    def generateMap(self):
        root = Event( 
            None, None, "Do you wake up at [1] 7am or [2] 6am", [], None
        )
    
        wakeLate = Event(
            "wake up at 7am", "you're late", None, [], None
        )

        wakeEarly = Event(
            "wake up at 6am", "you arrive on time", None, [], None
        )

        root.next_event.append(wakeLate)
        root.next_event.append(wakeEarly)

        self.mappola = root
