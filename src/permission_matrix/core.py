def decide(subject,action,resource,assignments,rules):
 roles=set(assignments.get(subject,()))
 matched=[r for r in rules if r["role"] in roles and r["action"] in {action,"*"} and r["resource"] in {resource,"*"}]
 if any(r["effect"]=="deny" for r in matched): return {"decision":"denied","reason":"explicit_deny"}
 if any(r["effect"]=="allow" for r in matched): return {"decision":"allowed","reason":"explicit_allow"}
 return {"decision":"denied","reason":"no_rule"}
def matrix(subjects,actions,resources,assignments,rules):
 if len(subjects)*len(actions)*len(resources)>100000: raise ValueError("matrix limit")
 return [{"subject":s,"action":a,"resource":r,**decide(s,a,r,assignments,rules)} for s in subjects for a in actions for r in resources]
def run(data): return {"matrix":matrix(**data)}

