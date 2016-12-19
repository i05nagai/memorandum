# dual currency bond
* dual currency bond
    * 発行価格:円建て
    * 利子：円建て
    * 償還価格：外貨建て
* reverse dual currency bond
    * 発行価格:円建て
    * 利子：外貨建て
    * 償還価格：円建て
* powered reverse dual currency bond
    * 発行価格:円建て
    * 利子
        * オプション(swaptionなど...)
    * 償還価格：円建て

# reverse floater swap
* $K$:fixed rate
* $L$:floating rate(e.g. LIBOR)
$$
max(K - L * gearing, 0.0)
$$


