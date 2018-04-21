Pricing Spread Options by the Operator Splitting Method
=======================================================

論文の概要
----------
`Pricing Spread Options by the Operator Splitting Method`_ の概要。

.. _Pricing Spread Options by the Operator Splitting Method: http://papers.ssrn.com/sol3/Papers.cfm?abstract_id=2429696

* IR, FX, commodity marketでpopularなspread optionのpricingの話。
* spread optionは幾何ブラウン運動に対する解析的な結果はput/callでも知られていない。
* 幾何ブラウン運動を仮定した場合のcall optionの近似解として :ref:`Kirk's approximation` と呼ばれる近似が知られているが、理論的な解析はされていない。
* 本論文では、 :ref:`Lie-Trotter operator splitting method` を用いて :ref:`Kirk's approximation` の近似式が得られることを示す。
* また高次のoperator splittingを用いて、 :ref:`Kirk's approximation` より精度の良い近似式が得られることを示す。

設定
-----
原資産 :math:`F_{1}, F_{2}` が対数正規過程とする。
つまり、

.. math::
 \,d F_{1}(t) 
 & = \mu_{1}F_{1}(t)\,dt
 + \sigma_{1} F_{1}(t) \,d W_{1}(t) \\
 \,d F_{2}(t) 
 & =  \mu_{1}F_{2}(t)\,dt
 +\sigma_{2} F_{2}(t) \,d W_{2}(t) \\
 \,d \langle W_{1}, W_{2} \rangle (t) 
 & = \rho \,d t, \\
 \,d B(t) 
 & = rB(t) \,d t

ここで、 :math:`\sigma_{1}, \sigma_{2}, r` は定数で、 :math:`W_{1}, W_{2}` はリスク中立測度のもとでのブラウン運動である。
:math:`B` はMoney Market accountで、 :math:`r` は金利。
:math:`\rho` はブラウン運動間の相関を表すを表す定数である。

spreadを :math:`F:= F_{1} - F_{2}` とすると、 :ref:`Kirk's approximation` は以下となる。

.. math::
 p = \alpha \Phi \left( \ln \left( \frac{\alpha}{\gamma + \kappa} \right) + \frac{\sigma^{K}}{2} \right)
  - (\gamma + \kappa) \Phi \left( \frac{\ln \left(\frac{\alpha}{\gamma + \kappa} \right)}{\sigma^{K}} - \frac{\sigma^{K}}{2} \right)

ただし、

.. math::
 \sigma^{K} 
 & := \sqrt{\beta^{2} - 2\rho\beta\rho\frac{\gamma}{\gamma+\kappa} + \delta^{2}\left(\frac{\gamma}{\gamma + \kappa}\right)^{2}}, \\
 \alpha
 & = F_{1}(0)e^{\mu_{1}T}, \\
 \beta
 & = \sigma_{1}\sqrt{T}, \\
 \gamma
 & = F_{2}(0)e^{\mu_{2}T}, \\
 \delta
 & = \sigma_{2}\sqrt{T}, \\
 \kappa
 & = Ke^{-rT}.

Lie-Trotter operator splittingによるKirk's approx.の導出
--------------------------------------------------------

複製ポートフォリオの議論より以下のPDEを得る。

.. math::
 \left\{\frac{1}{2}\sigma_{1}^{2}F_{1}^{2}\frac{\partial^{2}}{\partial F_{1}^{2}}
 + \rho \sigma_{1}\sigma_{2}F_{1}F_{2}\frac{\partial^{2}}{\partial F_{1}\partial F_{2}}
 + \frac{1}{2}\sigma_{2}^{2}F_{2}^{2}\frac{\partial^{2}}{\partial F_{2}^{2}} - r - \frac{\partial}{\partial \tau} \right\} P(F_{1}, F_{2}, \tau) 
 = 0

 P(F_{1}, F_{2}, 0) = \mathrm{max}(F_{1} - F_{2} - K, 0)

実際 :math:`P(F_{1}, F_{2}, t)` を :math:`t` 時点のEuropean Call Spread optionの価格を :math:`P(F_{1}, F_{2}, t)` とすると以下を満たす :math:`a_{1}, a_{2}, b` が存在するので、

.. math::
 P(F_{1}(t), F_{2}(t), t) 
 = a_{1}(t)F_{1}(t) + a_{2}F_{2}(t) + b(t)B(t) \\

より、右辺は

.. math::
 & \,d (a_{1}(t)F_{1}(t) + a_{2}F_{2}(t) + b(t)B(t)) \\
 & = a_{1}(t)\,d F_{1}(t) + a_{2}(t)\,d F_{2}(t) + b(t)\,d B(t) \\
 & = \left( a_{1}(t)\mu_{1}F_{1}(t) + a_{2}(t)\mu_{2}F_{2} + b(t)rB(t) \right)\,dt
 + a_{1}(t)\sigma_{1}F_{1}(t)\,dW_{1}(t) 
 + a_{2}(t)\sigma_{2}F_{2}(t)\,dW_{2}(t) 

が成立する。
また、左辺は伊藤の公式より

.. math::
 \,d P 
 & = \left( \frac{\partial P}{\partial F_{1}}\mu_{1}F_{1} 
 + \frac{\partial P}{\partial F_{2}}\mu_{2}F_{2} 
 + \frac{1}{2}\frac{\partial^{2} P}{\partial F_{1}^{2}}\sigma_{1}^{2}F_{1}^{2}
 + \frac{\partial^{2} P}{\partial F_{1} \partial F_{2}}\rho\sigma_{1}\sigma_{2}F_{1}F_{2}
 + \frac{1}{2}\frac{\partial^{2} P}{\partial F_{2}^{2}}\sigma_{2}^{2}F_{2}^{2} \right) \,dt \\
 & + \frac{\partial P}{\partial F_{1}}\sigma_{1}F_{1}\,dW_{1}(t)
 + \frac{\partial P}{\partial F_{2}}\sigma_{2}F_{2}\,dW_{2}(t)

両辺を比較すると、

.. math::
 a_{1}(t) 
 & = \frac{\partial P}{\partial F_{1}} \\
 a_{2}(t) 
 & = \frac{\partial P}{\partial F_{2}} \\
 a_{1}(t)\mu_{1}F_{1}(t) + a_{2}(t)\mu_{2}F_{2} + b(t)rB(t)
 & = \frac{\partial P}{\partial F_{1}}\mu_{1}F_{1} 
 + \frac{\partial P}{\partial F_{2}}\mu_{2}F_{2} 
 + \frac{1}{2}\frac{\partial^{2} P}{\partial F_{1}^{2}}\sigma_{1}^{2}F_{1}^{2}
 + \frac{\partial^{2} P}{\partial F_{1} \partial F_{2}}\rho\sigma_{1}\sigma_{2}F_{1}F_{2}
 + \frac{1}{2}\frac{\partial^{2} P}{\partial F_{2}^{2}}\sigma_{2}^{2}F_{2}^{2} 
 P(F_{1}(t), F_{2}(t), t) 
 & = a_{1}(t)F_{1}(t) + a_{2}F_{2}(t) + b(t)B(t) \\

より、 :math:`a_{1}, a_{2}, b` を消去できる。
最後に :math:`\tilde{P}(F_{1}, F_{2}, t) := P(F_{1}, F_{2}, T - t)` とし、 :math:`\tilde{P}` を改めて :math:`P` とおけばよい。

さて、

.. math::
 R_{1} 
 & := \frac{F_{1}}{F_{2} + K}, \\
 R_{2} 
 & := F_{2} + K

とおくと、上記のPDEは次のように書ける。

.. math::
 \left( L_{0} + L_{1} - r - \frac{\partial }{\partial t} \right) P(R_{1}, R_{2}, t) = 0,

.. math::
 L_{0} 
 & := \frac{1}{2}\tilde{\sigma}^{2}R_{1}^{2}\frac{\partial^{2}}{\partial R_{1}^{2}}, \\
 L_{1} 
 & := \frac{1}{2}\tilde{\sigma_{2}}^{2}R_{2}^{2}\frac{\partial^{2}}{\partial R_{2}^{2}} 
 + (\rho\sigma_{1} - \tilde{\sigma_{2}})\tilde{\sigma_{2}}R_{1}R_{2}\frac{\partial}{\partial R_{1} \partial R_{2}} 
 - (\rho\sigma_{1} - \tilde{\sigma_{2}})\tilde{\sigma_{2}}R_{1}\frac{\partial}{\partial R_{1}},\\
 \tilde{\sigma} 
 & := \sqrt{\sigma_{1}^{2} - 2\rho\sigma_{1}\tilde{\sigma_{2}} + \tilde{\sigma_{2}}^{2}} \\
 \tilde{\sigma_{2}} 
 & := \sigma_{2} \left( \frac{F_{2}}{F_{2} + K} \right) 
 :label: definition_sigma2_tilde

境界条件は

.. math::
 P(R_{1}, R_{2}, 0) = R_{2} \mathrm{max}(R_{1} - 1, 0)

境界条件は明らか。
PDEについては、

.. math::
 F_{1}(R_{1}, R_{2}) 
 & := R_{1}R_{2}, \\
 F_{2}(R_{1}, R_{2}) 
 & := R_{2} - K, \\
 C(R_{1}, R_{2}, t) 
 & := P(F_{1}(R_{1}, R_{2}), F_{2}(R_{1}, R_{2}), t), \\

とおくと

.. math::
 \frac{\partial F_{1}}{\partial R_{1}} & = R_{2}, 
 \frac{\partial F_{1}}{\partial R_{2}} & = R_{1}, \\
 \frac{\partial F_{2}}{\partial R_{1}} & = 0,
 \frac{\partial F_{2}}{\partial R_{2}} & = 1, \\

.. math::
 \frac{\partial C}{\partial R_{1}} 
 & = \frac{\partial P}{\partial F_{1}}\frac{\partial F_{1}}{\partial R_{1}} 
 + \frac{\partial P}{\partial F_{2}}\frac{\partial F_{2}}{\partial R_{1}} \\
 & = R_{2}\frac{\partial P}{\partial F_{1}} ,

 \frac{\partial C}{\partial R_{2}} 
 & = \frac{\partial P}{\partial F_{1}}\frac{\partial F_{1}}{\partial R_{2}} 
 + \frac{\partial P}{\partial F_{2}}\frac{\partial F_{2}}{\partial R_{2}} \\
 & = R_{1}\frac{\partial P}{\partial F_{1}}
 + \frac{\partial P}{\partial F_{2}},

.. math::
 \frac{\partial^{2} C}{\partial R_{1}^{2}} 
 & = \frac{\partial }{\partial R_{1}}\left(\frac{\partial P}{\partial F_{1}}\frac{\partial F_{1}}{\partial R_{1}} \right) \\
 & = R_{2}^{2}\frac{\partial^{2} P}{\partial F_{1}^{2}},

.. math::
    \frac{\partial^{2} C}{\partial R_{1} \partial R_{2}} 
    & = \frac{\partial }{\partial R_{2}}\left( R_{2}\frac{\partial P}{\partial F_{1}} \right) \\
    & = \frac{\partial P}{\partial F_{1}}
    + R_{2}\frac{\partial}{\partial F_{1}} \left(\frac{\partial P}{\partial F_{1}}R_{1} + \frac{\partial P}{\partial F_{2}}\right) \\
    & = \frac{\partial}{\partial F_{1}}P
    + R_{1}R_{2}\frac{\partial^{2}}{\partial F_{1}^{2}}P
    + R_{2}\frac{\partial^{2}}{\partial F_{1} \partial F_{2}}P \\

.. math::
 \frac{\partial^{2} C}{\partial R_{2}^{2}} 
 & = \frac{\partial}{\partial R_{2}}\left(R_{1}\frac{\partial P}{\partial F_{1}} + \frac{\partial P}{\partial F_{2}}\right) \\
 & = R_{1}^{2}\frac{\partial}{\partial F_{1}^{2}}P
 + 2R_{1}\frac{\partial}{\partial F_{1} \partial F_{2}}P
 + \frac{\partial^{2}}{\partial F_{2}^{2}}P \\

より、

.. math::
 \frac{\partial^{2} P}{\partial F_{1}^{2}}
 & = \frac{1}{R_{2}^{2}}\frac{\partial^{2} C}{\partial R_{1}^{2}}, \\
 \frac{\partial^{2} P}{\partial F_{1} \partial F_{2}}
 & = \frac{\partial^{2} C}{\partial R_{1} \partial R_{2}} 
 - \frac{1}{R_{2}}\frac{\partial C}{\partial R_{1}} 
 - \frac{R_{1}}{R_{2}}\frac{\partial^{2} C}{\partial R_{1}^{2}} \\
 \frac{\partial^{2} P}{\partial F_{2}^{2}} 
 & = \frac{\partial^{2} C}{\partial R_{2}^{2}}
 - \frac{R_{1}^{2}}{R_{2}^{2}}\frac{\partial^{2} C}{\partial R_{1}^{2}} 
 - 2R_{1}\frac{\partial^{2} C}{\partial R_{1} \partial R_{2}}
 + 2\frac{R_{1}}{R_{2}}\frac{\partial C}{\partial R_{1}}
 + 2\frac{R_{1}^{2}}{R_{2}}\frac{\partial^{2} C}{\partial R_{1}^{2}}
 

が成立。
これをもとのPDEに代入し、 :math:`C(R_{1}, R_{2}, t)` を改めて :math:`P(R_{1}, R_{2}, t)` とおけば良い。

次に、PDEを近似的に解く。
初期値 :math:`x \in \mathbb{R}^{d}` 、微分作用素 :math:`L` の微分方程式の解を :math:`\gamma_{x}^{L}(t)` と書く。
つまり、 :math:`\gamma_{x}^{L}(t)` は次を満たす。

.. math::
 \frac{\,d\gamma_{x}^{L}(t)}{\,dt} 
 & = L\gamma_{x}^{L}(t) \\
 \gamma_{x}^{L}(0) 
 & = x.

微分作用素 :math:`L` の指数写像 :math:`\exp(tL)x` を以下で定義する。

.. math::
 \exp(tL)x := \gamma_{x}^{L}(t)

指数写像を用いてPDEを書き直す。
まず、 :math:`\tilde{P}(R_{1}, R_{2}, t) := e^{-rt}P(R_{1}, R_{2}, t)` と置くと次のPDEを得る。

.. math::
 \left( L_{0} + L_{1} - \frac{\partial }{\partial t} \right) \tilde{P}(R_{1}, R_{2}, t) 
 & = 0, \\
 \tilde{P}(R_{1}, R_{2}, 0) 
 & = R_{2} \mathrm{max}(R_{1} - 1, 0).

よって、 :math:`P` は指数写像を用いて次のように書ける。

.. math::
 P(R_{1}, R_{2}, t) = e^{-rt}\exp\left( t(L_{0} + L_{1}) \right)R_{2}\mathrm{max}(R_{1} - 1, 0).

:ref:`Lie-Trotter operator splitting method` によって次のように近似できる。

.. math::
 P^{\mathrm{LT}}(R_{1}, R_{2}, t) = e^{-rt}\exp\left( tL_{0} \right)\exp\left( tL_{1} \right)R_{2}\mathrm{max}(R_{1} - 1, 0).
 
一般に、 初期値 :math:`f(x)` の指数写像 :math:`\exp(tL)f(x)` に対して :math:`Lf(x) = 0` ならば、 :math:`\exp(tL)f(x) = f(x)` が成り立つ。
実際、指数写像の定義より

.. math::
 \frac{\,d\gamma_{f(x)}^{L}(t)}{\,dt} 
 = L\gamma_{f(x)}^{L}(t) 

だから、両辺を :math:`[0, t]` で :math:`t` について積分を繰り返すと、

.. math::
 \gamma_{f(x)}^{L}(t) 
 = f(x) 
 + \sum_{n=1}^{\infty} \frac{t^{n}}{n!}(L)^{n} f(x)

となる。
条件より、無限級数の項はゼロ。
以上より、 :math:`L_{1}R_{2}\mathrm{max}(R_{1} - 1, 0) = 0` だから、

.. math::
 P^{\mathrm{LT}}(R_{1}, R_{2}, t) 
 & = e^{-rt}\exp\left( tL_{0} \right)R_{2}\mathrm{max}(R_{1} - 1, 0) \\
 & = R_{2} e^{-rt}\exp\left( tL_{0} \right)\mathrm{max}(R_{1} - 1, 0)

となる。
:math:`\exp(tL_{0})\mathrm{max}(R_{1} - 1, 0)` を解けば良い。
よって、

.. math::
 P^{\mathrm{LT}}(R_{1}, R_{2}, t) = e^{-rt}R_{2}\left(R_{1} N(\xi_{1}) - N(\xi_{2}) \right) 

ここで、

.. math::
 \xi_{1} 
 & := \frac{1}{\tilde{\sigma}\sqrt{t}} \left( \ln R_{1} + \frac{1}{2} \tilde{\sigma}^{2} \right), \\
 \xi_{2}
 & := \xi_{1} - \tilde{\sigma}\sqrt{t},

であり、 :math:`N(\xi)` は標準正規分布の分布関数である。
現在価値に対する価格式にする為、 :math:`S_{i}(t) := e^{-rt}F_{i}(t)` とおくと、 :ref:`Kirk's approximation` が得られる。

.. math::
 P_{\mathrm{Kirk}}(S_{1}, S_{2}, t) = S_{1} N(d_{1}) - (S_{2} + Ke^{-rt})N(d_{2})

ここで、

.. math::
 d_{1}
 & := \frac{\ln S_{1} - \ln (S_{2} + Ke^{-rt})}{\tilde{\sigma}\sqrt{t}} 
 + \frac{1}{2}\tilde{\sigma}\sqrt{t} \\
 d_{2}
 & := d_{1} - \tilde{\sigma}\sqrt{t} \\
 \tilde{\sigma} 
 & := \sqrt{\sigma_{1}^{2} - 2\rho\sigma_{1}\tilde{\sigma_{2}} + \tilde{\sigma_{2}}^{2}} \\
 \tilde{\sigma_{2}} 
 & := \sigma_{2}\left(\frac{S_{2}}{S_{2} + Ke^{-rt}}\right) \\

Lie-Trotter operator splittingでは :math:`\tilde{\sigma}^{2}t \ll 1` である必要がある。
つまり、以下の状況では精度が悪くなる可能性がある。

* 相関 :math:`\rho` が負
* 相関が正で、 :math:`\sigma_{1}, \tilde{\sigma_{2}}` の値が大きく異なる。

    * 定義へ :eq:`definition_sigma2_tilde`


高次のoperator splittingへの拡張
--------------------------------

Strang operator splitting を用いるとPDEは次のように近似できる。

.. math::
 P^{\mathrm{Strang}}(R_{1}, R_{2}, t)
 & = \exp\left(\frac{1}{2}tL_{1}\right)\exp(tL_{0})\exp\left(\frac{1}{2}tL_{1}\right)R_{2}\mathrm{max}(R_{1} - 1, 0)  \\
 & = \exp\left(\frac{1}{2}tL_{1}\right)P^{\mathrm{LT}}(R_{1}, R_{2}, t) \\
 & = P^{\mathrm{LT}}(R_{1}, R_{2}, t) 
 + \sum_{n=1}^{\infty}\frac{(t/2)^{n}}{n!}(L_{1})^{n} P^{\mathrm{LT}}(R_{1}, R_{2}, t)

:ref:`Kirk's approximation`  :math:`P^{\mathrm{LT}}` に調整が入ったものとみることができる。
無限級数の第一項を解くと

.. math::
 \frac{1}{2}tL_{1}P^{\mathrm{LT}}(R_{1}, R_{2}, t) 
 & = \frac{1}{2}t\tilde{\sigma_{2}}^{2}e^{-rt}R_{2}\Phi(\xi_{2})
     \left(\frac{R_{2}}{\tilde{\sigma}}\frac{\partial\sigma}{\partial R_{2}}\right) \\
         & \left\{ \xi_{2}\left( 1 - \frac{\rho\sigma_{1}}{\tilde{\sigma_{2}}} \right) 
              + \frac{1}{2}\tilde{\sigma}\sqrt{t}
                 \left\{ \xi_{1}\xi_{2} + (1 - \rho^{2})\left( \frac{\sigma_{1}}{\rho\sigma_{1} - \tilde{\sigma_{2}}} \right)^{2} \right\}
                     \left( \frac{R_{2}}{\tilde{\sigma_{2}}}\frac{\partial \tilde{\sigma}}{\partial R_{2}} \right) \right\}.

ここで、

.. math::
 \Phi(x) 
 & := \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{x^{2}}{2}\right) \\
 \frac{R_{2}}{\tilde{\sigma}}
 & = - \frac{(\rho\sigma_{1} - \tilde{\sigma_{2}})\sigma_{2}}{\tilde{\sigma}^{2}}\frac{K}{R_{2}}.

Lie-Trotter operator splitting methodと同様に、 :math:`S_{i}(t) := F_{i}(t)e^{-rt}` とおくと

.. math::
 P(S_{1}, S_{2}, t)
 & \approx P_{\mathrm{Kirk}}(S_{1}, S_{2}, t) \\
 & - \frac{1}{2}t\tilde{\sigma_{2}}^{2}Ke^{-rt}\Phi(d_{2})
     \frac{\rho\sigma_{1} - \tilde{\sigma_{2}}\sigma_{2}}{\tilde{\sigma}^{2}} \\
     & \left( d_{2}\left( 1 - \frac{\rho\sigma_{1}}{\tilde{\sigma_{2}}} \right)
     - \frac{1}{2}\tilde{\sigma}\sqrt{t}
        \left\{ d_{1}d_{2} + (1 - \rho^{2})
            \left(\frac{\sigma_{1}}{\rho\sigma_{1} - \tilde{\sigma_{2}}}\right)^{2} \right\}
        \frac{(\rho\sigma_{1} - \tilde{\sigma_{2}})\sigma_{2}}{\tilde{\sigma}^{2}}
        \frac{Ke^{-rt}}{S_{2} + Ke^{-rt}} \right)

Appendix
--------

European spread optionに対する近似式
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
また :math:`S_{1}, S_{2}` が以下を満たすような確率過程であるとする。
(e.g. log normal process）

.. math::
 S_{1}(t) 
 & = \alpha e^{\beta W_{1}(t) - \beta^{2}/2}, \\
 S_{2}(t)
 & = \gamma e^{\delta W_{2}(t) - \delta^{2}/2}.

ここで、 :math:`W_{1}, W_{2}` は相関のあるブラウン運動で、 :math:`\alpha, \beta, \gamma, \delta` は適当な定数である。
spreadを以下で定義する。

.. math::
 S := S_{1} - S_{2}.

.. index::
    Bachelier's model

Bachelier's Model
"""""""""""""""""
:math:`S` を下記のGaussian distributionで近似する。

.. math::
 S \sim \mathrm{N}(\mathbb{E}(S), \mathbb{V}(S))

期待値と分散は以下で与えられる。

.. math::
 \mathbb{E}(S) = \alpha - \gamma

.. math::
 \mathbb{V}(S) = \alpha^{2}\left(e^{\beta^{2}} - 1\right) - 2\alpha\gamma\left(e^{\rho\beta\delta} - 1\right) + \gamma^{2}\left(e^{\delta^{2}} - 1\right).

このとき、call optionの価値は

.. math::
 p = (\alpha - \gamma - \kappa) \Phi\left(\frac{\alpha - \gamma - \kappa}{\sigma^{B}}\right) 
  + \sigma^{B}\Phi\left(\frac{\alpha - \gamma - \kappa}{\sigma^{B}}\right)

ここで、

.. math::
 \sigma^{B} := \sqrt{\alpha^{2}(e^{\beta^{2}} - 1) - 2\alpha\gamma(e^{\rho\beta\delta} - 1) + \gamma^{2}(e^{\delta^{2}} - 1)}

.. index::
    Kirk's approximation

.. _Kirk's approximation:

Kirk's approximation
""""""""""""""""""""

.. math::
 p = \alpha \Phi \left( \ln \left( \frac{\alpha}{\gamma + \kappa} \right) + \frac{\sigma^{K}}{2} \right)
  - (\gamma + \kappa) \Phi \left( \frac{\ln \left(\frac{\alpha}{\gamma + \kappa} \right)}{\sigma^{K}} - \frac{\sigma^{K}}{2} \right)

ここで

.. math::
 \sigma^{K} := \sqrt{\beta^{2} - 2\rho\beta\rho\frac{\gamma}{\gamma+\kappa} + \delta^{2}\left(\frac{\gamma}{\gamma + \kappa}\right)^{2}}

.. index::
    operator splitting method

Operator splitting method
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _Lie-Trotter operator splitting method:

Lie-Trotter operator splitting method
"""""""""""""""""""""""""""""""""""""

:math:`L_{1}, L_{2}` を微分作用素とし、 :math:`x \in \mathbb{R}^{d}` とする。
指数写像 :math:`\exp\left( t(L_{0} + L_{1}) \right)x` に対して以下が成り立つ。

.. math::
 \exp\left( t(L_{0} + L_{1}) \right) = \exp( tL_{0} ) \exp( tL_{1}) + O(t)

微分作用素 :math:`L` がリー括弧積について可換な時(i.e. :math:`[L_{1}, L_{2}] = [L_{2}, L_{1}]` ) 誤差0で成立する。
operator splittingは、微分作用素の和をについての微分方程式を、 :math:`L_{1}` と :math:`L_{2}` それぞれに関する微分方程式で近似する。
よって、 :math:`L_{1}, L_{2}` に関する微分方程式が解析的に解くことが可能なら、高速に計算可能となる。


高次のoperator spittting method
"""""""""""""""""""""""""""""""

Lie-Trotter operator splittingは2次の近似だが、より高次の近似を構成する方法も知られている。
:math:`A, B` を非可換作用素(今までの :math:`L_{1}, L_{2}` など）とする。
次の近似は [F_Neri_1988]_ [M_Suzuki_1985]_ による。


.. math::
 \exp(t(A + b)) = \exp(\frac{1}{2}tA)\exp(tB)\exp(\frac{1}{2}A) + O(t^{2})

この近似は、Strang operator splittingなどと知られている。


Reference
---------
.. [C_Lo_2014] C.Lo, Pricing Spread Options by the Operator Splitting Method (2014).

.. [H_Yoshida_1990] H.Yoshida, Construction of higher order sympletic integrator (1990)

.. [F_Neri_1988] F.Neri, Lie algebras and canonical integration(1988)

.. [M_Suzuki_1985] M.Suzuki, Decomposition formulas of exponential operators and Lie exponentials with some applications to quantum mechanics and statistical physics.

