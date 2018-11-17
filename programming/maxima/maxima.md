---
title: Maxima
---

## Maxima

## Install

For OSX,

```
# you need to install maxima to use wxmaxima
brew install maxima
brew install wxmaxima
```

## Commands

Define functions

```
f(x,y):=(a*x^2 + b*x*y);
```

Calculate hessian matrix

```
hessian(f(x, y), [x, y]);
```

Eigen values

```
A: matrix([1, 1], [1, 1]);
eigenvalues(A)
# [[eigenvalues], [multiplicity of eigenvalues]]
```

Eigen values

```
A: matrix([1, 1], [1, 1]);
eigenvectors(A);
# [[[eigenvalues], [dimension of eivenspace]], [eigenvectors]]
```

## Tips

### Solve Ax= b
[Solving the matrix vector equation Ax=b in Maxima – The MaximaList](https://themaximalist.org/2017/02/28/solving-the-matrix-vector-equation-axb-in-maxima/)

```
matsolve(A,b):=block(
   [AugU],
   AugU:echelon(addcol(A,b)),
   backsolve(AugU)
 );

backsolve(augU):=block(
 [i,j,m,n,b,x,klist,k,np,nosoln:false],
 [m,n]:matsize(augU),
 b:col(augU,n),
 klist:makelist(concat('%k,i),i,1,n-1),
 k:0,
 x:transpose(matrix(klist)),
 for i:m thru 1 step -1 do (
   np:pivot(row(augU,i)), 
   if is(equal(np,n)) then
     (nosoln:true,return())
   else if not(is(equal(np,0))) then
     (x[np]:b[i],
     for j:np+1 thru n-1 do
       x[np]:x[np]-augU[i,j]*x[j])
    ),
 if nosoln then 
    return([])
 else 
   return(expand(x)) 
)$

matsize(A):=[length(A),length(transpose(A))]$

pivot(rr):=block([i,rlen],
 p:0,
 rlen:length(transpose(rr)),
 for i:1 thru rlen do( 
 if is(equal(part(rr,1,i),1)) then (p:i,return())), 
 return(p)
)$
```

## Reference
* [Solve Ax=b in Maxima, part 2 – The MaximaList](https://themaximalist.org/2017/03/02/solve-axb-in-maxima-part-2/)
