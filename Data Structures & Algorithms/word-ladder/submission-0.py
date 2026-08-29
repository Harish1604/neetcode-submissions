class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord,1)])

        while queue:

            word, step = queue.popleft()

            if word == endWord:
                return step
            
            for i in range(len(word)):
                for ch in "qwertyuioplkjhgfdsazxcvbnm":
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord,step+1))
        return 0

