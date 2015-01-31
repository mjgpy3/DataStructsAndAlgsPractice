'''
The "interface" for the dicationary ADT
'''
class Dictionary(object):
    def insert(key, value):
        '''
        Adds an item to the dictionary, under `key`. Duplicate inserts overwrite
        the original.
        '''
        raise NotImplementedError('Children must implement insert')

    def delete(key):
        '''
        Removes an item from the dictionary.
        '''
        raise NotImplementedError('Children must implement delete')

    def get(key):
        '''
        Returns the value at a given key.
        '''
        raise NotImplementedError('Children must implement get')

    def __contains__(key):
        '''
        Whether a value is in the dictionary
        '''
        raise NotImplementedError('Children must implement __contains__')
