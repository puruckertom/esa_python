import unittest

class TestDicts(unittest.TestCase):
    def test_dicts(self):
        """
        A basic introduction to dictionaries
        """
        # Create the variable ``common_to_latin`` and assign to an empty dict
        #**************************************************
        common_to_latin={}
        self.assertEquals(common_to_latin, {})

        # map the string 'Capuchin monkey' to an empty list
        #**************************************************
        common_to_latin['Capuchin monkey']=[]
        self.assertEquals(common_to_latin['Capuchin monkey'], [])
        self.assertTrue('Capuchin monkey' in common_to_latin)

        # map the string 'Squirrel monkey' to the list ['Saimiri sciureus', 'Saimiri oerstedi']
        #**************************************************
        common_to_latin['Squirrel monkey']=['Saimiri sciureus', 'Saimiri oerstedi']
        self.assertEquals(common_to_latin['Squirrel monkey'], ['Saimiri sciureus', 'Saimiri oerstedi'])

        # map the string 'Capuchin monkey' to a list with one element ['Cebus capucinus'] 
        #**************************************************
        common_to_latin['Capuchin monkey']=['Cebus capucinus']
        self.assertEquals(common_to_latin['Capuchin monkey'], ['Cebus capucinus'])

        # use ``in`` to see if 'Howler monkey' is there.
        # assign the results to variable ``howler``
        #**************************************************
        howler = 'Howler monkey' in common_to_latin
        self.assertEquals(howler, False)

        # use ``del`` to remove 'Capuchin monkey'
        #**************************************************
        del common_to_latin['Capuchin monkey']
        self.assertTrue('Capuchin monkey' not in common_to_latin)
        
if __name__ == '__main__':
    unittest.main()
