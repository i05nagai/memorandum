---
title: "Techniques for Scientific C++"
---

## 1.6 Containers
Containerは、STL-style(iterator-based)とData/Viewに分かれる。

### 1.6.1 STL-style containers
* 全てのデータを保持する1つのContainer
* Subcontainersは半開区間[iter1, iter2)のiterator rangeで指定される。
* STL-styleであれば、STL内の多くのアルゴリズムが使える。
* 1-dのorderingが必要。
 全てのsubcontainersは1-d orderingなので、multi-dimensional arrayは1-d orderingにならない。
* iteratorは、poiinterをベースとしており、間違いを起こしやすい。
 iteratorにまつわる失敗は多く存在する。
* containerの値返しは難しい。
 代わりに引数として、結果を詰めたいcontainerを渡す。

### 1.6.2 Data/View containers
* container objectの外側にdataが存在する。
 containerはDataのViewを操作するもの。
* multiple containerは同じデータを参照することができが、しかし異なるViewを与える。
* Reference countingが使用される。Dataを参照するHandlerが消えた時Dataも消える。
* multidimensional arrayのsubarrayのように、簡単にsubcontainersを指定できる場合がある。
* subcontainersの型とはcontainerの型は一致することがある。(Array<N> Array<N-1>)
* referene count containerの設計は、注意が必要
* 値渡しや値返しは簡単にできる。

## 1.7 Aliasing and restrict
aliasingは、scientific c++において頭の痛い問題。rank1-matrixのupdateを考える。
$A \leftarrow A + x x^{T}$

```cpp
void rank1Update(Matrix& A, const Vector& x)
{
    for (int i=0; i < A.rows(); ++i) 
        for (int j=0; j < A.cols(); ++j) 
            A(i, j) += x(i) * x(j);
}
```

x(i)をregisterに入れた方が効率的であるが、 コンパイラーはx(i)がループ内で書き変わるかどうか判断できない。

別の問題として、ソフトウェアパイプラインが行われないというものがある。

* ベクトル化は、SIMDで使われている専用の命令"addpd"などを使用しての高速化
* 命令パイプラインは、load, add, mply, storeという命令サイクルを並列に実行して、高速化する。
    * ソフトウェアパイプラインは、命令パイプラインが有効に働くようにコードを最適化する。
次のdaxpy operation <- $y \leftarrow y + a x$を見る。

```cpp
void daxpy(int n, double a, double*x , double*y)
{
    for (int i=0; i < n; ++i)
        y[i] += y[i] + a * x[i];
}
```

パフォーマンスを良くする為に、コンパイラはループを展開し、ソフトゥエアパイプライニングを行う。
ソフトウェアパイプライニングでは、load, store命令の順番をかえる。例えば

```cpp

```

残念なことに、配列xとyがオーバーラップしている可能性があるので、コンパイラは順番をかえることができない。
Fortran 77/99では、配列にaliasingがないことをコンパイラが仮定できる。
これにより20%-50%のパフォーマンスの改善が起こる場合がある。

良いコンパイラはalias解析をし、pointerがover-lapしているかを判定する。
alias解析は、多くのaliasを除去できるが、全てではない。
例えばdaxypyのような処理は、プログラム全体の解析が必要。
プログラム全体の解析をしない限り、aliasの問題は起こる。

Numerical C Extension Group(NCEG)は、restrict keywordを追加した。
restrictはコンパイラにaliasがないことを伝えることができる。例えば、

```cpp

```

コンパイラはrestrictがあれば、load/storeの順番に悩むこと無く最適化を行える。

現在のところ、ISO/ANSI C++ standardにrestrictキーワードは採用されていない。
C99のみ。C++11にも採用されていない。VCは独自拡張で`__restrict`をもつ。

```
valarray classは、aliasを取り除く様に定義されており、これらのクラスのoperationは最適化がされる。
```

restricキーワードはISO/ANSI Cには採用されることが決まっており、C++にも採用されることが期待される。
restrictが使用できるようにコードを書くには、次のようにマクロを使用する。

```cpp

```

いくつかのplatformでは、コンパイラフラグを使用してaliasについての強い仮定をおくことができる。
しかし、これらはポインタの文脈を変更する。

## 1.8 Traits
Traitsは、"Traits: a new and useful template technique," Nahan, Myersがもとになる。
Traitsは、写像で、

* Types
* Cmpile-time konw values(e.g. constant)
* Tuples of the above
* Tuples of the above

から、自分が殆どのもの(types, constants, run-time variables, functions)のへの写像となる。

### 1.8.1 An example: average()
次のコードを考える。

```
template <class T>
T average(const T* data, int numElements)
{
    T sum = 0;
}
```

これは、Tがfloatなら正しく動くが、例えば、

* Tが組み込み型(int, long)の場合は、切り捨てが起こる。
* Tがcharの場合は、すぐにsumがoverflowする。

組み込み型の場合は、常にdoubleを使えば良いが、例えば`complex<float>`のaverageが欲しい場合が問題になる。
そこで、Tが組み込み型の場合は`double`にmapしそれ以外の場合は`T`をそのまま使うようにする。

```cpp

```

mapのドメインはtemplate parameterであり、codomainはclassの中に存在する。
上の例では、`float_tratis::T_float`が適切な型を与えている。

traitsを用いてもとの例を書き直すと

```cpp

```

### 1.8.2 Type promotion example
vector同士の足し算をする場合を考える。

```cpp

```

以下のルールが考えられる。

```
Vector<int> + Vector<int> -> Vector<int>
Vector<int> + Vector<float> -> Vector<float>
Vector<float> + Vector<complex<flaot> > -> Vector<complex<float>>
```

この場合、`float`から`complex<float>`へのmapが必要になる。

traitsを単純に使用した場合次のようになる。

```cpp

```

この方法の欠点は、全ての組み合わせの特殊化を行わなければならない点にある。 
コードを追加で書くのが苦でなければ、もっと良い方法がある。
以下は、Jean-Louis Leroyによる。

* `bool`, `char`, `unsinged char`, `short int`を自動的に`int`に変換する。
* それぞれの型に*presition rank*を割り当てる。
traitsをtypeから"presion rank"へのmapとする。
    * 例えば、`bool`=1, `int`=2, `float`=3, `double`=4, `complex<float>`=5
* 型をより高いpresition rankの型へ変換する。
* もしpresition rankが設定されていない型であれば、

以下が実装例となる。

```cpp
template<class T>
struct precision_trait {
    enum { precisionRank = 0,
        knowPrecisionRank = 0 };
};
#define DECLARE_PRECISION(T,rank) \
    template<> \
struct precision_trait< T > { \
    enum { precisionRank = rank, \
        knowPrecisionRank = 1 }; \
};
    DECLARE_PRECISION(int,100)
    DECLARE_PRECISION(unsigned int,200)
    DECLARE_PRECISION(long,300)
    DECLARE_PRECISION(unsigned long,400)
    DECLARE_PRECISION(float,500)
    DECLARE_PRECISION(double,600)
    DECLARE_PRECISION(long double,700)
    DECLARE_PRECISION(complex<float>,800)
    DECLARE_PRECISION(complex<double>,900)
DECLARE_PRECISION(complex<long double>,1000)
    template<class T>
    struct autopromote_trait {
        typedef T T_numtype;
    };
#define DECLARE_AUTOPROMOTE(T1,T2) \
    template<> \
struct autopromote_trait<T1> { \
    typedef T2 T_numtype; \
};
// These are the odd cases where small integer types
// are automatically promoted to int or unsigned int for
// arithmetic.
    DECLARE_AUTOPROMOTE(bool, int)
    DECLARE_AUTOPROMOTE(char, int)
    DECLARE_AUTOPROMOTE(unsigned char, int)
    DECLARE_AUTOPROMOTE(short int, int)
DECLARE_AUTOPROMOTE(short unsigned int, unsigned int)
    template<class T1, class T2, int promoteToT1>
    struct promote2 {
        typedef T1 T_promote;
    };
template<class T1, class T2>
struct promote2<T1,T2,0> {
    typedef T2 T_promote;
};

template<class T1, class T2>
struct promote2<T1,T2,0> {
    typedef T2 T_promote;
};
template<class T1_orig, class T2_orig>
struct promote_trait {
    // Handle promotion of small integers to int/unsigned int
    typedef _bz_typename autopromote_trait<T1_orig>::T_numtype T1;
    typedef _bz_typename autopromote_trait<T2_orig>::T_numtype T2;
    // True if T1 is higher ranked
    enum {
        T1IsBetter =
            precision_trait<T1>::precisionRank >
            precision_trait<T2>::precisionRank,
        // True if we know ranks for both T1 and T2
        knowBothRanks =
            precision_trait<T1>::knowPrecisionRank
            && precision_trait<T2>::knowPrecisionRank,
        // True if we know T1 but not T2
        knowT1butNotT2 = precision_trait<T1>::knowPrecisionRank
            && !(precision_trait<T2>::knowPrecisionRank),
        // True if we know T2 but not T1
        knowT2butNotT1 = precision_trait<T2>::knowPrecisionRank
            && !(precision_trait<T1>::knowPrecisionRank),
        // True if T1 is bigger than T2
        T1IsLarger = sizeof(T1) >= sizeof(T2),
        // We know T1 but not T2: true
        // We know T2 but not T1: false
        // Otherwise, if T1 is bigger than T2: true
        defaultPromotion = knowT1butNotT2 ? _bz_false :
            (knowT2butNotT1 ? _bz_true : T1IsLarger)
    };
    // If we have both ranks, then use them.
    // If we have only one rank, then use the unknown type.
    // If we have neither rank, then promote to the larger type.
    enum {
        promoteToT1 = (knowBothRanks ? T1IsBetter : defaultPromotion)
            ? 1 : 0
    };
    typedef typename promote2<T1,T2,promoteToT1>::T_promote T_promote;
};
```

# 1.9 Expressin Template
次のような式が問題となる。

```cpp
Vector<double> a, b, c, d;
a = b + c + d;
```

これは次のようなコードを生成する。

```cpp
double* _t1 = new double[N];
for (int i=0; i < N; ++i)
_t1[i] = b[i] + c[i];
double* _t2 = new double[N];
for (int i=0; i < N; ++i)
_t2[i] = _t1[i] + d[i];
for (int i=0; i < N; ++i)
a[i] = _t2[i];
delete [] _t2;
delete [] _t1;
```

### 1.9.1 Performance implications of pairwise evaluation
上のcコードの問題。

arrayが小さい場合は、`new`と`delete`のオーバーヘッドが大きく、1/10程度になる。
中くらいのcacheに収まるarrayの場合は、余分なループの影響が大きく30%-50%遅くなる。
余計なnewで生成される`_t1`のような変数の影響で、キャッシュがすぐあふれる。

large arrayの場合はextra dataのメインメモリとキャッシュの間の転送にコストがかかる。
基本的にscientific codeは(flopsというより）メモリバンド幅に制限されるので、大きな問題になる。
M個の異なるarrayのoperandとN個のoperatorがある場合、M/2N程度の時間がかかる。

特にM=1でNが大きい場合に問題になる。
この場合、1/7, 1/27程度のパフォーマンスになる。

### 1.9.2 Recursive templates
expression templateを理解するために、recursive templateを理解するのが役にたつ。

```cpp

```

自分自身をtemplate parameterにとることができるクラス。
次のような表現が可能になる。

```cpp

```

これは、list `[A, B, C, D]`を表現する。
さらにこれは、以下の木を表現できる。

```cpp

```

### 1.9.3 Expression templates: building parse tree
expression templateの基本的なideaは、opeartor overloadingによってparse treeを作る。

```cpp
Array A, B, C, D;
D = A + B + C;
```

次のように表現できる。

```cpp
X<Array, plus, X<Array, plus, Array> >
```

上の次のように生成できる。

```cpp

```

次のようにparseできる。

```cpp

```

### 1.9.4 A minimal implementation
1-D arrayに対する最小限の実装が次になる。
まず、plusは次のようになる。

```cpp

```

parse treeのnodeは次のようになる。

```cpp
template<typename Left, typename Op, typename Right>
struct X {
    Left leftNode_;
    Right rightNode_;
    X(Left t1, Right t2)
        : leftNode_(t1), rightNode_(t2)
    { }
    double operator[](int i)
    { return Op::apply(leftNode_[i],rightNode_[i]); }
};
```

次がsimple array classになる。

```cpp
struct Array {
    Array(double* data, int N)
        : data_(data), N_(N)
    { }
    // Assign an expression to the array
    template<typename Left, typename Op, typename Right>
        void operator=(X<Left,Op,Right> expression)
        {
            for (int i=0; i < N_; ++i)
                data_[i] = expression[i];
        }
    double operator[](int i)
    { return data_[i]; }
    double* data_;
    int N_;
};
```

次が、operator+の実装になる。

```cpp
template<typename Left>
X<Left, plus, Array> operator+(Left a, Array b)
{
    return X<Left, plus, Array>(a,b);
}
```

次がmainになる。

```cpp
int main()
{
    double a_data[] = { 2, 3, 5, 9 },
           b_data[] = { 1, 0, 0, 1 },
           c_data[] = { 3, 0, 2, 5 },
           d_data[4];
    Array A(a_data,4), B(b_data,4), C(c_data,4), D(d_data,4);
    D = A + B + C;
    for (int i=0; i < 4; ++i)
        cout << D[i] << " ";
    cout << endl;
    return 0;
}
```

このプログラムのアウトプットは次のようになる。

```

```

コンパイラの処理の流れは次のようになる。

```
D = A + B + C;
    = X<Array,plus,Array>(A,B) + C;
    = X<X<Array,plus,Array>,plus,Array>(X<Array, plus,Array>(A,B),C);

```

ここで、Array::operator=が実行される。

```cpp
D.operator=(X<X<Array,plus,Array>,plus,
        Array>(X<Array,plus,Array>(A,B),C) expression)
{
    for (int i=0; i < N_; ++i)
        data_[i] = expression[i];
}
```

`expression[i]`は次のように評価される。

```cpp
data_[i] = plus::apply(X<Array,plus,Array>(A,B)[i], C[i]);
    = plus::apply(A[i],B[i]) + C[i];
    = A[i] + B[i] + C[i];
```

最終的に次のコードが得られる。

```cpp
for (int i=0; i < D.N_; ++i)
    D.data_[i] = A.data_[i] + B.data_[i] + C.data_[i];
```

一時オブジェクトが作られず、single loopになっている。

### 1.9.5 Refinements
真面目に実装すると、arraysそれ自身の代わりにparse treeの中にiteratorsが要求される。
ここで示した基本的な実装の拡張や改善は多く存在する。
compilerに苦しみや痛みを与えるという望みまでの程度にのみ制限される。

```
``My desire to inflict pain on the compilers is large.
They've been tormenting me for the last 8 years. Now's my
chance to strike back!'' --Scott Haney
```

## 1.10 Template metaprograms
template metaprogramsは、小さな開いたのクラスに対する特定のアルゴリズムを生成する場合に有用である。
Value classはdataに対するpointerというより全てのデータを含んでいる。
典型的な例は、Complex number, auaternions, intervals, tensors and small fixed size vectors and matrixである。
アルゴリズムの特殊化は、より制限をつけ高速に動作するように一般的なアルゴリズムを修正したものを意味する。

$N < 10$の小さなオブジェクトに対するいくつかの例を述べると

* Dot products
* Matrix/vector multiply
* Matrix/matrix multiply
* vector expression, tensor expression, matrix expression

などである。

samll object以外で良いパフォーマンスを得る為には、floating pointの複雑なcodeを生成する為のloopを展開する必要がある。
これはtemplate metagramsが、まぁまぁ良いものであるということである。
いくつかのcompilerはこれらの一部を展開するが、全てではない。
template metaprogramsは、下記のFFT exmapleのようにbest compilerの最適化の能力を超えて最適化を行うことをプログラマに強いる。

### 1.10.1 Template metaprograms: some history
C++にtemplateが追加されたとき、それが意図するものより多くのもの得た。
Erwin Unruhは、ISO/ANSI C++ committee mettings in 1994で一つのプログラムを公開した。

```cpp

```

上記のプログラムはコンパイルできないので、役に立たない。
コンパイラは次のエラーをはく

```

```

Unruhのプログラムのtrickは、compiler timeに素数のリストを出力することにある。
C++のtemplateは、自分自身に対するプログラミング言語として解釈される。
if/else/else ifやforやdo while, switch, subroutin callなどの一般的なcontrol flowを持っている。

次がUnruhのものよりSimpleな例である。

```cpp

```

上記の例では、`Fractoral<5>::value`は5!となる。
recursive templateは`while`のように動作し、`Fractoral<1>`はloopを止める。
compile timeのtemplateによる計算に制限はあるか？
理論的には、ない！templateの仕様はチューリング完全である。
つまり、

1. 任意の計算はC++ compilerが行うことができる。
2. C++は与えられたプログラムの処理がcompiler時に決定できない時計算をやめる。

実用的には、リソースの制限によりmetaprogramでできることは限られている。
多くのcompilerは再帰的なinstance化に制限をかけているが、それでも十分有用である。

### 1.10.2 The need for specilized algorithms
多くのアルゴリズムは、特殊化で高速にできる。
以下が例になる。

```cpp

```

図1.2が*dot()*のvectorの長さに対するパフォーマンスである。
小さいvectorに対しては、performanceが悪い。（ループのoverheadが大きく）
パフォーマンスをあげるために、Nが3の場合に特殊化できる。

```cpp

```

このversionがpeak speedで動作する。
loopのoverheadを無くしている。
関数の呼び出しのOverheadをなくすことで、floating-operationが連続して行われること、registerにデータが登録されることを許可している。

これにより$n_{1/2} \rightarrow 0$となり、また$R_{peak}$を上回ることもある。

### 1.10.3 Using template metaprograms to specialized algorithms
C++ compilerをinterpreterとするtrickとnormal C++ codeを組み合わせることで、specialized algorithmが作れる。
次が、特殊なdot productを生成するtemplate metaprogramである。

```cpp

```

```cpp

```

いくつかのcompilerでは自動的にこれらの展開を行う。
しかし以下は、もっと洗練された例である。
FFT変換のmetaprogramで、1の根を計算し、compile timeに配列の並び替えを行い、floating-point codeのblockを出力する。

```cpp

```

## 1.11 Comma overloading
C++では、カンマ演算子をオーバーロードできる。
データの初期化の良い記法を与える。

```cpp

```

上記のコードは次のように解釈される。

```cpp

```

なので、`A = 0.1`が特別な型を返す必要がある。
次が単純な例になる。

```cpp

```

