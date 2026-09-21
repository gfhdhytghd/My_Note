# Checklist Before Submission

## Code Readability
- [ ] Function definitions include correct type annotations when required.
- [ ] Each function has a clear docstring describing purpose, arguments, and return value or output.
- [ ] Names are descriptive and follow `snake_case` where required.
- [ ] Avoid unclear abbreviations and single-letter names outside very small scopes.
- [ ] Formatting is consistent:
  4-space indentation, reasonable line length, blank lines between top-level functions, no trailing whitespace.

## Design
- [ ] Break the problem into smaller subproblems when it improves clarity.
- [ ] Use helper functions when the rubric or prompt expects decomposition.
- [ ] Reuse helpers instead of duplicating logic across multiple functions.
- [ ] When one part of the solution is meant to build on another, the relationship is visible in the code instead of being reimplemented separately.
- [ ] Helper functions are called correctly and contribute to the final solution as intended.
- [ ] Keep each function focused on one job.
- [ ] Use simple, appropriate constant representations for fixed labels or categories.
- [ ] Multi-step logic is organized into clear stages when that improves readability and makes the design easier to justify.
- [ ] Avoid unnecessary global state unless the assignment explicitly allows or requires it.

## Spec Matching
- [ ] Required function names match the assignment exactly.
- [ ] Required parameter lists and return types match the assignment exactly.
- [ ] Output format matches the assignment exactly.
- [ ] Small naming details match the prompt exactly, including spelling and capitalization.
- [ ] If the prompt restricts built-ins, modules, or methods, the solution follows those restrictions.

## Correctness And Edge Cases
- [ ] Typical cases work correctly.
- [ ] Boundary cases are considered:
  empty input, single-item input, smallest/largest relevant values, ties, no-match cases.
- [ ] Conditions test the intended value, not the function object or wrong index.
- [ ] Position-sensitive logic checks the intended location or element.
- [ ] Loops and indexing do not have off-by-one errors.
- [ ] Functions return the required value on all control paths.
- [ ] Variable names used inside a function match the actual parameter and local names.
- [ ] Data-cleaning steps preserve the structure the later logic depends on.

## Mutation Vs Return
- [ ] If a function is supposed to mutate input, it changes the original object in place.
- [ ] If a function is supposed to return a new value, it does not silently rely on side effects instead.
- [ ] No unnecessary temporary lists or copies are created when the spec forbids them.

## Testing
- [ ] `main()` or the required driver includes enough tests for each required function(3 tests for each functions, healper function not include).
- [ ] Tests cover normal cases and edge cases.
- [ ] Prefer `assert` when allowed so failures are obvious and repeatable.
- [ ] Test examples reflect the exact assignment behavior, not a guessed variant.

## Submission Hygiene
- [ ] File names match the assignment spec exactly.
- [ ] Header comments, name, collaboration statement, and other required metadata are filled in.
- [ ] No debug prints or leftover placeholders remain.
- [ ] No obviously unused variables, dead code, or incomplete TODOs remain.
- [ ] The file runs from a clean start without manual setup beyond the assignment instructions.
