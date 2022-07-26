print("let's practice everything")
print('you \'d need to know \'bout escape with \\that do:')
print("\nnew lines and \t tabs ")
poem="""
\t A dog wandered into our garden one day,\n\t
A friendly old mutt, didn't look like a stray.\n\t
We never discovered whence he had come,\n\t
But we brushed him and fed him and the kids called him Rum.
"""
print("-----------------------------------------------------")
print(poem)
print("")
writer="Peter R Wolveridge "
print(f"the poem was written by {writer}")
def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
start_point=10000
jelly_beans,jars,crates=secret_formula(start_point)
print("with a starting point of{start_point}")
print(f"we have {jelly_beans} jelly beans ,{jars} jars,{crates} crates")
start_point=start_point/10

