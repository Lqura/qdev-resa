from enum import Enum

class Room(Enum):
  REFUSE = 0
  SMALL = 1
  MEDIUM = 2
  LARGE = 3
  
def bookMeetingRoom(participants):
  return Room.REFUSE
