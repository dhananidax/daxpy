

class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(rows):
    info,question=find_best_split(rows)
    if info==0:return Leaf(rows)
    true_rows,false_rows=partition(rows,question)
    true_branch=build_tree(true_rows)
    false_branch=build_tree(false_rows)
    return Decision_Node(question,true_branch,false_branch)