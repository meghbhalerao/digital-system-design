import logicmin
# truth table 3 inputs, 2 outputs
t = logicmin.TT(4,3);
# add rows to the truth table (input, ouutput)
# ci a b  |  s co
t.add("0000","")
t.add("0001","")
t.add("0010","")
t.add("0011","")
t.add("0100","")
t.add("0101","")
t.add("0110","")
t.add("0111","")
t.add("1000","")
t.add("1001","")
t.add("1010","")
t.add("1011","")
t.add("1100","")
t.add("1101","")
t.add("1110","")
t.add("1111","")

# minimize functions and get
# solution for analysis and print
sols = t.solve()
# print solution mapped to var names (xnames=inputs, ynames=outputs)
# add debug information
print(sols.printN(xnames=['Ci','a','b'],ynames=['s','Co'], info=True))