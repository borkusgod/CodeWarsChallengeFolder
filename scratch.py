# n0v4s3c — Today at 7:01 PM
# In c++ you would pass the argument by reference to modify to the original array.
# In python, I think you use [:] so in your function do this
# wealth[:] = modifiedList
# Where modifiedList is your modified list.
#
# n0v4s3c — Today at 7:12 PM
# /run python


def redistribute(wealth):
    wealth[:] = [sum(wealth)/len(wealth) for i in range(len(wealth))]


list = [5, 6, 10]
redistribute(list)
print(list)


