import unittest
from Game import Game

class TestGame(unittest.TestCase):


    def testGutterGame(self):
        self.assertScoreForRolls( [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0 ], 0 )

    def testExampleInDescription(self):
        self.assertScoreForRolls( [1,4, 4,5, 6,4, 5,5, 10, 0,1, 7,3, 6,4, 10, 2,8,6 ], 133 )

    def testRollAndScore(self):

        self.assertScoreForRolls( [0], 0 )
        self.assertScoreForRolls( [1], 1 )
        self.assertScoreForRolls( [2], 2 )
        self.assertScoreForRolls( [3], 3 )
        self.assertScoreForRolls( [4], 4 )
        self.assertScoreForRolls( [8], 8 )
        self.assertScoreForRolls( [9], 9 )

        self.assertScoreForRolls( [0, 1], 1 )
        self.assertScoreForRolls( [1, 0], 1 )

        self.assertScoreForRolls( [1, 2], 3 )
        self.assertScoreForRolls( [2, 3], 5 )
        self.assertScoreForRolls( [4, 5], 9 )
        self.assertScoreForRolls( [1, 3], 4 )
        self.assertScoreForRolls( [3, 5], 8 )

        self.assertScoreForRolls( [0, 1, 1], 2 )
        self.assertScoreForRolls( [0, 1, 2], 3 )

        self.assertScoreForRolls( [1, 2, 3], 6 )
        self.assertScoreForRolls( [2, 4, 5], 11 )

        self.assertScoreForRolls( [1,2,3,4,5,4,7,2], 28 )
        self.assertScoreForRolls( [3,2,1,4,9,0,4,2], 25 )

        self.assertScoreForRolls( [1,2, 3,4, 5,4, 7,2, 2,3], 33 )

        self.assertScoreForRolls( [1,2, 3,4, 5,4, 7,2, 2,3, 1,2, 3,4, 5,4, 7,2, 2,3 ], 66 )


    def testRollAndScoreForSpares(self):
        self.assertScoreForRolls( [1,9, 1], 12 )
        self.assertScoreForRolls( [4,6, 3], 16 )
        self.assertScoreForRolls( [5,5, 2], 14 )

        self.assertScoreForRolls( [1,9, 1,5, 7,3 ], 27 )
        self.assertScoreForRolls( [1,9, 1,5, 7,3, 2 ], 31 )

        self.assertScoreForRolls( [4,6, 3,2, 1,8, 3,6, 4,5, 8,2, 8,2, 8,1, 6,3 ], 99 )

        self.assertScoreForRolls( [4,6, 3,2, 1,8, 3,6, 4,5, 8,2, 8,2, 8,1, 6,3, 3,7 ], 109 )
        self.assertScoreForRolls( [4,6, 3,2, 1,8, 3,6, 4,5, 8,2, 8,2, 8,1, 6,3, 3,7,6 ], 115 )


    def testRollAndScoreForStrikes(self):
        self.assertScoreForRolls( [10], 10 )
        self.assertScoreForRolls( [10, 2], 14 )
        self.assertScoreForRolls( [10, 2,6], 26 )

        self.assertScoreForRolls( [10, 2,6, 1,8, 10, 4,5, 10, 10, 8,1, 6,3, 3,3 ], 134 )

        self.assertScoreForRolls( [10, 2,6, 1,8, 10, 4,5, 10, 10, 8,1, 10, 3,3 ], 141 )

        self.assertScoreForRolls( [10, 2,6, 1,8, 10, 4,5, 10, 10, 8,1, 10, 10,3 ], 155 )
        self.assertScoreForRolls( [10, 2,6, 1,8, 10, 4,5, 10, 10, 8,1, 10, 10,3,5 ], 160 )

        self.assertScoreForRolls( [10, 10, 10, 10, 10, 0,0, 0,0, 0,0, 0,0, 10,10,10 ], 150 )

        self.assertScoreForRolls( [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,10,5 ], 295 )
        self.assertScoreForRolls( [10, 10, 10, 10, 10, 10, 10, 10, 10, 10,10,10 ], 300 )


    def testSparesAndStrikes(self):

        self.assertScoreForRolls( [10, 4,6, 10, 10, 5,5, 10, 10, 8,2, 10, 2,8,5 ], 208 )


    def testIgnoresExtraRolls(self):

        # no spares or strikes
        self.assertScoreForRolls( [1,2, 3,4, 5,4, 7,2, 2,3, 1,2, 3,4, 5,4, 7,2, 2,3, 4 ], 66 )

        #spares
        self.assertScoreForRolls( [4,6, 3,2, 1,8, 3,6, 4,5, 8,2, 8,2, 8,1, 6,3, 3,7,6, 4 ], 115 )

        #strikes
        self.assertScoreForRolls( [10, 2,6, 1,8, 10, 4,5, 10, 10, 8,1, 10, 10,3,5, 7 ], 160 )


    def testRollEdgeCases(self):

        self.assertScoreForRolls( [-1], 0 )
        self.assertScoreForRolls( [11], 0 )
        self.assertScoreForRolls( [999], 0 )

    def assertScoreForRolls(self, rolls, expectedScore, msg = None):
        theGame = Game()

        for roll in rolls:
            theGame.roll(roll)

        theActualScore = theGame.score()

        if theActualScore != expectedScore:
            print 'expected score: %d, but got score: %d' % ( expectedScore, theActualScore )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

