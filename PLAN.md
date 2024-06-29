1. REPL (query user for text, they click enter, it runs on that text)
2. Parse it into actual python stuff (from strings)
3. Turn that stuff into expressino trees
ex: 2 + 3*5 =
    +
   / \\
  2    *
      / \\
     3    5

     sin
     /
    2

4. If enter a function, then it will open a window, and evaluate all the values in the window size (step=1/resolution). f(0), f(0.0001) f(0.0002) ... <- draw