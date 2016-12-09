######################## read source code #######################
f_code_in = open('codeT1.input')
token_data = []

for line in f_code_in:
    line = line.replace('\n','')
    line = line.replace('    ','')
    line = line.replace('\t','')
    [token_data.append(e) for e in line.split(' ')]
f_code_in.close()
token_data.append('$')
#################################################################
#### make parser table and read nonterminal symbol  #############
f_nonterminal_in = open('nonterminal.input')
table = dict()
nonterminal = []
for line in f_nonterminal_in:
    line = line.replace('\n','')
    line = line.replace('    ','')
    line = line.replace('\t','')
    nonterminal.append(line)
    table[line]=dict()

f_nonterminal_in.close()
#################################################################
######################### read terminal symbol  ##################
f_terminal_in = open('terminal.input')
terminal = []
for line in f_terminal_in:
    line = line.replace('\n','')
    line = line.replace('"','')
    [terminal.append(e) for e in line.split(',')]
f_terminal_in.close()

f_table_data_in = open('pTable.input')
nonterminal_index = 0
for line in f_table_data_in:
    line = line.replace('\n','')
    number_in_line = [int(e) for e in line.split(',')]
    for i in range(len(terminal)):
        table[nonterminal[nonterminal_index]][terminal[i]] = number_in_line[i]
    nonterminal_index+=1
f_table_data_in.close()
##############################################################
################### fill pasing table ########################
f_rule_in = open('rule.input')
rule = []
for line in f_rule_in:
    line = line.replace('\n','')
    l_line = [e for e in line.split(' ')]
    rule.append(l_line)
    print(l_line)

#################### check Gramma ##########################

r = 1
token_index = 0
accept = False
check_stack = ['$','CODE']
while True:
    print('word ',r)
    top_stack = check_stack.pop()
    now_token = token_data[token_index]
    print(top_stack+' '+now_token)
    if(top_stack=='LAMBDA'):
        continue
    if(token_index >= len(token_data) or top_stack =='error'):
        break
    if(top_stack =='$'):
        if(now_token=='$'):
            accept = True
            break
        else:
            break
    elif top_stack  == now_token:
        r+=1
        token_index+=1
        print('==')
    else:
        try:
            rule_number = table[top_stack][now_token]
            print('rule nember',rule_number)
            l = len(rule[rule_number])
            for i in range(l):
                check_stack.append(rule[rule_number][l-1-i])
        except KeyError:
            break
    print(check_stack)
#################################################################
################### print answer ###############################
if(accept):
    print('ACCEPT')
else:
    print('ERROR')
###############################################################
