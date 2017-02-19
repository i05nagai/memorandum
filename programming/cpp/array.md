## 固定長配列

### 二次元配列
宣言

```cpp
int a[10][20];
```

関数の引数

```cpp
int a[10][20];

// OK
void func(int a[10][20])
{
}

func(a);
```

```cpp
int a[10][20];

// OK
void func(int a[][20])
{
}

func(a);
```

```cpp
int a[10][20];

// OK in C, but not C++
void func2(int row, int col, int a[row][col])
{
}


func(10, 20, a);
```

```cpp
int a[10][20];

// OK
void func2(int row, int col, int a[row][col])
{
}

int* b[10];
for (int i = 0; i < 10; ++10)
{
    b[i] = a[i];
}

func(10, 20, b);
```

* [多次元配列を関数に渡す - Qiita](http://qiita.com/kics/items/a5fc977ed1f003faab1e)
* [プログラミング言語 C の新機能](http://seclan.dll.jp/c99d/c99d04.htm#dt19990719)
