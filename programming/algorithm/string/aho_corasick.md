---
title: Aho Corasick
---

## Aho Corasick


```mermaid
graph TD;
    root(root);
    i(i);
    in(in);
    t(t);
    ti(ti);
    tin(tin);
    s(s);
    st(st);
    sti(sti);
    stin(stin);
    sting(sting);
    style i fill:#ADFF2F
    style in fill:#ADFF2F
    style tin fill:#ADFF2F
    style sting fill:#ADFF2F
    subgraph A
        i;
        in;
    end
    subgraph B
        t;
        ti;
        tin;
    end
    subgraph C
        s;
        st;
        sti;
        stin;
        sting;
    end
    root-->i;
    root-->t;
    root-->s;
    i-->in;
    t-->ti;
    ti-->tin;
    s-->st;
    st-->sti;
    sti-->stin;
    stin-->sting;

    ti-.->i;
    tin-.->in;
    st-.->t;
    sti-.->ti;
    stin-.->tin;
```

## Reference
- https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
- https://cp-algorithms.com/string/aho_corasick.html
- http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Slides02.pdf
