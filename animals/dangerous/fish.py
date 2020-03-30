class Fish:
        def __init__(self):
                ''' Constructor for this class.'''
                #Create some member animals
                self.members = ['Shark','Tuna','Goldfish','Puffer','Piranha','Pollock']
                for i in self.members:
                        if i == 'Goldfish' or i == 'Tuna' or i == 'Pollock':
                                self.members.remove(i)
                        else:
                                continue

        def printMembers(self):
                print('Printing members of the Dangerous Fish class')
                for member in self.members:
                        print('\t%s ' % member)

