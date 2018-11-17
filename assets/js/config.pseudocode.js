let pseudocodes = document.getElementsByClassName("pseudocode-js");

for (var i = 0; i < pseudocodes.length; i++) {
  pseudocode.render(pseudocodes[i].nextElementSibling.textContent, pseudocodes[i], {
    indentSize: '1.2em',
    commentDelimiter: ' //',
    lineNumber: true,
    lineNumberPunc: ':',
    noEnd: false,
    captionCount: undefined,
  });
}
