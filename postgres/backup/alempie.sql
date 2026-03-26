--
-- PostgreSQL database dump
--

\restrict RIVvihfYwFKNA8wZRIxLyJQOgrUKFpe0jBVQZwsraNhycq0fj5uJAbKWL3nCSzJ

-- Dumped from database version 17.9
-- Dumped by pg_dump version 17.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account; Type: TABLE; Schema: public; Owner: alempie
--

CREATE TABLE public.account (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL,
    department_id integer
);


ALTER TABLE public.account OWNER TO alempie;

--
-- Name: account_id_seq; Type: SEQUENCE; Schema: public; Owner: alempie
--

CREATE SEQUENCE public.account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.account_id_seq OWNER TO alempie;

--
-- Name: account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alempie
--

ALTER SEQUENCE public.account_id_seq OWNED BY public.account.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: alempie
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO alempie;

--
-- Name: department; Type: TABLE; Schema: public; Owner: alempie
--

CREATE TABLE public.department (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying NOT NULL
);


ALTER TABLE public.department OWNER TO alempie;

--
-- Name: department_id_seq; Type: SEQUENCE; Schema: public; Owner: alempie
--

CREATE SEQUENCE public.department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.department_id_seq OWNER TO alempie;

--
-- Name: department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: alempie
--

ALTER SEQUENCE public.department_id_seq OWNED BY public.department.id;


--
-- Name: account id; Type: DEFAULT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.account ALTER COLUMN id SET DEFAULT nextval('public.account_id_seq'::regclass);


--
-- Name: department id; Type: DEFAULT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.department ALTER COLUMN id SET DEFAULT nextval('public.department_id_seq'::regclass);


--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: alempie
--

COPY public.account (id, name, description, department_id) FROM stdin;
2	Joris	Pruimenpoeper	2
3	Karel	schroevendraaier	1
4	Hendrik	kniptang	2
5	Truus	bombsquad	2
6	Elise	readyteddy	1
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: alempie
--

COPY public.alembic_version (version_num) FROM stdin;
16d3ed6cd203
\.


--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: alempie
--

COPY public.department (id, name, description) FROM stdin;
1	Administrators	fijne gasten
2	Superusers	handige harries
\.


--
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alempie
--

SELECT pg_catalog.setval('public.account_id_seq', 6, true);


--
-- Name: department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: alempie
--

SELECT pg_catalog.setval('public.department_id_seq', 2, true);


--
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id);


--
-- Name: account account_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: alempie
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(id);


--
-- PostgreSQL database dump complete
--

\unrestrict RIVvihfYwFKNA8wZRIxLyJQOgrUKFpe0jBVQZwsraNhycq0fj5uJAbKWL3nCSzJ

