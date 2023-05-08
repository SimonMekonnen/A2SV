class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r = set(recipes)
        table = defaultdict(int)
        graph = defaultdict(set)
        for i in range(len(ingredients)):
            for j in ingredients[i]:
                    table[recipes[i]] += 1
                    graph[j].add(recipes[i])

        que = deque(supplies)
        ans = []
        while que:
            
            cur = que.popleft()
            ans.append(cur)
            for ing in graph[cur]:
                table[ing] -= 1
                if table[ing] == 0:
                    que.append(ing)
        realans = set()
        for i in ans:
            if i in r:
                realans.add(i)
        return realans
    
            
        