from cnf import Clause, Literal, Cnf

def assign(model_so_far, symbol, bool_assignment):
    return {**model_so_far, symbol: bool_assignment}


class SearchSolver:
            
    def __call__(self, sent):
        symbols = sent.symbols()
        result = self._search_solver_helper(sent, symbols)
        return result
    
    def _search_solver_helper(self, sent, symbols):                       
        m = sent.implicit_model()
        unassigned_symbols = sorted(symbols - m.keys())
        if len(unassigned_symbols) == 0:
            if sent.check_model(m):
                return m, [m]
            else:
                return None, [m]
        else:
            next_symbol = unassigned_symbols[0]
            negative_unit_clause = Clause([Literal(next_symbol, polarity=False)])
            sent_if_false = Cnf(sent.clauses | { negative_unit_clause })            
            sat_if_false, models_if_false = self._search_solver_helper(sent_if_false, symbols)            
            if sat_if_false != None: # early termination if already satisfied
                return sat_if_false, models_if_false
            positive_unit_clause = Clause([Literal(next_symbol, polarity=True)])
            sent_if_true = Cnf(sent.clauses | { positive_unit_clause })
            sat_if_true, models_if_true = self._search_solver_helper(sent_if_true, symbols) 
            return sat_if_true, models_if_false + models_if_true  
    

search_solver = SearchSolver()

