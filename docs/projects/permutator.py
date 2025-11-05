#TO DO

# - Add instructions
# - Add test cases
# - Strip whitespace
# - Add Error management.
# - Add table headers
# - Consider Nesting

# Import statements
from itertools import product
from re import findall, sub
from pprint import pprint

# Help text for when the "HELP" command is given.
HELP_TEXT = '''
                           TEST PERMUTATOR
---------------------------------------------------------------------
Generates all permutations for a given set of options and conditions.
Use each of the modes to add data, then generate the scenarios.

Use "|" to represent OR statements.
Use "&" to represent AND statements.

All OR statements are evaluated before any AND statements.
As such, DO NOT NEST LOGICAL OPERATIONS.
Instead expand all brackets (E.g. 1(a | (b & c)) ==> 1(a), 1(b & c))


Upon startup enter data via the following prompts:

* SET OPTIONS:
Add all options and their possible states to the database.
Syntax is "option_1(state_1 | state_2), option_2(state_3 | state_4)".
E.g. 1(a|b|c), 2(d|e|f).

* SET CONDITIONS:
Add all requirements and their expected results.
Syntax is "result_1(state_1=requirement_1 | state_2=requirement_2), 
result_2(state_3=requirement_3 | state_4=requirement_4)".
E.g. Dog(1=a|2=e), Cat(2=d), Hamster(1=c&2=e), Lizard(1=b).

* SET FILTERS (Optional): 
Remove select permutations. 
E.g. 1=b&2=f, 1=c.
'''

def format_options(d: dict) -> dict:
    '''Format the options dictionary such that the values are in the "field = state" format.'''
    format_states = lambda field, states : {f'{field}={state}' for state in states}
    return {field: format_states(field, states) for field, states in d.items()}

def get_cartesian_product(d: dict) -> set:
    '''Get the cartesian product across all dictionary values.'''
    return set(product(*d.values()))

def format_product(s: set) -> set:
    '''Format the cartesain product into a dictionary with an empty tuple to store results.'''
    return {frozenset(element): tuple() for element in s}

def apply_conditions(p: dict, c: dict) -> dict:
    '''Assign results to each cartesian product permutation in accordance with the applied OR conditions.'''
    for permutation, condition in product(p.keys(), c.items()):
        result, requirements = condition[0], condition[1]

        # Scan for OR conditions.
        if len(permutation & requirements) > 0:
            p[permutation] += (result,)

        # Scan for AND conditions.
        for requirement in requirements:
            if permutation == requirement:
                p[permutation] += (result,)
    return p

def apply_filters(p: dict, f: set) -> dict:
    '''Remove permutations based on the applied filters.'''
    for permutation, filter in product(p.keys(), f):
        if permutation == filter or permutation & {filter,}:
            p.pop(permutation)
        else:
            continue
    return p

def apply_operations_sequentially(data, operations: dict):
    '''Sequentially apply operations to an initial input.'''
    [data := operation(data, *arguments) for operation, arguments in operations.items()]
    return data

comma_split = lambda s: s.split(',')
strip_element_whitespace = lambda l: [e.strip() for e in l]
OR_element_split = lambda l: [set(e.split('|')) for e in l]
remove_element_parentheses = lambda l: [sub(r"\(.*?\)", "", e) for e in l]
extract_from_element_parentheses = lambda l: [findall(r"\((.*?)\)", e)[0] for e in l]
build_dict = lambda a, b: {x: y for x, y in zip(a, b)}

def AND_element_split(l):
    for e in l:
        if '&' in e:
            l.add(frozenset(e.split('&')))
            l.remove(e)
        else:
            continue

def format_options_command(options: str) -> dict:
    '''Format the options string input into a dictionary.'''
    options = apply_operations_sequentially(options, {
        comma_split: [], 
        strip_element_whitespace: [],
    })
    fields = apply_operations_sequentially(options, {
        remove_element_parentheses: [], 
        strip_element_whitespace: [],
    })
    states = apply_operations_sequentially(options, {
        extract_from_element_parentheses: [], 
        strip_element_whitespace: [], 
        OR_element_split: [],
    })
    return build_dict(fields, states)

def format_conditions_command(conditions: str) -> dict:
    '''Format the conditions string input into a dictionary.'''
    conditions = apply_operations_sequentially(conditions, {
        comma_split: [], 
        strip_element_whitespace: [],
    })
    results = apply_operations_sequentially(conditions, {
        remove_element_parentheses: [], 
        strip_element_whitespace: [],
    })
    requirements = apply_operations_sequentially(conditions, {
        extract_from_element_parentheses: [], 
        strip_element_whitespace: [], 
        OR_element_split: [],
    })
    [AND_element_split(requirement) for requirement in requirements]
    return build_dict(results, requirements)

def format_filters_command(filters: str) -> set:
    '''Format the options string input into a set.'''
    filters = apply_operations_sequentially(filters, {
        comma_split: [], 
        strip_element_whitespace: [],
        set: [],
    })
    AND_element_split(filters)
    return filters

def Permutate() -> None:
    '''Take in user input, apply a sequence of operations.'''
    options, conditions, filters = (
        format_options_command(input('SET OPTIONS: ')),
        format_conditions_command(input('SET CONDTIONS: ')),
        format_filters_command(input('SET FILTERS (Optional): '))
    )

    operations = {
        format_options: [],
        get_cartesian_product: [],
        format_product: [],
        apply_conditions: [conditions,],
        apply_filters: [filters,],
    }

    # Print combinations
    output = apply_operations_sequentially(options, operations)
    #header1, header2 = ['Permutations', '',], ['Results', '',]
    #permutations, results = [
    #    pd.DataFrame(output.keys(), columns=header1), 
    #    pd.DataFrame(output.values(), columns=header2)
    #]
    
    #df3 = pd.concat([permutations, results], axis=1)
    #df3.index = df3.index + 1
    #print(df3)
    pprint(output)

    # Reset variables
    options, conditions, filters = None, None, None

 

Permutate()