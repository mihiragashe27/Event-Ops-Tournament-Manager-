import numpy as np


class Participant:

  def __init__(self, name):
    self.name = name
    self.scores = []  

  def add_score(self, score):
    self.scores.append(score)


class EventManager:

  def __init__(self):
    self.participants = []  

  def add_participant(self, name):
    
    new_player = Participant(name)
    self.participants.append(new_player)

  def get_leaderboard(self):
    
    names = []
    for p in self.participants:
      names.append(p.name)

    
    avg_scores = []
    for p in self.participants:
      
      if len(p.scores) > 0:
        player_avg = np.mean(p.scores)
        avg_scores.append(player_avg)
      else:
        avg_scores.append(0)

    
    sorted_indices = np.argsort(avg_scores)

    
    reversed_indices = sorted_indices[::-1]

    
    print("\n--- LEADERBOARD ---")

    rank = 1
    for idx in reversed_indices:
      player_name = names[idx]
      player_score = avg_scores[idx]

      print(f"{rank}. {player_name} - Avg Score: {player_score:.2f}")

      rank = rank + 1  # Increment rank for the next player



if __name__ == "__main__":
  manager = EventManager()

  
  manager.add_participant("Mit A")
  manager.add_participant("Mit B")

  
  manager.participants[0].add_score(85)
  manager.participants[0].add_score(90)

  
  manager.participants[1].add_score(95)
  manager.participants[1].add_score(70)

  
  manager.get_leaderboard()
