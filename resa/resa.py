from enum import Enum

class Room(Enum):
  REFUSE = 0
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

  def __str__(self):
    if self == Room.LARGE:
      return "Large"
    if self == Room.MEDIUM:
      return "Medium"
    if self == Room.SMALL:
      return "Small"
    return "Refused"

def bookMeetingRoom(participants):
  if participants>=1 or participants<=10:
    return Room.SMALL
  elif participants>=11 or participants<=30:
    return Room.MEDIUM
  elif participants>=31 or participants<=50:
    return Room.LARGE
  elif participants<1:
    raise ValueError("Nombre de participants négatif")
  return Room.REFUSE
