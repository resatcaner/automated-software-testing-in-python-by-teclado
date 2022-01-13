# Section 3 - Your first automated software

## Links
- [Boundary Value Analysis and Equivalence Partitioning Testing](https://www.guru99.com/equivalence-partitioning-boundary-value-analysis.html)

## Notes
- **Unit Test**: a test which evaluates a part of the code that has no dependency.
- All test suites must be a class. For unit testing it must inherit _TestCase_ from _unittest_.
- Naming: filename_test.py
- test methods should start with test: eg. _test_create_post_
- `self.assertEqual(X, Y)` -> checks if the X = Y
- `self.assertDictEqual(X, Y)` -> checks if DX = DY. Needed for dicts
- `self.assertIsInstance(type, X)` -> checks if X is the type of that.
- `self.assertListEqual(list1, list2)` -> checks if list1 equals to list2
- **System Test**: the tests that checks the complete system, such as interface
- **setUp method: 
```
    def setUp(self):
        """following Blog object will be created seperately for each class"""
        blog = Blog('Test', 'Test Author')  # Create a new object
```
- **patch** : 
```
from unittest.mock import patch
from blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')  # Create a new object
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:  # patches the builtin print method, replacing the function
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)') # calls the function but not checking the result, checking if the function is called with correct params
```
- `with patch('builtins.input', return_value='q'):` -> _return_value_ is mocking the return
- `mocked_object.side_effect = (a,b,c)` is  the variable that has the results in order when the mocked object is called. So this will return a on first call, b on second call and c on the third call. 

#### Boundry Value Analysis:
So these extreme ends like Start- End, Lower- Upper, Maximum-Minimum, Just Inside-Just Outside values are called boundary values and the testing is called “boundary testing”.
The basic idea in normal boundary value testing is to select input variable values at their:
- Minimum
- Just above the minimum
- A nominal value
- Just below the maximum
- Maximum

#### Equivalence Partitioning
Equivalence Partitioning or Equivalence Class Partitioning is type of black box testing technique which can be applied to all levels of software testing like unit, integration, system, etc. In this technique, input data units are divided into equivalent partitions that can be used to derive test cases which reduces time required for testing because of small number of test cases.

- It divides the input data of software into different equivalence data classes.
- You can apply this technique, where there is a range in the input field.