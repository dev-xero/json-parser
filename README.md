# JSON Parser

A parser for the JSON file format specified [here](https://www.json.org/json-en.html) written in Python.

## Grammar (CFG)

Context-free Grammar draft the recursive descent parser follows.

```md
object ::= '{' members '}'
members ::= pair(',' pair)*
pair ::= string ':' value
value ::= string | number | object | boolean | null
```

## Currently Recognized Tokens

1. Left and right braces.
2. Commas.
3. Colons.
4. Strings.
5. Numbers.
6. Booleans.
7. Null.
8. Nested objects.
