# Pyramids: English

This package provides the English grammar configuration for the 
[Pyramids parser](https://github.com/hosford42/pyramids).

# Usage:

Code:
```python
import time
from pyramids.categorization import Category
from pyramids_english.plugin import LANGUAGE

timeout = 5  # maximum time, in seconds
text = "This is a test."

(forests, emergency_disambiguation, parse_timed_out, disambiguation_timed_out) = \
        LANGUAGE.parse(text, timeout=time.time() + timeout)

for index, forest in enumerate(forests):
    forest = forest.restrict(Category('sentence'))
    if forest.has_gaps():
        # Gaps indicate that the input could not be fully parsed.
        break
    if forest.is_ambiguous():
        forest = forest.disambiguate()
    print("Interpretation #%s" % (index + 1))
    for graph in forest.get_parse_graphs(forest):
        print(graph)
        print()
    print()
```

Output:
```text
sentence(aux,be,be_form,categorized,complete,cop,decorated,definite,finished_predicate,finished_verb,forward,grouped,has_object,has_subject,known_ending,present,singular,statement,takes_agent,takes_cause,takes_degree,takes_place,takes_purpose,takes_selection,takes_style,takes_time,terminated,third):
  This:
  *is:
    SUBJECT: This
    OBJECT: test
    DELIMITER: .
  a:
  test:
    SELECTOR: a
  .:
```
