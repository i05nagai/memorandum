---
title: Graph
---

## Graph

## Representation of a graph

#### Option1: adjacent array

`graph[vertex1][vertex2] = 1`

- If there is an edge from `vertex1` to `vertex2`, `1`
- Non direct graph, graph is symmetric
- For graph with weights, graph contains the weight
- For graph with multiple edgets without edgets, graph contains the number of edgets
- Space complexity is $O(V^{2}$,

Check all edges at a vertex

- $O(V)$ complexity

Get all edges

```cpp
for (int i = 0; i < graph.size(); ++i) {
    for (int j = 0; j < graph.size(); ++j) {
        if (graph[i][j] == 1) {
            // (i, j)
        }
    }
}
```

#### Optino2: linked list

`graph[vertex1] = {vertex2, ..., vertexk}`

- If there is an edge from `vertex1` to `vertex2`, append `vertex2` to the list in `graph[vertex1]`.
- Space complexity is $O(V + E)$,

Check all edges at a vertex

- $O(E)$ complexity

Get all edges

```cpp
for (int v = 0; i < graph.size(); ++v) {
    for (int j = 0; j < graph[v].size(); ++j) {
        // (v, graph[v][j])
    }
}
```


#### Option3 edge list

```
struct Edge {
    int from;
    int to;
    int weight;
};

edges = {Edge(v1, v2, w), ..., Edge(v1, vk, w)}
```



## Union find
- Quick find

```
class UnionFind {
public:
    // index corresponds to the vertex num
    std::vector<int> root;
    UnionFind(int size): root(size) {
        for (int i = 0; i < size; ++i) {
            this.root[i] = i;
        }
    }
    int findRoot(int node) {
        return this.root[node];
    }
    void union(int x, int y) {
        int rootX = findRoot(x);
        int rootY = findRoot(y);
        if (rootX != rootY) {
            // update existing root from y to x
            for (int i = 0; i < this.root.size(); ++i) {
                if (this.root[i] == rootY) {
                    this.root[i] = rootX;
                }
            }
        }
    }
    bool connected(int x, int y) {
        return findRoot(x, y);
    }
};
```

- Quick union

```
class UnionFind {
public:
    std::vector<int> root;
    // O(N)
    UnionFind(int size): root(size) {
        for (int i = 0; i < size; ++i) {
            this.root[i] = i;
        }
    }

    // O(logN)
    int find(int x) {
        while (root[x] != x) {
            x = root[x]
        }
        return x;
    }

    // O(logN)
    void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            root[rootY] = rootX;
        }
    }

    // O(logN)
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
}
```

## DFS

```
int dfs(int v) {
    std::vecotor<int> graph[numVertex];
    for (int i = 0; graph[v].size(); ++i) {
        int a = dfs(graph[v][i]);
    }
}
```

- Time complexity


## Kosaraju's algorithm
https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm

## Minimum Spannign Tree

#### Kruskal’s Algorithm
Kruskal’s Algorithm is an algorithm to construct a minimum spanning tree of a weighted undirected graph.

- Time Complexity $O(E \log E)$,
- Space Complexity $O(E \log E)$,

```cpp
class Edge {
public:
  Edge(double w, int from, int to): w(w), from(from), to(to)
  {}
  double w;
  int from;
  int to;
};

bool comp(const Edge& lhs, const Edge& rhs)
{
    return lhs.w < rhs.w;
}

class UnionFind {
public:
  vector<int> vs;
  UnionFind(int size): vs(size) {
    for (int i = 0; i < size; ++i) {
      vs[i] = i;
    }
  }
  int find(int x) {
    return vs[x];
  }
  void connect(int x, int y) {
    int rootX = find(x);
    int rootY = find(y);
    if (rootX != rootY) {
      for (int i = 0; i < vs.size(); ++i) {
        if (vs[i] == rootY) {
          vs[i] = rootX;
        }
      }
    }
  }
  bool connected(int x, int y) {
    return find(x) == find(y);
  }
};

class Solution {
public:
    int run(vector<vector<int>>& points) {
      int numV = points.size();
      vector<Edge> edges;
      UnionFind uf(numV);
      for (int i = 0; i < numV; ++i) {
        for (int j = i + 1; j < numV; ++j) {
          double weight = 1.0;
          edges.push_back(Edge(weight, i, j));
        }
      }
      sort(edges.begin(), edges.end(), comp);
      double sum = 0.0;
      for (int i = 0; i < edges.size(); ++i) {
        Edge e = edges[i];
        if (!uf.connected(e.from, e.to)) {
          uf.connect(e.from, e.to);
          sum += e.w;
        }
      }
      return sum;
    }
};
```

#### Prim algorihtm

- time complexity $O(E \log V)$,
- space complexity $O(V)$,

```cpp
int prim() {
    for (int i = 0; i < V; ++i) {
        mincost[i] = INF;
        used[i] = false;
    }
    mincost[0] = 0;
    int res = 0;
    while (true) {
        int v = -1;
        for (int u = 0; u < V; ++u) {
            if (!used[u] && (v == -1 || mincost[u] < mincost[v]))
                v = u;
        }
        if (v == -1) break;
        used[v] = true;
        res += mincost[v];
        for (int u = 0; u < V; ++u) {
            mincost[u] = min(mincost[u], cost[v][u]);
        }
    }
    return res;
}
```


## Find the shortest path

#### Dijkstra's method

- Time Complexity $O(E \log V)$,
- Space Complexity $O(E)$,
- Cannot use with negative weight


```cpp
// O(V^2) solution
class Solution1 {
public:
    void solve() {
      int numVertex;
      int d[numVertex];
      int used[numVertex];
      int INF = 100000;
      vector<vector<int>> graph(n);
      for (int i = 0; i < numVertex; ++i) {
        graph[i] = vector<int>(numVertex, INF);
      }
      // cost

      fill(d, d + numVertex, INF);
      fill(used, used + numVertex, false);
      d[start] = 0;
      while (true) {
        // find unupdated node
        int v = -1;
        for (int u = 0; u < numVertex; u++) {
          if (!used[u] && (v == -1 || d[u] < d[v])) {
            v = u;
          }
        }

        // cannot updated
        if (v == -1) {
          break;
        }
        used[v] = true;
        for (int u = 0; u < numVertex; ++u) {
          d[u] = min(d[u], d[v] + graph[v][u]);
        }
      }
    }
};

// adjacent list
struct Edge {
    int to;
    int cost;
};
// first: min dist from start, second: vertex num
typdef pair<int, int> P;
class Solution2 {
public:
    void solve() {
      int numVertex;
      int d[numVertex];
      vector<vector<Edge>> graph;
      priority_queue<P, vector<P>, greater<P>> q;
      for (int i = 0; i < numVertex; ++i) {
        graph[i] = vector<int>(numVertex, INF);
      }
      // cost

      fill(d, d + numVertex, INF);
      d[start] = 0;
      q.push(P(0, s));
      while (q.size() > 0) {
        P p = q.top();
        q.pop();
        int v = p.second;
        if (d[v] < p.first) {
            continue;
        }
        for (int i = 0; i < graph[v].size(); ++i) {
            Edge e = graph[v][i];
            // distance is updated
            if (d[e.to] > d[v] + e.cost) {
                d[e.to] = d[v] + e.cost;
                q.push(P(d[e.to], e.to));
            }
        }
      }
    }
};
```

#### Bellman ford method

- Time Complexity $O(VE)$,
- Space Complexity $O(V)$,
- graph cannot contain a cycle with negative weight


```cpp
struct Edge {
    int from;
    int to;
    int cost;
};
class Solution {
public:
    void solution() {
        int INF = 1e7;
        Edge edges[numEdge];
        int d[numVertex];
        fill(d, d+ numVertex, INF);
        d[start] = 0;
        while (true) {
            bool update = false;
            for (int i = 0; i < numEdge; ++i) {
                Edge e = edges[i];
                if (d[e.from] != INF && d[e.to] > d[e.from] + e.cost) {
                    d[e.to] = d[e.from] + e.cost;
                    update = true;
                }
            }
            if (update) break;
        }
    }
};
```

## Traversal
- [Tree traversal \- Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)

#### morris traversal

## Topological sort


## Reference
* [Knuth: The Stanford GraphBase](https://www-cs-faculty.stanford.edu/~knuth/sgb.html)
