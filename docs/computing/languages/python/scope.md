# Local and Global variables
- A variable outside of any functions is within the <ins>global</ins> scope.
- A variable inside a function is within the <ins>local</ins> scope of that function.
- There is only one global scope. Each function has its own local scope.
- The global scope is created and destroyed upon program initiation and completion.
- Each local scope is created and destroyed upon its function's initiation and completion.
- The global scope <ins>cannot</ins> access local variables.
- The local scope <ins>can</ins> access global variables.
- Different local scopes do not share variables.
- Consequently, the same variable names can be used in different scopes. However, this is not recommended.
- The ```global``` statement can be used to change the value of a global variable from within a function. However, this is not recommended.
#### [Back](README.md)
