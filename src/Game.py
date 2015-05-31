
class Game:

    def __init__(self):
        self.myCurrentFrame = Frame()

    def roll(self, pins):
        if 0 <= pins <= 10:
            self.myCurrentFrame = self.myCurrentFrame.roll(pins)

    def score(self):
        return self.myCurrentFrame.score()

class Frame:

    def __init__(self, previousFrame = None, nextFrame = None, rolls = None ):

        if previousFrame is None:
            self.myPreviousFrame = NilFrame()
        else:
            self.myPreviousFrame = previousFrame

        if nextFrame is None:
            self.myNextFrame = NilFrame()
        else:
            self.myNextFrame = nextFrame

        self.myPreviousFrame.myNextFrame = self
        self.myNextFrame.myPreviousFrame = self

        if rolls is None:
            self.myRolls = []
        else:
            self.myRolls = list(rolls)

    def roll(self, pins):
        self.myRolls.append(pins)

        if self.createPreviousFrameIfComplete():
            self.myRolls = []

        if self.getFrameNumber() == 10:
            return FinalFrame( self.myPreviousFrame )

        return self

    def score(self):
        thePreviousFrameScore = self.myPreviousFrame.score()
        return thePreviousFrameScore + sum(self.myRolls)

    def firstRoll(self):
        if len(self.myRolls) >= 1:
            return self.myRolls[0]
        return 0

    def secondRoll(self):
        if len(self.myRolls) >= 2:
            return self.myRolls[1]
        return 0

    def getFrameNumber(self):
        return self.myPreviousFrame.getFrameNumber() + 1

    def createPreviousFrameIfComplete(self):
        if StrikeFrame.isStrike( self ):
            StrikeFrame( self.myPreviousFrame, self, self.myRolls )
            return True
        elif SpareFrame.isSpare( self ):
            SpareFrame( self.myPreviousFrame, self, self.myRolls )
            return True
        elif Frame.isComplete( self ):
            Frame( self.myPreviousFrame, self, self.myRolls )
            return True

        return False

    @classmethod
    def isComplete(cls, aFrame):
        return len(aFrame.myRolls) == 2

class FinalFrame(Frame):

    def roll(self, pins):
        if self.newRollIsAllowed():
            self.myRolls.append(pins)

        return self

    def newRollIsAllowed(self):
        if len(self.myRolls) <= 1:
            return True

        if len(self.myRolls) == 2:
            if StrikeFrame.isStrike( self ) or SpareFrame.isSpare( self ):
                return True

        return False

class StrikeFrame(Frame):

    def score(self):
        return Frame.score(self) + self.myNextFrame.firstRoll() + self.myNextFrame.secondRoll()

    def secondRoll(self):
        return self.myNextFrame.firstRoll()

    @classmethod
    def isStrike(cls, aFrame):
        return aFrame.firstRoll() == 10

class SpareFrame(Frame):

    def score(self):
        return Frame.score(self) + self.myNextFrame.firstRoll()

    @classmethod
    def isSpare(cls, aFrame):
        return len(aFrame.myRolls) == 2 and sum(aFrame.myRolls) == 10

class NilFrame(Frame):

    def __init__(self):
        pass

    def roll(self, pins):
        theNewFrame = Frame( self, self )
        return theNewFrame.roll(pins)

    def score(self):
        return 0

    def firstRoll(self):
        return 0

    def secondRoll(self):
        return 0

    def getFrameNumber(self):
        return 0


if __name__ == '__main__':
    pass