---
title: A/B test
---

## A/B test

以下の仮定のもと、商品list pageのCVRが並び順の変更で変わることがわかる。

1. itemのConversion Rate(Click Rate)は一定
2. 商品listのitemの表示順の変更で, itemをuserが見る確率は変わる
3. itemごとにConversion Rateは異なる
4. 商品list page->item pageの遷移は、同じsession, userであっても、前の遷移に無関係に行動する

2, 3から商品list全体のConversion Rateは表示順の変更で変わる可能性がある。

## Reference
* Dmitriev, P., Gupta, S., Kim, D. W., & Vaz, G. (n.d.). A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments. Permissions@acm.org. KDD ’, 17. https://doi.org/10.1145/3097983.3098024
* Johari, R., Koomen, P., Pekelis, L., & Walsh, D. (n.d.). Peeking at A/B Tests. https://doi.org/10.1145/3097983.3097992
* [A/B Testing: The Complete Guide with Expert Tips from Google & HubSpot](https://www.shopify.com/blog/the-complete-guide-to-ab-testing)
* [Sample Size Calculator (Evan's Awesome A/B Tools)](https://www.evanmiller.org/ab-testing/sample-size.html)
