bool isCycle(int V, vector<int> adj[]) {
        vector<int> visited(V, 0);
        int cycle = 0;

        function<void(int, int)> dfs = [&](int node, int parent) {
            if (visited[node] == 1) {
                return;
            }

            visited[node] = 1;
            for (int neigh : adj[node]) {
                if (visited[neigh] == 0) {
                    dfs(neigh, node);
                } else {
                    if (neigh != parent) {
                        cycle = 1;
                        return;
                    }
                }
            }
        };

        for (int i = 0; i < V; i++) {
            if (cycle == 1) {
                break;
            }
            if (visited[i] != 1) {
                dfs(i, -1);
            }
        }

        return cycle == 1;
    }
};
