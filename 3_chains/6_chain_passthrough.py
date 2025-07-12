from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableBranch

conditional_branch = RunnableBranch(
    (
        lambda x: "shout" in x.lower(),
        RunnableLambda(lambda x: x.upper())
    ),
    RunnablePassthrough()
)

print("With 'shout':", conditional_branch.invoke("please shout this out loud"))

print("Without 'shout':", conditional_branch.invoke("just say this normally"))
