
from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable
from problog.engine import DefaultEngine

rules=PrologString("""
edge(X, Y) :- arc(X, Y) ; arc(Y, X).

reachable(X, Y) :- reachableHelper(X, Y, [X]).

reachableHelper(X, Y, Seen) :-
	edge(X, Y),
	\+ member(Y, Seen).
reachableHelper(X, Y, Seen) :-
	edge(X, Z),
	\+ member(Z, Seen),
	reachableHelper(Z, Y, [Z | Seen]).	

member(X,[X|_]).
member(X,[_|T]) :- member(X,T).
query(reachable(n1, n5)).
""")

evidence=PrologString("""
0.5::arc(n1, n2).
arc(n2, n3).
0.9::arc(n1, n3).
arc(n3, n4).
arc(n4, n5)."""
)

db = DefaultEngine().prepare(rules)
# print (get_evaluatable().create_from(db).evaluate())

for statement in evidence:
	db += statement

print (get_evaluatable().create_from(db).evaluate())

