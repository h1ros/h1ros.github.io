Title: Python Style Guide Cheatsheet  
Slug: 
Date: 2018-04-21 12:00
Category: python 
Tags: python, pep8, cheatsheet
Author: h1r03
Summary: Python Style Guide Cheatsheet 







> Readability counts
>
> code is read much more often than it is written



## Code Layout



* **Space** is preferred, rather than tab

* Maximum Line Length: **79 characters** 

* Binary operator: **before a line break**

* import: **seperate lines**

* order of imports: 

  1. standard library imports
  2. third party imports
  3. local application/library specifc imports

* Comments: complete sentences starting with **Capital letter**

  ​

## Namining Convention



* _ prefix: weak internal use. 
* _ suffix: used to avoid conflicts with Python keyword
* __ prefix: strong internal use (harder to access because of name mangling)
* __ prefix & __ suffix: magic objects or attributes. **Never use these names**



Never use: 

* l (lowercase letter el) <-> 1
* O (uppercase letter oh) <-> 0



#### Use Lowercase & seperated by '_': 

* Package and Module Names
* Function and Variable Names
* Method and Instance Variables Names



#### Use CapWords convention:

* Class Names


* Type Variable Names 
* Exception Names 



#### Use ALL CAPITAL: 

* Constants



## Programming Recommendations



* Try/Except clauses: 
  * limit the `try` clause to the absolute minimum amount of code necessary
* Return statement:
  * be consistent what to return i.e., all returns the same expression or none
* Use `''.startswith() `
  * rather than checking for prefixes or suffixes
* Use `isinstance(obj, int)`
  * rather than comparing types by `type(obj)`
* Use the fact that **empty sequences (strings, lists, tuples ) are **`false`
  * `if not seq:` or `if seq:` 
  * rather than `if len(seq):` or `if not len(seq)`



Note that the following sections are ommited since IDE can automatically correct.

Whitespace in Expressions and Statement