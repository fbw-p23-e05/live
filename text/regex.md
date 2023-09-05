# Regular Expressions

- What Regex is?
- Metacharacters 
- re module
- methods in the re module.

A regular Expression (RegEx) is a sequence of characters that defines a search pattern.

```
# matches any five letter string start with a and ending with s
^a...s$
```


## Metacharacters

### [] - Square brackets - specifies a set of characters that you wish to match

| Expression | String | Result |
|------------|--------|--------|
| [abc] | `a` | 1 match |
| [abc] | `ac` | 2 matches |
| [abc] | `Hey Rida` | 1 match |
| [abc] | `abc de ca` | 5 matches |

> [abc] will match if th string you are trying to search against contains any of the letters a, b or c.
> You can also specify a range of characters using `-` inside the square brackets.
- [a-e] - [abcde]
- [1-4] - [1234]
- [0-9] - [0123456789]

> You can invert the character set by using `^` at the start of the square bracket.
- [^abc] means any character except a, b and c
- [^0-9] means any non-digit character. 

### . - Period - matches any single character (except newline '\n').

| Expression | String | Result |
|------------|--------|--------|
| .. | `a` | 0 matches |
| .. | `ac` | 1 match |
| .. | `abc` | 1 match |
| .. | `abc de ce` | 3 matches |
| ... | `abcd` | 1 matches |

### ^ - Caret - is used to to check if a string starts with a certain character.

| Expression | String | Result |
|------------|--------|--------|
| ^a | `a` | 1 match |
| ^a | `abc` | 1 match |
| ^a | `bac` | 0 matches |
| ^ab | `abc` | 1 match |
| ^ab | `abyss` | 1 match |
| ^ab | `agent` | No match (start with a but is not followed by b) |

### $ - Dollar - is used to check if a string **ends with** a certain character

| Expression | String | Result |
|------------|--------|--------|
| s$ | `a` | No match |
| s$ | `abyss` | 1 match |
| a$ | `formula` | 1 match |
| a$ | `taxi` | No match  |

### + - Plus - matches one or more occurrences of the pattern left of it.

| Expression | String | Result |
|------------|--------|--------|
| ta+n | `tan` | 1 match |
| ta+n | `taxation` | No match |
| ta+n | `taaaan` | 1 match |
| ta+ | `tatan` | 2 matches |

### ? - Question Mark - matches zero or one occurrences of the pattern to the left of it.

| Expression | String | Result |
|------------|--------|--------|
| ma?n | `mn` | 1 match |
| ma?n | `man` | 1 match |
| ma?n | `maaaan` | No match | 





 



