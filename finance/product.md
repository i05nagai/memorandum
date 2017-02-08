---
title: Quanto CMS
---


# Product
デリバティブ商品を網羅的に記すもの。

## Call option

## Put option

## Bull spread option

## Butterfly spread option

## Asian option

## Knock-in (konck-out) option

## Digital Option

## Dual Currency Deposit
* ドル円のdual currency deposit
* Base Currency: JPY
* Alternate Currency: USD
* Strike Rate: $K$
* today: 0
* spot FX rate[USD/JPY] at today: $fx(0)$
* Pricipal amount: $N_{\mathrm{JPY}}$
* Pricinpal amount in alternate currency: $N_{\mathrm{USD}} := N_{\mathrm{JPY}} / fx(0)$
* Coupon: $C$
* expiry date: $T$

為替がexpiry dateに円安になっていれば
* $fx(T) > fx(0)$

$$
    N_{\mathrm{JPY}} C 
$$

為替がexpiry dateに円高になっていれば
* $fx(T) < fx(0)$

$$
    N_{\mathrm{USD}} C
$$

## Dual Currency Deposit Bond

## Referese Dual Currency Bond
元本は円で、利子の払いがドルで行われるような取引。

* Base Currency: JPY
* Alternate Currency: USD
* today: 0
* spot FX rate[USD/JPY] at today: $fx(0)$
* Pricipal amount: $N_{\mathrm{JPY}}$
* Pricinpal amount in alternate currency: $N_{\mathrm{USD}} := N_{\mathrm{JPY}} / fx(0)$
* Coupon: $C$
* expiry date: $T_{N-1}$

$$
    - N_{\mathrm{JPY}} D(0)
    + \sum_{i=0}^{N-1} 
        D(T_{i})
        \left(
             N_{\mathrm{USD}} C_{\mathrm{USD}} 
             - N_{\mathrm{JPY}} C_{\mathrm{JPY}}
        \right)
    + N_{\mathrm{JPY}} D(T_{N-1})
    =
        - N_{\mathrm{JPY}} D(0)
        + \sum_{i=0}^{N-1} D(T_{i}) N_{\mathrm{USD}} C_{\mathrm{USD}} 
        + N_{\mathrm{JPY}} D(T_{N-1})
        - 
        \left(
            - N_{\mathrm{JPY}} D(0)
            + \sum_{i=0}^{N-1} N_{\mathrm{JPY}} C_{\mathrm{JPY}}
            + N_{\mathrm{JPY}} D(T_{N-1})
        \right)
$$

## Power Reverse Dual Currency

$$
    - N_{\mathrm{JPY}} D(0)
    + \sum_{i=0}^{N-1} N_{\mathrm{USD}} C D(T_{i})fx(T_{i})
    + N_{\mathrm{JPY}} D(T_{N-1})
    
$$

## CMS floater


## Callable bond

* 解約権があるもの
* 解約権を行使すれば、元本が償還される
* 解約権を行使するまでは、クーポンが受け取れる
* americal option

## Auto Callable bond

* 解約が自動で行われるもの
* 条件が満たされると元本が償還される
* 条件が満たされるまでは、クーポンが支払われる
* knock-out option


## TARN

## TARF

