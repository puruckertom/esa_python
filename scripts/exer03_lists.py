import unittest

class TestLists(unittest.TestCase):
    def test_lists(self):
        """
        A basic introduction to lists
        """
        # Create the variable ``bird_list`` and assign to an empty list
        # **************************************************

        self.assertEquals(bird_list, [])

        # Append 'American redstart' and 'Arctic tern' to ``bird_list``
        # **************************************************


        self.assertEquals(bird_list, ['American redstart','Arctic tern' ])

        # Sort ``bird_list`` in reverse order (use help())
        # **************************************************

        self.assertEquals(bird_list,  ['Arctic tern', 'American redstart'])

        # ``extend`` the list ``bird_list`` with ['Northern parula', 'Hooded warbler']
        # **************************************************

        self.assertEquals(bird_list, ['Arctic tern', 'American redstart', 'Northern parula', 'Hooded warbler'])

        # create a variable ``warbler_id`` with the index of 'Hooded warbler' in
        # ``bird_list`` using list methods.
        # **************************************************

        self.assertEquals(warbler_id, 3)
        

if __name__ == '__main__':
    unittest.main()
