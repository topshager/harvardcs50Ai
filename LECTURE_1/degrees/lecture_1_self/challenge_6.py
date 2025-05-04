"""
✅ 4. Word Morph Puzzle (Custom Dictionary)
Given:

python
Copy code
start = "cold"
goal = "warm"
dictionary = {"cold", "cord", "card", "ward", "warm", "core", "care"}
"""

from collections import deque




def word_Morph(start,goal,dictionary):
    if goal not in dictionary:
        return None

    que = deque()
    visited = set()
    que.append((start,[start]))

    while que:

       current_word,path = que.popleft()

       if current_word == goal:
           return path


       for i in range(len(current_word)):
          for c in 'abcdefghijklmnopqrstuvwxyz':
              if c != current_word[i]:
                  next_word = current_word[:i] + c + current_word[i+1:]
                  if next_word in dictionary and next_word not in visited:
                      visited.add(next_word)
                      que.append((next_word,path+[next_word]))
    return None
  
        
    
start = "cold"
goal = "warm"
dictionary = {"cold", "cord", "card", "ward", "warm", "core", "care"}


print(word_Morph(start,goal,dictionary))






