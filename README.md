HW: Sudoku 8
------------

All right, so we're sorta going back to the drawing board and creating a
SAT solver based on the search strategy discussed in class. Let's all resolve
to make this approach work! 

1. We're going to represent partial models as a dictionary. Specifically,
   a model that assigns 1 to symbol A, and 0 to symbol B should be represented
   as the following dictionary:
   
       {'A': True, 'B': False}
       
   In this dictionary, use the Boolean value ```True``` for 1 and
   the Boolean value ```False``` for 0.
   
   Now, in ```search.py``` create an immutable function called ```assign```
   that takes a partial model (represented as a dictionary), a symbol,
   and a polarity. It should create a new partial model that extends the previous
   model with the specified assignment. For instance:
   
       assign({'A': True, 'B': False}, 'C', True)
       
   should return the new partial model:
   
       {'A': True, 'B': False, 'C': True}
       
   and should not change the original dictionary. Once you have a successful
   implementation, the following unit tests should succeed:
   
       python -m unittest test_part8.TestModelAssignment

2. Add a method ```.implicit_model()``` to ```cnf.Cnf``` that returns
   a partial model based on the unit clauses (i.e. clauses with a single
   literal) in the Cnf sentence. For instance:
   
       from cnf import sentence
       sent = sentence('\n'.join(['a || b', '!a || b', 'c', '!d']))
       sent.implicit_model()
       
   should return the partial model:
   
       {'c': True, 'd': False}
       
   Note that this method should not perform any resolution; it should
   simply harvest the existing unit clauses and turn them into assignments.
    
   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part8.TestImplicitModel

3. Add a method ```.check_model(model)``` to ```cnf.Cnf``` that takes a
   model (represented as a dictionary, described above) and returns
   whether it satisfies the logical sentence. For instance, if we have
   the following CNF sentence:
   
       sent = sentence('\n'.join(['a || b', '!a || !b'])
       
   Then the following two calls should return ```False```:
   
       sent.check_model({'a': False, 'b': False})
       sent.check_model({'a': True, 'b': True})
       
   But the following two calls should return ```True```:
   
       sent.check_model({'a': False, 'b': True})
       sent.check_model({'a': True, 'b': False})
       
   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part8.TestCheckModel
       
4. Finally, create a function called ```search_solver``` in ```search.py```
   that takes a ```Cnf``` instance (i.e. a CNF sentence) and returns two
   outputs:
   - The first output is a satisfying model, represented as a dictionary
     (if the sentence is satisfiable), or ```None``` (if the sentence is
     unsatisfiable).
   - The second output is a list of (complete) models that were visited
     during the search.
     
   For instance, if we have the following CNF sentence:
   
       sent = sentence('\n'.join(['a || b', '!a || !b'])
       
   Then the call:
   
       satisfying_model, visited_models = search_solver(sent)
       
   should return the satisfying model ```{'a': False, 'b': True}```
   and a list of visited models 
   ```[{'a': False, 'b': False}, {'a': False, 'b': True}]```.
     
   Make sure to obey the following conventions:
   - Once a satisfying model is found, then no further models should be visited.
   - The negative polarity of a symbol should be explored before the positive
     polarity.
   - Symbols should be assigned in alphabetical order.
   
   **HINT**: Consider using the ```.implicit_model``` method to simplify
   the task of finding the next variable to assign.
   
   Once you have a successful implementation, the following unit tests should
   succeed:
   
       python -m unittest test_part8.TestSearchSolver
       
       
   
   
   