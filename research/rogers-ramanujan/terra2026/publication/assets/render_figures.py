from pathlib import Path
import subprocess

P=Path(__file__).parent
INK='#14293b'; TEAL='#087f80'; CORAL='#cc5b4d'; GOLD='#dba847'; BG='#f8f5ed'; MUTED='#536777'; WHITE='#ffffff'; LINE='#d7e2df'; PALE='#edf6f3'; PEACH='#fceee9'

def text(x,y,s,size=24,fill=INK,weight=400,anchor='start'):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>'
def rect(x,y,w,h,fill=WHITE,stroke=LINE,r=17,sw=1.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def line(x,y,x2,y2,color=TEAL,dash='',width=3):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {"stroke-dasharray=\"8 7\"" if dash else ""}/>'
def header(k,title,sub):
    return text(54,55,k,16,TEAL,700)+text(54,103,title,34,INK,700)+text(54,137,sub,20,MUTED)
def frame(body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700" role="img"><rect width="1200" height="700" fill="{BG}"/><g font-family="DejaVu Sans, sans-serif">{body}</g></svg>'''
def save(name,body):
    svg=frame(body); (P/(name+'.svg')).write_text(svg,encoding='utf8'); subprocess.run(['inkscape',str(P/(name+'.svg')),'--export-type=png','--export-width=1800','--export-filename='+str(P/(name+'.png'))],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

b=header('01  /  RESEARCH LANDSCAPE','The problem and the current route','A positive auxiliary model is established; the complete structural bridge remains open.')
b+=rect(54,177,506,138)+rect(640,177,506,138)
b+=text(78,212,'RESIDUE PARTITIONS  B',17,TEAL,700)+text(78,249,'Parts congruent to',23)+text(78,284,'1, 3, 6, 8  (mod 9)',25,INK,700)
b+=text(664,212,'GAP PARTITIONS  A',17,TEAL,700)+text(664,249,'Distance-two gap ≥ 3',23)+text(664,284,'Close pairs sum to 0 mod 3',22)
b+=rect(54,357,506,111,PALE)+rect(640,357,506,111,PALE)
b+=text(78,392,'FLAT COLUMNS  U',17,TEAL,700)+text(78,427,'Unbounded height support',23)
b+=text(664,392,'CLUSTER COORDINATES',17,TEAL,700)+text(664,427,'(a, b, μ, ν)',23)
b+=line(307,315,307,357)+line(893,315,893,357)
b+=line(560,411,640,411,CORAL,'dash')+text(600,399,'OPEN',15,CORAL,700,'middle')
b+=rect(54,508,1092,124,WHITE,LINE)+text(78,546,'POSITIVE CUT-WORD MODELS',17,TEAL,700)+text(78,582,'All-index auxiliary models have an explicit sign cancellation.',22)+text(78,613,'Object-level recurrence maps to the KR1 gap class remain unresolved.',20,CORAL,600)
save('01_problem_route',b)

b=header('02  /  THE CANCELLATION','A marker becomes a suffix increment','One signed pair at n = 6. Each cell carries its own index.')
b+=rect(54,170,1092,452)
labels=['|','|','α','|','β','|','|','|']; xs=[210+100*i for i in range(8)]
b+=text(94,231,'word',18,MUTED,700)
for x,s in zip(xs,labels):
    b+=rect(x,195,76,66,PALE if s in 'αβ' else BG,LINE,9)+text(x+38,240,s,29,TEAL if s in 'αβ' else INK,700,'middle')
b+=text(94,313,'indices',18,MUTED,700)
for x in xs:b+=text(x+38,313,'0',25,INK,600,'middle')
b+=text(94,382,'marker',18,MUTED,700)+rect(210,350,206,52,PEACH,'#f1cbc2',9)+text(313,385,'− q¹⁸',24,CORAL,700,'middle')
b+=text(514,386,'remove marker',19,MUTED,500,'middle')+text(702,386,'→',29,TEAL,700,'middle')+text(913,386,'add 1 to δ₇',20,TEAL,700,'middle')
b+=line(89,422,1112,422,LINE,width=2)+text(94,486,'new indices',18,MUTED,700)
for i,x in enumerate(xs):b+=text(x+38,486,'1' if i>=6 else '0',25,TEAL if i>=6 else INK,700 if i>=6 else 500,'middle')
b+=text(94,559,'Intrinsic weights',18,MUTED,700)+text(292,559,'α = 28',21,INK,600)+text(432,559,'β = 32',21,INK,600)+text(624,559,'18 = 9 + 9',21,TEAL,700)+text(934,559,'TOTAL 78',23,CORAL,700)
b+=text(94,592,'The last two cut indices rise; the marker contributes the same weight.',18,MUTED)
save('02_marker_cancellation',b)

b=header('03  /  AN EXACT OBSTRUCTION','A recurrence must allow particle counts to change','At weight 8, the n = 0 row cannot preserve the number of colored particles.')
b+=rect(54,178,503,376)+rect(643,178,503,376)
b+=text(78,217,'SOURCE  C₀',17,TEAL,700)+text(78,258,'Two objects of weight 8',22,INK,600)
b+=rect(78,282,454,88,PALE)+text(99,319,'β₀(0)  +  common part 3',21)+text(99,350,'5 + 3 = 8    ·    1 colored particle',18,MUTED)
b+=rect(78,388,454,88,BG)+text(99,425,'α₀(0)  +  α₀(0)',21)+text(99,456,'4 + 4 = 8    ·    2 colored particles',18,MUTED)
b+=text(667,217,'TARGET BRANCHES',17,TEAL,700)+text(667,258,'Two objects of weight 8',22,INK,600)
b+=rect(667,282,454,88,PALE)+text(688,319,'A₁:  β₁(0) + β₁(0)',21)+text(688,350,'4 + 4 = 8    ·    2 colored particles',18,MUTED)
b+=rect(667,388,454,88,PEACH,'#f1cbc2')+text(688,425,'q⁸ A₂:  empty object',21)+text(688,456,'8 + 0 = 8    ·    0 colored particles',18,MUTED)
b+=text(895,512,'Shifted C₁ branches: no weight-8 objects',17,MUTED,500,'middle')
b+=text(600,593,'No target has exactly one colored particle.',23,CORAL,700,'middle')
save('03_particle_count_obstruction',b)

b=header('04  /  EVIDENCE AND SCOPE','What is proved, checked, and still open','The evidence has different roles; a computation or a partial certificate is not the full bijection.')
items=[('01','ALL-INDEX WRITTEN THEOREM','Positive cut-word models and sign cancellation','Written construction for every auxiliary index.',TEAL),('02','SELECTED LEAN LEMMAS','Cancellation, blocks, entropy and merge bounds','Checks selected universal components, not the full map.',TEAL),('03','FINITE CHECKS','Independent bounded tests and coefficient checks','Corroborate the implementations within stated bounds.',GOLD),('04','FULL KR1 BIJECTION','Product-to-gap algorithms and inverse proofs','Open: object-level recurrence and coverage remain.',CORAL)]
for idx,(num,label,title,sub,col) in enumerate(items):
 y=166+idx*119
 b+=rect(54,y,1092,100,WHITE,LINE,13)+f'<rect x="54" y="{y}" width="9" height="100" rx="4" fill="{col}"/>'
 b+=text(82,y+38,num,20,col,700)+text(134,y+32,label,16,col,700)+text(134,y+62,title,22,INK,700)+text(134,y+86,sub,17,MUTED)
save('04_evidence_scope',b)
