---
title: Generalized Inverse
---

# Generalized Inverse

## definition
### symbols
* $M(m, n)$
    * $m$行$n$列の行列の集合
* $A^{*}$
    * $A$のエルミート行列とする。

### generalized inverse
$A \in M(m, n)$とする。
以下を満たす$A^{\dagger}$をMoore-Penrose擬似逆行列と呼ぶ。
1. $AA^{\dagger}A = A$
2. $A^{\dagger}AA^{\dagger} = A^{\dagger}$
3. $(AA^{\dagger})^{*} = AA^{\dagger}$
4. $(A^{\dagger}A)^{*} = A^{\dagger}A$

因みに、
$(AA^{\dagger})^{*} = (A^{\dagger})^{*}A^{*}$

#### remark1
一般化逆行列は存在すれば一意。
実際$A$の一般化逆行列が$B, C$と存在するとすると、

### remark2
$(A^{\dagger})^{\dagger} = A$である。
実際、
1. $A^{\dagger}AA^{\dagger} = A^{\dagger}$
2. $AA^{\dagger}A = A$
3. $(A^{\dagger}A)^{*} = A^{\dagger}A$
4. $(AA^{\dagger})^{*} = AA^{\dagger}$

となって、$A$が$A^{\dagger}$に対して1, 2, 3, 4を満たす。

### remark3

## reference
* [pdf](http://www.i-repository.net/il/user_contents/02/.../keidaironshu_062_005_037-047.pdf)
    * かなり良くまとまっている。
