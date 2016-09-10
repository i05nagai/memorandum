'use strict';

(function(_doc, _win) {
  MathJax.Hub.Config({ 
    tex2jax: { 
        inlineMath: [['$','$']],
        displayMath: [['$$', '$$']],
    },
    TeX: { 
      equationNumbers: { 
        autoNumber: "AMS",
        formatNumber: function (n) {
          return n;
        }
      } 
    }
  });
})(document, window);
