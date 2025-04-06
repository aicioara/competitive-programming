// Allow Copy
javascript: document.addEventListener('copy', (event) => event.stopImmediatePropagation(), true);

// Allow Paste
javascript: var allowPaste = function (e) { e.stopImmediatePropagation(); return true; }; document.addEventListener('paste', allowPaste, true);
