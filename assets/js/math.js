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
      },
      Macros: {
        diag: '\\mathop{\\mathrm{diag}}\\nolimits',
        argmax: '\\mathop{\\mathrm{argmax}}\\limits',
        argmin: '\\mathop{\\mathrm{argmin}}\\limits',
        deg: '\\mathrm{deg}',
        norm: ['\\left\\| #1 \\right\\|', 1],
        abs: ['\\left| #1 \\right|', 1],
      } 
    }
  });
})(document, window);
