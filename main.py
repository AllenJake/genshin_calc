
talent_mult = 2.23 #%
scaling = 2058 # atk/def/max hp/em

dgt_base = talent_mult * scaling

mult_dgt_base = 1 #ex yoi E
add_base_dgt = 0 #ex hu tao C2

bonus_dgt = 0.466 + 0.35 #% ex gobelet
reduc_dgt = 0 

dgt_crit = 2.198
taux_crit = 0.552


lvl_char = 90
lvl_enemy = 77
reduc_def = 0
ignore_def = 0 # ex raiden c2

enemy_def = (lvl_char + 100) / ((lvl_char + 100) + (lvl_enemy +100)*(1 - reduc_def)*(1 - ignore_def))

enemy_base_res = 0.1
res_reduc = 0
enemy_res = enemy_base_res - res_reduc

if enemy_res<0 :
    enemy_res_mult = 1 - enemy_res/2
elif enemy_res>= 0.75 :
    enemy_res_mult = 1/(4*enemy_res +1)
else :
    enemy_res_mult = 1 - enemy_res

mult_react = 1.5 # 2 si hydro vape ou pyro melt, 1.5 si pyro vape ou cryo melt
bonus_react = 0 #ex 4p pyro
em = 0

reaction = False

if reaction:
    ampli_react = mult_react * (1 + (2.78*em)/(1400 + em) + bonus_react)
else :
    ampli_react = 1

addi_react = 0 # autres reactions


dgt = (dgt_base * mult_dgt_base + add_base_dgt) * (1 + bonus_dgt - reduc_dgt) * (1 + dgt_crit) * enemy_def * enemy_res_mult * ampli_react + addi_react

print(dgt)