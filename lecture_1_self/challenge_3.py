from collections import deque
start = "hit"
goal = "cog"
dictionary = {"hot", "dot", "dog", "lot", "log", "cog"}

def word_ladder(start,goal,dictionary):

    if goal not in dictionary:
        return None

    que = deque()
    que.append((start,[start]))


    while que:
        current_word,path = que.popleft()

        if current_word == goal:
            return path

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i]+c  + current_word[i+1:]
                if  next_word in dictionary and next_word not in path:
                    que.append((next_word,path+[next_word]))
    return None
print(word_ladder(start,goal,dictionary))

