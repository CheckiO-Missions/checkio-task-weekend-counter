"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {'input': [[2013, 9, 18], [2013, 9, 23]], 'answer': 2},
        {'input': [[2013, 1, 1], [2013, 2, 1]], 'answer': 8},
        {'input': [[2013, 2, 2], [2013, 2, 3]], 'answer': 2},
        {'input': [[1999, 1, 1], [2000, 1, 1]], 'answer': 105},
        {'input': [[2004, 2, 1], [2004, 2, 29]], 'answer': 9},
        {'input': [[1980, 8, 8], [2012, 3, 3]], 'answer': 3295},
        {'input': [[2001, 2, 2], [2007, 12, 31]], 'answer': 722},
    ],
    "Extra": [
        {'answer': 2, 'input': [[2002, 9, 7], [2002, 9, 8]]},
        {'answer': 0, 'input': [[2002, 9, 9], [2002, 9, 10]]},
        {'answer': 114, 'input': [[2011, 1, 1], [2012, 2, 1]]},
        {'answer': 410, 'input': [[1995, 3, 2], [1999, 2, 3]]},
        {'answer': 827, 'input': [[1992, 2, 1], [2000, 1, 1]]},
        {'answer': 294, 'input': [[1998, 5, 1], [2001, 2, 22]]},
        {'answer': 166, 'input': [[2003, 8, 2], [2005, 3, 3]]},
        {'answer': 94, 'input': [[2010, 2, 5], [2010, 12, 31]]}
    ]
}
