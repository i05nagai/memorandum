'use strict';

(function(_doc, _win) {
  window.MathJax = {
    loader: {
      load: ['[tex]/ams']
    },
    tex: {
      packages: {'[+]': ['base', 'ams']},
      // kramdown convert $a$ -> \\(\\). \\( is required to use kramdown
      // However, kramdown doesn't convert all of $ to \\(. 
      // having $ in inlineMath allows us to convert the leftovers to math
      inlineMath: [['$', '$'], ['\\(', '\\)']], 
      processEscapes: false, // use \$ to produce a literal dollar sign
      processEnvironments: true, // process \begin{xxx}...\end{xxx} outside math mode
      processRefs: true,
      tags: 'ams',
      macros: {
        diag: '\\mathop{\\mathrm{diag}}\\nolimits',
        argmax: '\\mathop{\\mathrm{argmax}}\\limits',
        argmin: '\\mathop{\\mathrm{argmin}}\\limits',
        deg: '\\mathrm{deg}',
        norm: ['\\left\\| #1 \\right\\|', 1],
        abs: ['\\left| #1 \\right|', 1],
      },
    },
  };
})(document, window);
