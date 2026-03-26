

COPY public.department (id, name, description) FROM stdin;
1	Administrators	fijne gasten
2	Superusers	handige harries
\.


COPY public.account (id, name, description, department_id) FROM stdin;
2	Joris	Pruimenpoeper	2
3	Karel	schroevendraaier	1
4	Hendrik	kniptang	2
5	Truus	bombsquad	2
6	Elise	readyteddy	1
\.
