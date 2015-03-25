from random import randint

class Map: 

    def __init__(self):
        self.mappola = None

    def _getLeaf(self, m):
        cur = m
        while (cur['next'] != {}):
            cur = cur['next']
        return cur

    def _getRandomWorkBreak(self):
        work_type = [
            {'cond':'challenge', 'word':'work', 'times':10, 'next':{}},
            {'cond':'challenge', 'word':'electronics', 'times':10, 'next':{}},
            {'cond':'challenge', 'word':'clothes', 'times':10, 'next':{}},
            {'cond':'challenge', 'word':'shoes', 'times':10, 'next':{}},
        ]

        rand = randint(0, 3)
        w = work_type[rand]
        wb = {'cond':'You can work or take a break', 'act':[]}
        wb['act'].append({'opt':1, 'health':0, 'money':1, 'outcome':None, 'val':'work', 'next':w.copy()})
        wb['act'].append({'opt':2, 'health':1, 'money':0, 'outcome':None, 'val':'break', 'next':{}})
        return wb

    def genGoHomeStory(self):
        done = {'cond':'done'}

        e_home_safe = {'cond':'you get home safely. You must give your family money so they can continue to live', 'act':[]}
        act_give_money = {'opt':1, 'health':0, 'money':-4, 'outcome':'your family lives other day', 'val':'give your family money', 'next':done}
        act_keep_money = {'opt':2, 'health':-99999, 'money':0, 'outcome':'your family does not live', 'val':'don\'t give your family money', 'next':done}
        e_home_safe['act'].append(act_give_money)
        e_home_safe['act'].append(act_keep_money)

        e_go_home = {'cond':'you finish and on your way home pass by a store', 'act':[]}
        act_water = {'opt':1, 'health':1, 'money':-1, 'outcome':None, 'val':'buy water', 'next':e_home_safe}
        act_home = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'don\'t stop', 'next':e_home_safe}
        if (randint(0,100) == 1):
            act_water['health'] = -10
            act_water['money'] = -7
            act_water['outcome'] = 'On your way home you were mugged'
            act_home['health'] = -10
            act_home['money'] = -7   
            act_home['outcome'] = 'On your way home you were mugged'
        e_go_home['act'].append(act_water)
        e_go_home['act'].append(act_home)
        return e_go_home

    def genGetNewJobStory(self):
        e_drugs = {'cond':'you have some drugs you need to sell', 'act':[]}
        act_sell = {'opt':1, 'health':-3, 'money':3, 'outcome':None, 'val':'found someone to sell to', 'next':self.genGoHomeStory()}
        act_take = {'opt':2, 'health':-2, 'money':-1, 'outcome':None, 'val':'take the drugs', 'next':self.genGoHomeStory()}
        e_drugs['act'].append(act_sell)
        e_drugs['act'].append(act_take)

        act_drugs = {'opt':1, 'health':0, 'money':-1, 'outcome':None, 'val':'drugs', 'next':e_drugs}
        if (randint(0,25) == 10):
            act_drugs['outcome'] = "you get mugged and loose all your product"
            act_drugs['health'] = -4
            act_drugs['money'] = -1
            act_drugs['next'] = self.genGoHomeStory()

        ch_job = {'cond':'choose what kind of job you want to have', 'act':[]}
        act_slavery = {'opt':2, 'health':-2, 'money':2, 'outcome':'you get sold to a man for 1 hour', 'val':'sex slavery', 'next':self.genGoHomeStory()}
        act_go_home = {'opt':3, 'health':0, 'money':0, 'outcome':None, 'val':'nevermind, I want to go home', 'next':self.genGoHomeStory()}
        ch_job['act'].append(act_drugs)
        ch_job['act'].append(act_slavery)
        ch_job['act'].append(act_go_home)
        return ch_job

    def genGetFoodStory(self):
        e_food = {'cond':'you go to the local store and get some food', 'act':[]}
        act_yes = {'opt':1, 'health':2, 'money':-1, 'outcome':None, 'val':'cost: 1, health: +2', 'next':self.genGoHomeStory()}
        act_no = {'opt':2, 'health':4, 'money':-2, 'outcome':None, 'val':'cost: 2, health: +4', 'next':self.genGoHomeStory()}
        e_food['act'].append(act_yes)
        e_food['act'].append(act_no)
        return e_food

    def genMap(self):
        e_done_work = {'cond':'you have finished your job for the day', 'act':[]}
        act_new_job = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'look for new job', 'next':self.genGetNewJobStory()}
        act_go_home = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'go home', 'next':self.genGoHomeStory()}
        act_get_food = {'opt':3, 'health':0, 'money':0, 'outcome':None, 'val':'go get food', 'next':self.genGetFoodStory()}
        e_done_work['act'].append(act_new_job)
        e_done_work['act'].append(act_go_home)
        e_done_work['act'].append(act_get_food)

        sorry_c = {'cond':'challenge', 'word':'sorry', 'times':10, 'next':{}}
        work_c = {'cond':'challenge', 'word':'work', 'times':10, 'next':{}}
        electronics_c = {'cond':'challenge', 'word':'electronics', 'times':10, 'next':{}}
        clothes_c = {'cond':'challenge', 'word':'clothes', 'times':10, 'next':{}}
        shoes_c = {'cond':'challenge', 'word':'shoes', 'times':10, 'next':{}}
        double_c = {'cond':'challenge', 'word':'electronics', 'times':10, 'next':{'cond':'challenge', 'word':'clothes', 'times':10, 'next':e_done_work}}
        triple_c = {'cond':'challenge', 'word':'electronics', 'times':10, 'next':{'cond':'challenge', 'word':'clothes', 'times':10, 'next':{'cond':'challenge', 'word':'shoes', 'times':10, 'next':e_done_work}}}

        work_break = {'cond':'You can work or take a break', 'act':[]}
        work_break['act'].append({'opt':1, 'health':0, 'money':1, 'outcome':None, 'val':'work', 'next':self._getRandomWorkBreak()})
        work_break['act'].append({'opt':2, 'health':1, 'money':0, 'outcome':None, 'val':'break', 'next':e_done_work})
        work_break['act'][0]['next']['act'][0]['next']['next'] = e_done_work
        work_break['act'][0]['next']['act'][1]['next'] = e_done_work

        dwork_break = {'cond':'You can work or take a break', 'act':[]}
        dwork_break['act'].append({'opt':1, 'health':0, 'money':1, 'outcome':None, 'val':'work', 'next':double_c.copy()})
        dwork_break['act'].append({'opt':2, 'health':1, 'money':0, 'outcome':None, 'val':'break', 'next':work_break})

        twork_break = {'cond':'You can work or take a break', 'act':[]}
        twork_break['act'].append({'opt':1, 'health':0, 'money':1, 'outcome':None, 'val':'work', 'next':triple_c.copy()})
        twork_break['act'].append({'opt':2, 'health':1, 'money':0, 'outcome':None, 'val':'break', 'next':dwork_break})

        root = {'cond': 'You need to wake up to get to work', 'act':[]}
        root_o1 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 7am', 'next':{}}
        root_o2 = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'wake up at 6am', 'next':{}}
    
        e2 = {'cond':'are you going to walk or run', 'act':[]}
        e2_o1 = {'opt':1, 'health':-2, 'money':0, 'outcome':'Manager is mad. You get beat', 'val':'walk', 'next':{}}
        e2_o2 = {'opt':2, 'health':-1, 'money':0, 'outcome':None, 'val':'run', 'next':{}}
        e2_o3 = {'opt':1, 'health':0, 'money':0, 'outcome':None, 'val':'walk', 'next':{}}
        e2_o4 = {'opt':2, 'health':-1, 'money':0, 'outcome':'You get to work early', 'val':'run', 'next':{}}

        e3 = {'cond':'You can continue to work or take a break', 'act':[]}
        e3_o1 = {'opt':1, 'health':0, 'money':1, 'outcome':None, 'val':'work', 'next':{}}
        e3_o2 = {'opt':2, 'health':1, 'money':0, 'outcome':None, 'val':'break', 'next':{}}

        e4 = {'cond':'You pass by the store on the way', 'act':[]}
        e4_o1 = {'opt':1, 'health':1, 'money':-1, 'outcome':None, 'val':'buy water', 'next':twork_break}
        e4_o2 = {'opt':2, 'health':0, 'money':0, 'outcome':None, 'val':'don\'t stop', 'next':twork_break}


        root['act'].append(root_o1)
        root['act'].append(root_o2)
        e2_1 = e2.copy()
        e2_2 = e2.copy()
        e2_1['act'].append(e2_o1)
        e2_1['act'].append(e2_o2)
        e2_2['act'] = []
        e2_2['act'].append(e2_o3)
        e2_2['act'].append(e2_o4)
        
        e2_o1['next'] = sorry_c.copy()

        e3['act'].append(e3_o1)
        e3['act'].append(e3_o2)
        e3_o1['next'] = work_c
        e3_o1['next']['next'] = e_done_work
        e3_o2['next'] = work_break
        
        e2_o1['next']['next'] = e3

        e4['act'].append(e4_o1)
        e4['act'].append(e4_o2)
        e2_o2['next'] = e4.copy()
        e2_o3['next'] = e4.copy()
        e2_o4['next'] = twork_break

        root_o1['next'] = e2_1
        root_o2['next'] = e2_2

        self.mappola = root
