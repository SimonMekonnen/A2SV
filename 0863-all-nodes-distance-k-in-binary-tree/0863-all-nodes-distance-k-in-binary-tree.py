# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        
        def dfs(root):
            if not root:
                return 
            if root.left:
                graph[root.val].add(root.left.val)
                graph[root.left.val].add(root.val)
            if root.right:
                graph[root.val].add(root.right.val)
                graph[root.right.val].add(root.val)
            dfs(root.left)
            dfs(root.right)
      
        dfs(root)
        que = deque([target.val])
        level = 0
        visited = set()
        visited.add(target.val)
        while que and level != k:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                for neigh in graph[cur]:
                    if neigh not in visited:
                        que.append(neigh)
                        visited.add(neigh)
            level += 1
        
     
        return list(que)
                
            
        