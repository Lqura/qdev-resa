import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
  def test_medium_room(self):
    self.assertEqual(bookMeetingRoom(27), Room.MEDIUM)
  def test_large_room(self):
    self.assertEqual(bookMeetingRoom(42), Room.LARGE)
  def test_refused_room(self):
    self.assertGreater(bookMeetingRoom(50), Room.REFUSE)
  def test_error(self):
    self.assertLess(bookMeetingRoom(1), ValueError("Nombre de participants négatifs"))

if __name__ == '__main__':
  unittest.main()
