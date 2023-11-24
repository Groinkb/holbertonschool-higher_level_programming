Overview
You can use this set of guidelines, fork them or make your own - the key here is that you pick a style and stick to it. To suggest changes or fix bugs please open an issue or pull request on GitHub.

These guidelines are designed to be compatible with Joe Celko’s SQL Programming Style book to make adoption for teams who have already read that book easier. This guide is a little more opinionated in some areas and in others a little more relaxed. It is certainly more succinct where Celko’s book contains anecdotes and reasoning behind each rule as thoughtful prose.

It is easy to include this guide in Markdown format as a part of a project’s code base or reference it here for anyone on the project to freely read—much harder with a physical book.

SQL style guide by Simon Holywell is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. Based on a work at https://www.sqlstyle.guide/.

General
Do
Use consistent and descriptive identifiers and names.
Make judicious use of white space and indentation to make code easier to read.
Store ISO 8601 compliant time and date information (YYYY-MM-DD HH:MM:SS.SSSSS).
Try to only use standard SQL functions instead of vendor-specific functions for reasons of portability.
Keep code succinct and devoid of redundant SQL—such as unnecessary quoting or parentheses or WHERE clauses that can otherwise be derived.
Include comments in SQL code where necessary. Use the C style opening /* and closing */ where possible otherwise precede comments with -- and finish them with a new line.
SELECT file_hash  -- stored ssdeep hash
  FROM file_system
 WHERE file_name = '.vimrc';
/* Updating the file record after writing to the file */
UPDATE file_system
   SET file_modified_date = '1980-02-22 13:19:01.00000',
       file_size = 209732
 WHERE file_name = '.vimrc';
Avoid
CamelCase—it is difficult to scan quickly.
Descriptive prefixes or Hungarian notation such as sp_ or tbl.
Plurals—use the more natural collective term where possible instead. For example staff instead of employees or people instead of individuals.
Quoted identifiers—if you must use them then stick to SQL-92 double quotes for portability (you may need to configure your SQL server to support this depending on vendor).
Object-oriented design principles should not be applied to SQL or database structures.
Naming conventions
General
Ensure the name is unique and does not exist as a reserved keyword.
Keep the length to a maximum of 30 bytes—in practice this is 30 characters unless you are using a multi-byte character set.
Names must begin with a letter and may not end with an underscore.
Only use letters, numbers and underscores in names.
Avoid the use of multiple consecutive underscores—these can be hard to read.
Use underscores where you would naturally include a space in the name (first name becomes first_name).
Avoid abbreviations and if you have to use them make sure they are commonly understood.
SELECT first_name
  FROM staff;
Tables
Use a collective name or, less ideally, a plural form. For example (in order of preference) staff and employees.
Do not prefix with tbl or any other such descriptive prefix or Hungarian notation.
Never give a table the same name as one of its columns and vice versa.
Avoid, where possible, concatenating two table names together to create the name of a relationship table. Rather than cars_mechanics prefer services.
Columns
Always use the singular name.
Where possible avoid simply using id as the primary identifier for the table.
Do not add a column with the same name as its table and vice versa.
Always use lowercase except where it may make sense not to such as proper nouns.
Aliasing or correlations
Should relate in some way to the object or expression they are aliasing.
As a rule of thumb the correlation name should be the first letter of each word in the object’s name.
If there is already a correlation with the same name then append a number.
Always include the AS keyword—makes it easier to read as it is explicit.
For computed data (SUM() or AVG()) use the name you would give it were it a column defined in the schema.
SELECT first_name AS fn
  FROM staff AS s1
  JOIN students AS s2
    ON s2.mentor_id = s1.staff_num;
SELECT SUM(s.monitor_tally) AS monitor_total
  FROM staff AS s;
Stored procedures
The name must contain a verb.
Do not prefix with sp_ or any other such descriptive prefix or Hungarian notation.
Uniform suffixes
The following suffixes have a universal meaning ensuring the columns can be read and understood easily from SQL code. Use the correct suffix where appropriate.

_id—a unique identifier such as a column that is a primary key.
_status—flag value or some other status of any type such as publication_status.
_total—the total or sum of a collection of values.
_num—denotes the field contains any kind of number.
_name—signifies a name such as first_name.
_seq—contains a contiguous sequence of values.
_date—denotes a column that contains the date of something.
_tally—a count.
_size—the size of something such as a file size or clothing.
_addr—an address for the record could be physical or intangible such as ip_addr.
Query syntax
Reserved words
Always use uppercase for the reserved keywords like SELECT and WHERE.

It is best to avoid the abbreviated keywords and use the full length ones where available (prefer ABSOLUTE to ABS).

Do not use database server specific keywords where an ANSI SQL keyword already exists performing the same function. This helps to make the code more portable.

SELECT model_num
  FROM phones AS p
 WHERE p.release_date > '2014-09-30';
White space
To make the code easier to read it is important that the correct complement of spacing is used. Do not crowd code or remove natural language spaces.

Spaces
Spaces should be used to line up the code so that the root keywords all end on the same character boundary. This forms a river down the middle making it easy for the readers eye to scan over the code and separate the keywords from the implementation detail. Rivers are bad in typography, but helpful here.

(SELECT f.species_name,
        AVG(f.height) AS average_height, AVG(f.diameter) AS average_diameter
   FROM flora AS f
  WHERE f.species_name = 'Banksia'
     OR f.species_name = 'Sheoak'
     OR f.species_name = 'Wattle'
  GROUP BY f.species_name, f.observation_date)

  UNION ALL

(SELECT b.species_name,
        AVG(b.height) AS average_height, AVG(b.diameter) AS average_diameter
   FROM botanic_garden_flora AS b
  WHERE b.species_name = 'Banksia'
     OR b.species_name = 'Sheoak'
     OR b.species_name = 'Wattle'
  GROUP BY b.species_name, b.observation_date);
