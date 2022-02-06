
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDANDNOTORORLESS_EQUALGREATER_EQUALNOT_EQUALEQUALEQUALLESS_THANGREATER_THANleftEQUALQUESTIONMARKCOLONleftPLUSMINUSleftTIMESDIVIDEMODleftLPARENRPARENLSQUAREBRRSQUAREBRANDAND ARRAY COLON COMA COMMENT DIVIDE DO ELSE END EQUAL EQUALEQUAL FOREACH FUNCTION GREATER_EQUAL GREATER_THAN IDEN IF INT LESS_EQUAL LESS_THAN LPAREN LSQUAREBR MINUS MOD NIL NOT NOT_EQUAL NUMBER OF OROR PLUS QUESTIONMARK RETURN RETURNS RPAREN RSQUAREBR SEMICOLON TIMES VAL WHILEprog : func\n            | func progfunc : FUNCTION iden LPAREN flist RPAREN RETURNS type COLON body ENDbody : stmt\n            | stmt bodystmt : expr SEMICOLON\n            | defvar SEMICOLON\n            | IF LPAREN expr RPAREN COLON stmt END\n            | IF LPAREN expr RPAREN COLON stmt ELSE COLON stmt END\n            | WHILE LPAREN expr RPAREN DO stmt\n            | FOREACH LPAREN iden OF expr RPAREN stmt\n            | RETURN expr SEMICOLON\n            | COLON body ENDdefvar : VAL type idenexpr : iden LPAREN clist RPAREN  \n            | expr LSQUAREBR expr RSQUAREBR\n            | expr QUESTIONMARK expr COLON expr\n            | expr EQUAL expr\n            | expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr MOD expr\n            | expr LESS_THAN expr\n            | expr GREATER_THAN expr\n            | expr EQUALEQUAL expr\n            | expr NOT_EQUAL expr\n            | expr LESS_EQUAL expr\n            | expr GREATER_EQUAL expr\n            | expr OROR expr\n            | expr ANDAND expr\n            | NOT expr\n            | MINUS expr\n            | PLUS expr\n            | LPAREN expr RPAREN\n            | iden\n            | numberflist :\n            | type iden\n            | type iden COMA flistclist :\n            | expr\n            | expr COMA clisttype : INT\n            | ARRAY\n            | NILiden : IDENnumber : NUMBER'
    
_lr_action_items = {'FUNCTION':([0,2,40,],[3,3,-3,]),'$end':([1,2,4,40,],[0,-1,-2,-3,]),'IDEN':([3,9,10,11,12,19,21,22,24,30,31,32,33,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,71,91,94,96,99,102,103,106,107,108,110,111,113,],[6,6,-44,-45,-46,6,6,6,6,6,6,6,6,6,-6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-7,6,6,6,6,-13,-12,6,6,6,6,6,-10,6,-8,-11,6,-9,]),'LPAREN':([5,6,19,20,21,22,24,27,28,29,30,31,32,33,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,71,91,94,96,99,102,103,106,107,108,110,111,113,],[7,-47,21,37,21,21,21,60,61,62,21,21,21,21,21,-6,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-7,21,21,-13,-12,21,21,21,21,21,-10,21,-8,-11,21,-9,]),'COMA':([6,14,20,34,36,64,65,66,69,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,93,95,101,],[-47,16,-36,-37,-48,-34,-33,-32,94,-35,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-15,-16,-17,]),'RPAREN':([6,7,8,14,16,18,20,34,36,37,38,64,65,66,68,69,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,94,95,100,101,104,],[-47,-38,13,-39,-38,-40,-36,-37,-48,-41,70,-34,-33,-32,93,-42,-35,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,97,98,-15,-41,-16,-43,-17,107,]),'SEMICOLON':([6,20,25,26,34,36,63,64,65,66,70,74,75,76,77,78,79,80,81,82,83,84,85,86,87,92,93,95,101,],[-47,-36,42,59,-37,-48,91,-34,-33,-32,-35,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-14,-15,-16,-17,]),'LSQUAREBR':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,43,-37,-48,43,43,43,43,43,43,-35,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-15,-16,43,43,]),'QUESTIONMARK':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,44,-37,-48,44,44,-34,-33,44,44,-35,44,44,-18,-19,-20,-21,-22,-23,44,44,44,44,44,44,44,44,44,44,-15,-16,-17,44,]),'EQUAL':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,45,-37,-48,45,45,-34,-33,45,45,-35,45,45,-18,-19,-20,-21,-22,-23,45,45,45,45,45,45,45,45,45,45,-15,-16,-17,45,]),'PLUS':([6,19,20,21,22,24,25,30,31,32,33,34,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,99,101,102,103,104,106,107,108,110,111,113,],[-47,31,-36,31,31,31,46,31,31,31,31,-37,-48,31,46,-6,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-7,31,31,46,-34,-33,46,46,-35,-13,46,46,46,-19,-20,-21,-22,-23,46,46,46,46,46,46,46,46,46,46,-12,-15,31,-16,31,31,46,31,31,46,-10,31,-8,-11,31,-9,]),'MINUS':([6,19,20,21,22,24,25,30,31,32,33,34,36,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,66,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,93,94,95,96,99,101,102,103,104,106,107,108,110,111,113,],[-47,32,-36,32,32,32,47,32,32,32,32,-37,-48,32,47,-6,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-7,32,32,47,-34,-33,47,47,-35,-13,47,47,47,-19,-20,-21,-22,-23,47,47,47,47,47,47,47,47,47,47,-12,-15,32,-16,32,32,47,32,32,47,-10,32,-8,-11,32,-9,]),'TIMES':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,48,-37,-48,48,48,48,48,48,48,-35,48,48,48,48,48,-21,-22,-23,48,48,48,48,48,48,48,48,48,48,-15,-16,48,48,]),'DIVIDE':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,49,-37,-48,49,49,49,49,49,49,-35,49,49,49,49,49,-21,-22,-23,49,49,49,49,49,49,49,49,49,49,-15,-16,49,49,]),'MOD':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,50,-37,-48,50,50,50,50,50,50,-35,50,50,50,50,50,-21,-22,-23,50,50,50,50,50,50,50,50,50,50,-15,-16,50,50,]),'LESS_THAN':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,51,-37,-48,51,51,-34,-33,-32,51,-35,51,51,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,51,51,-15,-16,-17,51,]),'GREATER_THAN':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,52,-37,-48,52,52,-34,-33,-32,52,-35,52,52,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,52,52,-15,-16,-17,52,]),'EQUALEQUAL':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,53,-37,-48,53,53,-34,-33,-32,53,-35,53,53,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,53,53,-15,-16,-17,53,]),'NOT_EQUAL':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,54,-37,-48,54,54,-34,-33,-32,54,-35,54,54,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,54,54,-15,-16,-17,54,]),'LESS_EQUAL':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,55,-37,-48,55,55,-34,-33,-32,55,-35,55,55,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,55,55,-15,-16,-17,55,]),'GREATER_EQUAL':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,56,-37,-48,56,56,-34,-33,-32,56,-35,56,56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,56,56,-15,-16,-17,56,]),'OROR':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,57,-37,-48,57,57,-34,-33,-32,57,-35,57,57,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,57,57,-15,-16,-17,57,]),'ANDAND':([6,20,25,34,36,38,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,101,104,],[-47,-36,58,-37,-48,58,58,-34,-33,-32,58,-35,58,58,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,58,58,-15,-16,-17,58,]),'RSQUAREBR':([6,20,34,36,64,65,66,70,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,93,95,101,],[-47,-36,-37,-48,-34,-33,-32,-35,95,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-15,-16,-17,]),'COLON':([6,10,11,12,17,19,20,22,24,34,36,42,59,64,65,66,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,93,95,97,101,102,103,106,107,108,109,110,111,113,],[-47,-44,-45,-46,19,22,-36,22,22,-37,-48,-6,-7,-34,-33,-32,-35,-13,96,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-12,-15,-16,102,-17,22,22,-10,22,-8,111,-11,22,-9,]),'OF':([6,90,],[-47,99,]),'INT':([7,15,16,35,],[10,10,10,10,]),'ARRAY':([7,15,16,35,],[11,11,11,11,]),'NIL':([7,15,16,35,],[12,12,12,12,]),'RETURNS':([13,],[15,]),'IF':([19,22,24,42,59,71,91,102,103,106,107,108,110,111,113,],[27,27,27,-6,-7,-13,-12,27,27,-10,27,-8,-11,27,-9,]),'WHILE':([19,22,24,42,59,71,91,102,103,106,107,108,110,111,113,],[28,28,28,-6,-7,-13,-12,28,28,-10,28,-8,-11,28,-9,]),'FOREACH':([19,22,24,42,59,71,91,102,103,106,107,108,110,111,113,],[29,29,29,-6,-7,-13,-12,29,29,-10,29,-8,-11,29,-9,]),'RETURN':([19,22,24,42,59,71,91,102,103,106,107,108,110,111,113,],[30,30,30,-6,-7,-13,-12,30,30,-10,30,-8,-11,30,-9,]),'NOT':([19,21,22,24,30,31,32,33,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,71,91,94,96,99,102,103,106,107,108,110,111,113,],[33,33,33,33,33,33,33,33,33,-6,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-7,33,33,-13,-12,33,33,33,33,33,-10,33,-8,-11,33,-9,]),'VAL':([19,22,24,42,59,71,91,102,103,106,107,108,110,111,113,],[35,35,35,-6,-7,-13,-12,35,35,-10,35,-8,-11,35,-9,]),'NUMBER':([19,21,22,24,30,31,32,33,37,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,71,91,94,96,99,102,103,106,107,108,110,111,113,],[36,36,36,36,36,36,36,36,36,-6,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-7,36,36,-13,-12,36,36,36,36,36,-10,36,-8,-11,36,-9,]),'END':([23,24,39,41,42,59,71,91,105,106,108,110,112,113,],[40,-4,71,-5,-6,-7,-13,-12,108,-10,-8,-11,113,-9,]),'ELSE':([42,59,71,91,105,106,108,110,113,],[-6,-7,-13,-12,109,-10,-8,-11,-9,]),'DO':([98,],[103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,2,],[1,4,]),'func':([0,2,],[2,2,]),'iden':([3,9,19,21,22,24,30,31,32,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,62,67,94,96,99,102,103,107,111,],[5,14,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,90,92,20,20,20,20,20,20,20,]),'flist':([7,16,],[8,18,]),'type':([7,15,16,35,],[9,17,9,67,]),'body':([19,22,24,],[23,39,41,]),'stmt':([19,22,24,102,103,107,111,],[24,24,24,105,106,110,112,]),'expr':([19,21,22,24,30,31,32,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,94,96,99,102,103,107,111,],[25,38,25,25,63,64,65,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,69,101,104,25,25,25,25,]),'defvar':([19,22,24,102,103,107,111,],[26,26,26,26,26,26,26,]),'number':([19,21,22,24,30,31,32,33,37,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,94,96,99,102,103,107,111,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'clist':([37,94,],[68,100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> func','prog',1,'p_prog','parser.py',139),
  ('prog -> func prog','prog',2,'p_prog','parser.py',140),
  ('func -> FUNCTION iden LPAREN flist RPAREN RETURNS type COLON body END','func',10,'p_func','parser.py',144),
  ('body -> stmt','body',1,'p_body','parser.py',150),
  ('body -> stmt body','body',2,'p_body','parser.py',151),
  ('stmt -> expr SEMICOLON','stmt',2,'p_stmt','parser.py',156),
  ('stmt -> defvar SEMICOLON','stmt',2,'p_stmt','parser.py',157),
  ('stmt -> IF LPAREN expr RPAREN COLON stmt END','stmt',7,'p_stmt','parser.py',158),
  ('stmt -> IF LPAREN expr RPAREN COLON stmt ELSE COLON stmt END','stmt',10,'p_stmt','parser.py',159),
  ('stmt -> WHILE LPAREN expr RPAREN DO stmt','stmt',6,'p_stmt','parser.py',160),
  ('stmt -> FOREACH LPAREN iden OF expr RPAREN stmt','stmt',7,'p_stmt','parser.py',161),
  ('stmt -> RETURN expr SEMICOLON','stmt',3,'p_stmt','parser.py',162),
  ('stmt -> COLON body END','stmt',3,'p_stmt','parser.py',163),
  ('defvar -> VAL type iden','defvar',3,'p_defvar','parser.py',181),
  ('expr -> iden LPAREN clist RPAREN','expr',4,'p_expr','parser.py',190),
  ('expr -> expr LSQUAREBR expr RSQUAREBR','expr',4,'p_expr','parser.py',191),
  ('expr -> expr QUESTIONMARK expr COLON expr','expr',5,'p_expr','parser.py',192),
  ('expr -> expr EQUAL expr','expr',3,'p_expr','parser.py',193),
  ('expr -> expr PLUS expr','expr',3,'p_expr','parser.py',194),
  ('expr -> expr MINUS expr','expr',3,'p_expr','parser.py',195),
  ('expr -> expr TIMES expr','expr',3,'p_expr','parser.py',196),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','parser.py',197),
  ('expr -> expr MOD expr','expr',3,'p_expr','parser.py',198),
  ('expr -> expr LESS_THAN expr','expr',3,'p_expr','parser.py',199),
  ('expr -> expr GREATER_THAN expr','expr',3,'p_expr','parser.py',200),
  ('expr -> expr EQUALEQUAL expr','expr',3,'p_expr','parser.py',201),
  ('expr -> expr NOT_EQUAL expr','expr',3,'p_expr','parser.py',202),
  ('expr -> expr LESS_EQUAL expr','expr',3,'p_expr','parser.py',203),
  ('expr -> expr GREATER_EQUAL expr','expr',3,'p_expr','parser.py',204),
  ('expr -> expr OROR expr','expr',3,'p_expr','parser.py',205),
  ('expr -> expr ANDAND expr','expr',3,'p_expr','parser.py',206),
  ('expr -> NOT expr','expr',2,'p_expr','parser.py',207),
  ('expr -> MINUS expr','expr',2,'p_expr','parser.py',208),
  ('expr -> PLUS expr','expr',2,'p_expr','parser.py',209),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr','parser.py',210),
  ('expr -> iden','expr',1,'p_expr','parser.py',211),
  ('expr -> number','expr',1,'p_expr','parser.py',212),
  ('flist -> <empty>','flist',0,'p_flist','parser.py',257),
  ('flist -> type iden','flist',2,'p_flist','parser.py',258),
  ('flist -> type iden COMA flist','flist',4,'p_flist','parser.py',259),
  ('clist -> <empty>','clist',0,'p_clist','parser.py',273),
  ('clist -> expr','clist',1,'p_clist','parser.py',274),
  ('clist -> expr COMA clist','clist',3,'p_clist','parser.py',275),
  ('type -> INT','type',1,'p_type','parser.py',287),
  ('type -> ARRAY','type',1,'p_type','parser.py',288),
  ('type -> NIL','type',1,'p_type','parser.py',289),
  ('iden -> IDEN','iden',1,'p_iden','parser.py',295),
  ('number -> NUMBER','number',1,'p_number','parser.py',301),
]
