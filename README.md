# Recipes

Repository for cooking recipes.

## Format

The suggested format for most recipes is the following markdown template:

```
# Ingredients

## Sub-recipe 1
- ingredient 1, quantity, state
- ingredient 2, quantity, state
- ...

## Sub-recipe 2
- ingredient 1, quantity, state
- ingredient 2, quantity, state
- ...
- (opt) optionnal ingredient 3, quantity, state

# Preparation

# Sub-recipe 1
- step 1
- step 2
	(comment on step 2, in parenthesis, indented by a single tab)
  
## Sub-recipe 2
- step 1
- ...

## Assembly
- step 1
- ...

# Notes
- note 1 about the recipe

```

The ingredients section is straight forward: it is a list of ingredients for a
subset of the recipe (e.g. making the sauce in lasagna). The quantity should
be metric. If the original recipe is in imperial, please add the converted
quantities in metric in parenthesis. The `state` of an ingredient is how the
ingredient should be prepared for the *mise-en-place* (e.g. chopped, sliced,
etc).

As a general rule for readability in a standard 80x24 terminal, lines should not
exceed 80 characters. 

Whenever possible, sub-recipes should be written in a separate document and
included in the parent recipe document, to avoid repetition.

