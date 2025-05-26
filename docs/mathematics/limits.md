# Limits
A limit is the limiting value that a function approaches.
For example, the limit of ${\frac{1}{x}}$ as $x \rightarrow \infty$ is 0. 

$\lim_{x \to \infty} \frac{1}{x} = 0$

This can be visualised by loking at a graph of ${\frac{1}{x}}$, but in many other cases, it may be harder to discern the limiting value.

Limits are instrumental in finding the derivatives of functions.
For example, conside an object accelerating according to a function S(t), where t is time. 
The distance the object moves in one infinitesimal unit of time is threfore $\frac{S(t_{2}) - S(t_{1})}{t_{2} - t_{1}}$
Consider also that $S(t_{2}) = S(t_{1}+\delta_{t})$ where $\delta_{t}$ the infinitesimal difference between $t_{1}$ and $t_{2}$.
It therefore follows that $\frac{S(t_{1}+\delta_{t}) - S(t_{1})}{\delta_{t}}$, putting the entire function in terms of $t_{1}$.
If $\delta_{t}$ is evaluated as a limit that tends to zero, we obtain the instantaneous speed (i.e. the derivative of the acceleration) at time $t_{1}$ (i.e. at any time we choose):

$\lim_{\delta_{t} \to 0} \frac{S(t_{1}+\delta_{t}) - S(t_{1})}{\delta_{t}}$
