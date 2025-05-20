# Probability 

## Definitions 
- Experiment: A test (i.e. a single coin flip).
- Trial: A set of experiments.
- Sample space: A set of all possible outcomes.
- Event: A set of possible outcomes that is a subset of the sample space.
- Cardinality: Number of elements in a set.
- Uniform distribution: Each outcome in the sample space is equally likely to occur.

## Probability of a single event occurring
For a uniform distribution:

$\text{Probability of a specific event} = \frac{\text{Cardinality of the event}}{\text{Cardinality of the set}} \qquad \text{or} \qquad P(E) = \frac{n(E)}{n(S)}$

If $P(E) = 1$, the occurence of event E is certain. If $P(E) = 0$, the occurence of event E is impossible.

## Probabilty of either of two events occuring.
For a uniform distribution, the <ins>union</ins> of the two sets gives this probability.
E.g. Select for numbers that are either prime or odd on a 6-sided die.

$E = (2,3,5) \cup (1,3,5) = (1,2,3,5)$

Thus: $P(E) = \frac{4}{6} = \frac{2}{3}$

## Probability of two events occurring simultaneously.
For a uniform distribution, the <ins>intersection</ins> of the two sets gives this probability.
E.g. Select for numbers thay are both prime and odd on a 6-sided die.

$E = (2,3,5) \cap (1,3,5) = (3,5)$

Thus: $P(E) = \frac{2}{6} = \frac{1}{3}$

## Expectation Values
- Discrete random variable: A randomly sampled event that only takes integral values (e.g a die roll).
- Continuous random variable: A randomply sampled event that can take any real value.
- Expectation value:
$$E = (\text{value 1})(\text{probability of value 1})+...+(\text{value n})(\text{probability of value n} = x_{1}P(x_{1})+x_{2}P(x_{2})+...+x_{n}P(x_{n})$$
- Law of large numbers: Principle that the average result of random sampling converges to the expectation value as more samples are taken.
