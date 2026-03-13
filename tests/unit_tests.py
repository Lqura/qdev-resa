import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
  def test_medium_room(self):
    self.assertEqual(bookMeetingRoom(27), Room.MEDIUM)

if __name__ == '__main__':
  unittest.main()
