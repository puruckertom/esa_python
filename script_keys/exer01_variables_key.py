import unittest

class TestVariables(unittest.TestCase):
    def test_variables(self):
        """
        This is a test method you will need to fill in the content
        where it says and then run it from the proper directory using
        terminal (mac) or the command prompt (windows):
        (ie ``python exer01_variables.py``).
        or run from IDLE or another IDE.
        If it doesn't complain, then you pass- If it complains- fix it!
        """

        # create the variable ``diffusion_rate`` and assign it a float value
        # of 6.0
        # **************************************************
        diffusion_rate = 6.
        self.assertEqual(diffusion_rate, 6.)
        self.assert_(isinstance(diffusion_rate, float))

        # assign ``cohort_size`` to an integer value of 84
        # **************************************************
        cohort_size = 84
        self.assertEqual(cohort_size, 84)
        self.assert_(isinstance(cohort_size, int))

        # create a variable ‘species_name‘ ,
        # and assign it to ’Pieza kake’
        # ********************************************
        species_name = 'Pieza kake'
        self.assertEqual(species_name, "Pieza kake")
        self.assertTrue(isinstance(species_name, str))

# from terminal or DOS shell        
if __name__ == '__main__':
    unittest.main()
