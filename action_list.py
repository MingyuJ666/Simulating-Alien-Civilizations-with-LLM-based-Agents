class Action_List:
    def __init__(self):
        self.Default = {
            'description': 'Apart from development, there are no other actions, and the result is to update the resources of the next stage through a transfer function matrix.'
        }

        self.Passive = {
            'Civilization Discovered': {
                'Trigger Condition': 'Civilization information is transmitted at the speed of light, and information about the birth of another new civilization has been transmitted to this civilization.',
                'Influence': 'Initiate the triggering of the non-default action list.'
            },
            'Requested for Cooperation': {
                'Trigger Condition': 'Another civilization has decided to request cooperation from you.',
                'Influence': 'Increase the level of understanding between two civilizations; increase the rate of resource growth.'
            },
            'Annihilated': {
                'Trigger Condition': 'Another civilization launched an annihilation war against you, and you lost the war.',
                'Influence': 'This civilization was annihilated.'
            }
        }

        self.Active = {
            'Request for Cooperation': {
                'description': 'You decide to request cooperation from another civilization to achieve mutual benefits and growth.'
            },
            'Annihilate Civilization': {
                'description': 'You launch a war to annihilate another civilization, which may result in gaining their resources or territory.'
            }
        }

