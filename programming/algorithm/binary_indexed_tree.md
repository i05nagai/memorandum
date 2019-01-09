---
title: Binary Indexed Tree
---

## Binary Indexed Tree
Binary Indexed tree is also known as fenwick tree.


If $k$ is the number of elements, the number $n$ of elements in array to store data in BIT is $k \le 2^{l} = n$.


## Sample

```cpp
class BinaryIndexTree {
public:
  typedef long long data_type;
  BinaryIndexTree(int size): size_(size), array_size_(0), data_() {
    int array_size = 1;
    while (size_ >= array_size) {
      array_size *= 2;
    }
    array_size_ = array_size;
    data_ = std::unique_ptr<data_type[]>(new data_type[array_size]);
    for (int i = 0; i < array_size; ++i) {
      data_[i] = 0;
    }
  }

  void Add(const int index, const data_type v) {
    int i = index;
    while (i <= array_size_) {
      data_[i] += v;
      i += i & -i;
    }
  }

  data_type Sum(const int index) {
    data_type sum = 0;
    int i = index;
    while (i > 0) {
      sum += data_[i];
      i -= i & -i;
    }
    return sum;
  }
private:
  int size_;
  int array_size_;
  std::unique_ptr<data_type[]> data_;
};
```


## Reference
* [Fenwick tree \- Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)
* [The blue path: Counting inversions in an array using Binary Indexed Tree](http://pavelsimo.blogspot.com/2012/09/counting-inversions-in-array-using-BIT.html)
