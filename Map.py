class Map:  

    def __init__():
        self.game_path = {
    'cond':'You need to wake up to get to work',
     'act': [
        {
            'opt':1, 
            'val': 'wake up at 7am', 
            'pre':[], 
            'next': [
                {
                    'cond': 'you need to get to work',
                    'act': [
                        {
                            'opt':1,
                            'val':'walk',
                            'pre':[],
                            'next':[]
                        },
                        {
                            'opt':2,
                            'val':'run',
                            'pre':[],
                            'next':[]
                        }
                    ]
                }
            ]
        },
        {
            'opt':2, 
            'val': 'wake up at 6am', 
            'pre':[], 
            'next': [
                {
                    'cond': 'you need to get to work',
                    'act': [
                        {
                            'opt':1,
                            'val':'walk',
                            'pre':[],
                            'next':[]
                        },
                        {
                            'opt':2,
                            'val':'run',
                            'pre':[],
                            'next':[]
                        }
                    ]
                }

            ]
        }
    ]
}
        self.position = self.game_path

    def get_map(self):
        return self.game_path;

    def get_position(self):
        return self.position

    def set_poistion(self, pos):
        pass
