## Toropical Geometry
Toropical Geometry = Tropical semi ring 上の代数幾何

1. 代数幾何
2. Toropical Semi ring
3. ameba, tropical 曲線

代数幾何 = 代数多様体の研究

代数多様体は、集合でなくfunctor.
もしくは、(少なくとも局所的には)方程式系の共通零点.
大域的にはこれらの貼り合わせとして得られる。

$$
    f(x)
    :=
    x(x-1)(x - 2) + 100
    =
    0
$$

が定義するalgebraic manifold.
環$R$を選ぶごとに、$R$における方程式の解の集合

$$
V(R)
=
\left{
    x \in R
    \mid
    f(x) = 0
\right}
$$

が定まる。

* $$V(\mathbb{C})$$,
    * 3点
* $$V(\mathbb{})$$,
    * 1点
* $$V(\mathbb{F}_{p})$$,
* $$V(\mathbb{Z}_{p})$$,
* $$V(\mathbb{Z})$$,

$V$は(Ring)から(Set)への共変functor.

$$
    \phi: R \rightarrow S
$$


Step2

$$f_{i}$$たちの生成する多項式環$$\mathbb{k}[x_{1}, \ldots, x_{2}]$$上のidealを考える。

$$\mathbb{k}$$は、$V$の定義体
Vは($\mathbb{k}$-alg)から(Set)へのfunctor

Step3

商環$$\mathbb{k}[x_{1}, \ldots, x_{n} / I$$を考える。
$$\mathbb{k}[x_{1}, \ldots, x_{n}]/I$$と$$k[y_{1}, \ldots, y_{n}]/J$$が環として同型なら対応する代数多様体も同型。

### proof.

* $R$
    * $\mathbf{k}$-alg
* $V$
    * $I$で定義されるalg. var.
    * algebraic vanety
* $$I := (f_{1}(x_{1},\ldots, x_{n}), \ldots, f_{r}(x_{1}, \ldots, x_{n}))$$,

$$
    V(R)
    =
    \left\{
        (x_{1}, \ldots, x_{n})
        \in R^{n}
        \mid
        f_{1}(x_{1}, \ldots, x_{n})
        =
        \cdots
        =
        f_{r}(x_{1}, \ldots, x_{n})
        =
        0
    \right\}
    \apprx
    \mathrm{Hom}_{\mathbb{k}\mathrm{-alg}}(S_{1}, R)
$$

$$
    \phi
    \in
    \mathrm{Hom}_{\mathbb{k}\mathrm{-alg}}(S_{1}, R)
$$

$$
    (\phi([x_{1}]), \ldots, \phi([x_{n}]))
    \in
    S_{1}
    :=
    \mathbb{k}[x_{1}, \ldots, x_{n}]/I
$$

多項式環は自由な可換環である。
つまり、不定元の行き先を自由に選ぶことと、 多項式環から環への準同型を与えることは同値。
商環$$\mathbb{k}[x_{1}, \ldots, x_{n}]/I$$から$R$への準同型を与えることと、$R$の$n$個の元で、$I$に含まれる全ての方程式の解になっているものを選ぶことは同値。

<div class="end-of-statement" style="text-align: right">■</div>

Remark

任意の有限生成$$\mathbb{k}\mathrm{-alg}$$は、ある$n$と$r$によって、$$\mathbb{k}[x_{1}, \ldots, x_{n}] / (f_{1}(x_{1}, \ldots, x_{n}), \ldots, f_{r}(x_{1}, \ldots, x_{n})$$の形にかける。
Hilbertの定理。

<div class="end-of-statement" style="text-align: right">■</div>

$S$が有限生成とは、$$\exists \alpha_{1}, \ldots, \alpha_{n} \in S$$Nituite,$$\alpha_{1}, \lodts, \alpha_{n}$$をを含む$S$の$\mathbb{k}$-subalgの中で、最小のものが$S$と一致する。

多項式環のUniversality
$$\forall S$$: $$\mathbb{k}\mathrm{-alg}$$, $$\forall \alpha_{1}, \ldots, \alpha_{n} \in S$$について、$$\exists ! \phi: \mathbb{k}[x_{1}, \ldots, x_{n}] \rightarrow S$$が$$\mathbb{k}$$-alg hom.で、$$\phi(x_{i}) = \alpha_{i}\ (i= 1, \ldots, n)$$, 

$$
    \mathrm{fgt}: (\mathbb{k}-\mathrm{-alg}) \rightarrow (\mathbb{k}\mathrm{-vec.sp.}),
    \mathrm{free}: (\mathbb{k}-\mathrm{-vec.sp.}) \rightarrow (\mathbb{k}\mathrm{-alg.}),
    \mathrm{Hom}_{\mathbb{k}\mathrm{-vect}}(V, \mathrm{fgt}(R)),
    =
    \mathrm{Hom}_{\mathbb{k}\mathrm{-alg.}}(\mathrm{free}(V), R),
    V
    =
    \mathrm{span}_{\mathbb{k}}\{x_{1}, \ldots, x_{n}\}
$$

有限生成であることと、多項式環から全射があることは同値。
Hilbertの定理によれば、$$S := \mathbb{k}[x_{1}, \ldots, x_{n}] / (f_{1}, \ldots, f_{r})$$

$$\mathbb{k}$$-alg上の(affine)代数多様体と有限生成$$\mathbb{k}$$-algは一対一の対応がある。
((Aff Scheme /$\mathbb{k}$) \approx $$(\mathbb{k}\mathrm{-alg})^{op}$$)

$$\mathbb{Z}$$上のalg. var.の $\mathbb{Z}$-valued point、$\mathbb{R}$-valued pointにしか興味がなくても、$\mathbb{C}$-valued pointや$$\mathbb{F}_{p}$$-valued point、$$\mathbb{Z}_{p}$$-valued piontを調べることはしばしば約に立つ。
例えば、Weil予想、Mordell予想など。

Tropical manifoldとは、代数多様体のtropical semi ring -valued point.

Franceから見た、Brazilのイメージでついた。
Brazil人のしごとが元になっている。

* $$(\mathbb{R}^{+} := \mathbb{R} \cup \{\infty \}, \odot, \plus)$$,
    * the tropical jsemiring

The tropical addition

$$\oplus; \mathbb{R}^{+} \times \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$$

$$
    x \oplus y
    :=
    \min\{x, y\}
$$

The tropical multiplication

$$\odot: \mathbb{R}^{+} \times \mathbb{R}^{+} \rightarrow \mathbb{R}^{+}$$,

$$
    x \odot y
    :=
    x + y
$$

$$\oplus$$と$\odot$は通常音+と$\times$の持つ性質の多くをもつ。

* $\oplus$のか可換性、結合性
* $\odot$のか可換性、結合性
* 分配則
    * $$(a \oplus b) \odot c = a \odot c \oplus b \odot c$$
* 0が$\odot$の単位元、
* $\infty$が$\oplus$の単位元、

但し、減算はない。
減算なしの4則演算.
引き算しない多項式は、trop. semiring上で考えることができる。
例えば、

$$
    f(x)
    =
    2x^{2} + 3x + 1
$$

trop.化は

$$
    f^{\mathrm{trop.}}(x)
    =
    2 \odot x^{\odot 2}
    \oplus
    3 \odot x
    \oplus
    1
    =
    \min\{2 + x + x, 3 + x, 1\}
$$

これは$$\mathbb{R}^{+}$$から$$\mathbb{R}^{+}$$への写像になっている。
3つのgraphのmin.

Remark

$\oplus$はminのかわりにmaxにすることもできる。
その場合は、単位元は$-\infty$になる。
この場合は、semiringとして同型にできる。

<div class="end-of-statement" style="text-align: right">■</div>

引き算しない有理式は、tropical化されて、区分線形(affine)関数を定める。
組み合わせ論的になる。

* $f$から$f^{\mathrm{trop.}}$への対応はtropicalization
* $f^{\mathrm{trop.}}$から$f$への対応はgeometric lifting

1対1ではない。
情報が失われる。
簡単になる。

tropical化で残る情報は、基本的/本質的である。
tropical多項式の零点は、写像が微分不可能な点。
区分線形の変化点が零点。

$$
    f
    =
    1 + x + y
$$

$$
    f^{\mathrm{trop}}
    =
    \max
    \{
        1, x, y
    \}
$$

$$
    f
    =
    x
        + y
        + \frac{1}{xy}
        + 1
$$

$$
    f^{\mathrm{trop}}
    =
    \max
    \{
        1, x, y, -x-y
    \}
$$

2変数Laurent多項式

$$
    f(x, y)
    =
    \sum_{n,m=-\infty}^{\infty}
        a_{n,m}x^{n}y^{m}
    \quad
    (a_{n,m} \in \mathbb{R})
$$

$$\|\{(n, m) \in \mathbb{Z}^{2} \mid a_{n,m} \neq 0\} \| < \infty$$ に対して、
$f$の定義する$$(\mathbb{R}^{\times})^{2}$$の部分集合

$$
    V_{\mathbb{R}}
    :=
    \{
        (x, y) \in (\mathbb{R}^{\times})^{2}
        \mid
        f(x, y) = 0
    \}
$$

$$(\mathbb{C}^{\times})^{2}$$の部分集合

$$
    V_{\mathbb{C}}
    :=
    \{
        (x, y) \in (\mathbb{C}^{\times})^{2}
        \mid
        f(x, y) = 0
    \}
$$

及びtropical曲線

$$
    V^{\mathrm{trop.}}
    :=
    \{
        (x, y) \in \mathbb{R}^{2}
        \mid
        f^{\mathrm{trop.}}
        \text{ is not differentiable at } (x, y).
    \}
$$

を考えることができる。
$f$がlaurent多項式なので、$0$では定義されない。

Amoeba (Gelfand-Kapranov-Zelevinsky)

* Log: $$(\mathbb{C}^{\times})^{2} \rightarrow \mathbb{R}^{2}$$,

$$
    \mathrm{Log}(z, w)
    :=
    (\log |z|, \log |w|)
$$

$$(\mathbb{C}^{\times})^{2}$$内のalg. var $$V_{\mathbb{C}}$$のLogによる像を$$V_{\mathbb{C}}$$のamoebaと呼ぶ。

e.g.

$$
    V_{\mathbf{C}}
    =
    \{
        (x, y)
        \in (\mathbb{C}^{\times})^{2}
        \mid
        x + y + 1 = 0
    \}
$$

Logのかわりに

$$
    \mathrm{Log}_{t}
    =
    \frac{1}{\log t}
    \mathrm{Log}
$$

を考える。
$f$のかわりに$$f_{t} = x + y + t$$を考えて、$$\mathrm{Log}_{t}(\{f_{t}=0\})$$の(Hausdorff距離に関する)$t \rightarrow \infty$の極限を取ると、$f^{\mathrm{trop.}}$の定めるtropical曲線に一致する。

固定された距離空間の部分集合の集合入る距離。

* $$(X, d)$$
    * a metric space
* $A, B \subset X$

$$
    d_{H}(A, B)
    :=
    \max
    \{
        \max_{a \in A} d(a, B),
        \max_{b \in B} d(A, b),
    \}
$$

$$
    (a, B)
    :=
    \min_{b \in B} d(a, b)
$$


## Other Topics
Stack?

Schemeの拡張。
Schemaは (Ring)から(Set)へのfunctor.
Stackは、(Ring)から(Grpd)へのfunctor.

* Gropoid
    * 全ての射が、isomorphismであるようなcategory
    * Group with many objects
    * Objectが1つのgroupoidはgroup

なぜStackが必要か
空間を割りたい。

* 空間の作り方
    * 切る
        * 方程式の零点
    * 貼る
    * 割る
        * 同値関係による商
        * 代数多様体/schemeではしばしばうまくいかない

なぜうまくいかないか

7 / 3 = 2 + 1

* Geometric Invariant Theory
    * GIT商
    * projectvie spaceの$$\mathbb{RP}^{n}$$の部分
* unstable locus
    * projective spaceの$$\{0\}$$の部分

$$
    \mathbb{RP}^{n}
    :=
    (\mathbb{A}^{n+1} \setminus \{0\} / \mathbb{G}_{m})
    \mathbb{RP}^{n}(\mathbb{C})
    :=
    (\mathbb{C}^{n+1} \setminus \{0\} / \mathbb{C}^{\times})
$$

$$
    7 / 3
    =
    \frac{7}{3}
$$

stack quotient.
これは、orbifoldのなかま。
orbifoldとv manifoldは同じ。




## Reference
