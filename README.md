# TSLang-Compiler
a compiler written in python for an imaginary language named TSLang \n
this is the bnf of TSLang :

prog ::= func |func prog
func ::= function iden ( flist ) returns type : body end |
body ::= stmt | stmt body
stmt ::= expr ; |
         defvar ; |
         if ( expr ) stmt |
         if ( expr ) stmt else stmt |
         while ( expr ) do stmt |
foreach ( iden of expr ) stmt |
return expr ; |
: body end
defvar ::= val type iden
expr ::= iden ( clist ) |
expr [ expr ] |
expr ? expr : expr |
expr = expr |
expr + expr |
expr - expr |
expr * expr |
expr / expr |
expr % expr |
expr < expr |
expr > expr |
expr == expr |
expr != expr |
expr <= expr |
expr >= expr |
expr || expr |
expr && expr |
! expr |
- expr |
+ expr |
( expr ) |
iden |
num
flist ::= |
type iden |
type iden , flist
clist ::= |
expr |
expr , clist
type ::= Int |
Array |
Nil
num ::= [0-9]+
iden ::= [a-zA-Z_][a-zA-Z_0-9]*
