class Birds:
        def __init__(self):
                ''' Constructor for this class.'''
                #Create some member animals
                self.members = ['Sparrow','Robin','Hawk','Duck']
                for i in self.members:
                        if i == 'Hawk' or i == 'Eagle':
                                self.members.remove(i)
                        else:
                                continue

        def printMembers(self):
                print('Printing members of the Harmless Birds class')
                for member in self.members:
                        print('\t%s ' % member)
