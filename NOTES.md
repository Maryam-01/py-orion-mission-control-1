# NOTES.md

## Task 1: Domain Understanding

**The three resources**

[What are the resources, their attributes, and what they represent?]
the resources are any piece of identifiable data or entity such as user, id or product. the resource in crew.json are the three crews. the attributes are the id, name, role, clearance. 

**Relationships**

[How are the three resources connected to each other?]
The mission_id is a foreign key in crew which connects to the mission id.
The spacecraft__id is a foreign key in mission , which is connected to the id in spacecraft.


**What the API needs to support**

[For each resource, what operations would a client need to perform?]
We could select all missions, GET/missions, GET/mission/destination='Mars', POST/mission, DELETE/mission. 
The client should be able to retreive objects present in the API, DELETE or ADD new objects.
## Task 2: Critique

[For each violation in bad_design.md: quote the endpoint, name the violation, explain why it matters.]

**Corrected endpoint table**

[Your corrected version of Felix's design goes here.]

---

## Task 3: Design Decisions

**Why was each resource modelled the way it was?**

[Pick one non-obvious decision and explain the reasoning.]

**Client-side vs server-side concerns**

[Pick one feature. What does the client send? What does the server do? What does the server return? Which concerns live where?]
