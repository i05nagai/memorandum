---
title: doc2vec
---

## doc2vec


## word2vec

$$
    f(g(x; \theta))
$$

#### Continuous Bug Of Words
Step1. Collect all of the words appeard in the training data

Step2. Labeled the words with unique ID

Step3. Train a neural network with 

* $M=3$,
    * the number of layers including the input layer and the output layer
    * in this case, input layer, hidden layer, output layer
* $K$,
    * the number of unique words
    * input dimensions
* $W \in \mathbb{N}$,
    * the size of context window
* $N_{i} \in \mathbb{N}$,
    * the number of unique words
* $$x^{(1)} \in \{0, 1\}^{N}$$,
    * the input vector
* $$y^{(M)} := x^{(M)} \in [0, 1]^{N}$$,
    * the output vector
    * $n$-th dimension represents the probability $n$-th words
* $(x_{i}, y_{i}) \ (i = 1, \ldots, W)$,
    * $x_{i} \in \{0, 1\}^{N}$,
        * input data
    * $y_{i} \in [0, 1]^{N}$,
        * output data
        * $y_{i} = 1$ if $y_{i}$ is apperad between $W$ words before $x_{i}$ and $W$ words after $x_{i}$
        * $y_{i} = 0$ otherwise


Step4. The represented vector of $i$-th is the the output of the trained neural network

<div class="end-of-statement" style="text-align: right">■</div>

#### Skip-Gram
Step1. Collect all of the words appeard in the training data

Step2. Labeled the words with unique ID

Step3. Solve the maximization problem with

* $M=3$,
    * the number of layers including the input layer and the output layer
    * in this case, input layer, hidden layer, output layer
* $K$,
    * the number of unique words
    * input dimensions
* $W \in \mathbb{N}$,
    * the size of context window
* $T \in \mathbb{N}$,
    * the number of context window
* $K^{\prime} \in \mathbb{N}$,
    * the number of words in a document
    * $T = K^{\prime} - W - 1$,
* $w_{1}, \ldots, w_{K^{\prime}}$,
    * the words
* $$A: \{w_{i}\} \rightarrow \{1, \ldots, K\}$$,
    * map to unique words
* $$x^{(1)} \in \{0, 1\}^{N}$$,
    * the input vector
* $$y^{(M)} := x^{(M)} \in [0, 1]^{N}$$,
    * the output vector
    * $n$-th dimension represents the probability $n$-th words
* $(x_{i}, y_{i}) \ (i = 1, \ldots, W)$,
    * $x_{i} \in \{0, 1\}^{N}$,
        * input data
    * $y_{i} \in [0, 1]^{N}$,
        * output data
        * $y_{i} = 1$ if $y_{i}$ is apperad between $W$ words before $x_{i}$ and $W$ words after $x_{i}$
        * $y_{i} = 0$ otherwise

$$
\begin{eqnarray}
    p_{I \mid J}(i \mid j)
    & := &
        \frac{
            \exp
            \left(
                \theta_{i}^{\mathrm{T}}
                \theta_{j}
            \right)
        }{
            \sum_{k=1}^{K}
                \exp
                \left(
                    \theta_{k}^{\mathrm{T}}
                    \theta_{j}
                \right)
        }
    \nonumber
    \\
    & &
        \frac{1}{T}
        \sum_{t=1}^{T}
        \sum_{-W \le l \le W, l \neq 0}
            \log p_{I \mid J}(A(w_{t + l}) \mid A(w_{t}))
    \label{skip_gram_objective_function}
    .
\end{eqnarray}
$$

Step4. The represented vector of $i$-th unique word is the $\theta_{i}$ obtained by maximizing the above equation.

<div class="end-of-statement" style="text-align: right">■</div>

## Reference
* [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
    * paper proposing word2vec algorithm
    * only describing the algorithm from the aspect of the computational complexity
* [Distributed Representations of Sentences and Documents](https://arxiv.org/abs/1405.4053)
    * paper proposing doc2vec algorithm
* [A gentle introduction to Doc2Vec – ScaleAbout – Medium](https://medium.com/scaleabout/a-gentle-introduction-to-doc2vec-db3e8c0cce5e)
* [Word2Vec Tutorial \- The Skip\-Gram Model · Chris McCormick](http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/)
* [Vector Representations of Words  \|  TensorFlow](https://www.tensorflow.org/tutorials/representation/word2vec)
