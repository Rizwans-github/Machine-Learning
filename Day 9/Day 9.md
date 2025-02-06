<img height="200" src="https://github.com/user-attachments/assets/f27f2efd-0ba9-4f4f-a33d-1eef7397f994">

##### Nominal Data
Nominal data is a type of data that consists of categories and can't be
ordered or ranked. It is also called Nominal data and can't be
ranked or measured in any way. Still, nominal data can be both
qualitative and quantitative at times. Some examples of nominal data are symbols, words, letters, and the
gender of a person, state and your engineering branch.

##### Ordinal Data
Ordinal data is a category of data that has a natural order. It is often used
in surveys, questionnaires, and the fields of finance and economics.
Ordinal data stands out since it is impossible to differentiate between
data values.
Clothing sizes are one example of this type of data (small, medium, and
large are not measurable differences, but they are clearly ordered to
show size comparisons). Exam Grade or Division.

### What is Encoding
Data encoding involves converting a sequence of text characters into
binary code so computers, which operate using binary numbers, can
process, store, or transmit that textual information. Decoding occurs
when the information is then translated from binary form into a readable
version.

#### "Ordinal Encoding"
When we have a feature where variables have some order/rank.
<br></br>
<img height="100" src="https://github.com/user-attachments/assets/942406df-5b23-41b6-8e31-7907d15ffc91">

#### "Nominal Encoding"
When we have a feature where variables are just names and there is no
order or rank to this variable's feature.
<br></br>
<img height="100" src="https://github.com/user-attachments/assets/97e99718-4f10-4beb-8556-18a685e5a7c4">

#### Why is ordinal encoding referred as a Label Encoding?

Ordinal encoding is a technique that is used to transform categorical
variables into a numerical format by assigning a unique value to each of
its categories. It is also referred to as Label Encoding.
For example, we have customer feedback data based on a survey or
online feedback mechanism. It contains categories of very dissatisfied,
dissatisfied, neutral, satisfied, and very satisfied. To encode this variable
using ordinal encoding, we can assign numerical values as mentioned
below —
- very dissatisfied - 1
- dissatisfied - 2
- neutral - 3
- satisfied - 4
- very satisfied — 5

Ordinal encoding assumes that categories in categorical variables have
clear, natural, and intrinsic ordering to their categories. It does not work
for nominal categorical variables as no relationship exists between
categories of a nominal variable. In our previous example, we encoded
the categorical variable by assigning the lowest numerical value of 1 to
the very dissatisfied category and the highest value of 5 to the very
satisfied category.
This way, we were able to preserve the natural ordering of the categories - very dissatisfied < dissatisfied < neutral < satisfied < very satisfied was
retained in 1 < 2 < 3 < 4 < 5. Suppose we have another categorical
variable, which contains red, blue, and green categories. We can encode
this variable using ordinal encoding by assigning I to red, 2 to blue, and 3
to green, but it may lead to incorrect results. As encoded values have a
natural ordering between them - I < 2 < 3 will be there, but red < blue <
green does not exist.
