"""
이름 불리면 한 명씩 추월
"""

def solution(players, callings):
    
    dic = {player : i for i, player in enumerate(players)}
    
    for call in callings:
        idx = dic[call]
        dic[call] -= 1
        dic[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
  
    return players