from afd import AFD

afd1 = AFD(Q={0, 1, 2},
           Sigma={"a", "b"},
           Delta={(0, "a"):  1,
                  (0, "b"): -1,
                  (1, "a"):  1,
                  (2, "a"): -1,
                  (2, "b"):  2},
           q0=0,
           F={1, 2})
