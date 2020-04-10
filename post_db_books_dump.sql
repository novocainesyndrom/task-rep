--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: tbl_books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbl_books (
    b_id character(17) NOT NULL,
    b_name character(255) NOT NULL,
    b_author character(255),
    b_topic integer,
    b_price numeric(4,2)
);


ALTER TABLE public.tbl_books OWNER TO postgres;

--
-- Name: tbl_topics; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tbl_topics (
    topic_id integer NOT NULL,
    topic_name character(100),
    CONSTRAINT tbl_topics_topic_id_check CHECK (((topic_id >= 0) AND (topic_id <= 128)))
);


ALTER TABLE public.tbl_topics OWNER TO postgres;

--
-- Name: tbl_topics_topic_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tbl_topics_topic_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tbl_topics_topic_id_seq OWNER TO postgres;

--
-- Name: tbl_topics_topic_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tbl_topics_topic_id_seq OWNED BY public.tbl_topics.topic_id;


--
-- Name: tbl_topics topic_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbl_topics ALTER COLUMN topic_id SET DEFAULT nextval('public.tbl_topics_topic_id_seq'::regclass);


--
-- Data for Name: tbl_books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbl_books (b_id, b_name, b_author, b_topic, b_price) FROM stdin;
0-266-11156      	Moby-Dick                                                                                                                                                                                                                                                      	Herman Melville                                                                                                                                                                                                                                                	1	32.99
0-77-356-98      	Catch-22                                                                                                                                                                                                                                                       	Joseph Heller                                                                                                                                                                                                                                                  	1	21.95
0-91-156-78      	The Diary of a Young Girl                                                                                                                                                                                                                                      	Anne Frank                                                                                                                                                                                                                                                     	3	12.09
0-71-389-5-7     	The Waste Land                                                                                                                                                                                                                                                 	T. S. Eliot                                                                                                                                                                                                                                                    	2	17.11
0-14-89-357      	The Boy who was Raised as a Dog                                                                                                                                                                                                                                	Bruce Perry                                                                                                                                                                                                                                                    	4	10.88
0-4-198-63       	Essays                                                                                                                                                                                                                                                         	Michel de Montaigne                                                                                                                                                                                                                                            	5	38.50
\.


--
-- Data for Name: tbl_topics; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tbl_topics (topic_id, topic_name) FROM stdin;
1	classic                                                                                             
2	poetry                                                                                              
3	memoirs                                                                                             
4	psychology                                                                                          
5	philosophy                                                                                          
\.


--
-- Name: tbl_topics_topic_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tbl_topics_topic_id_seq', 5, true);


--
-- Name: tbl_books tbl_books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbl_books
    ADD CONSTRAINT tbl_books_pkey PRIMARY KEY (b_id);


--
-- Name: tbl_topics tbl_topics_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbl_topics
    ADD CONSTRAINT tbl_topics_pkey PRIMARY KEY (topic_id);


--
-- Name: tbl_topics tbl_topics_topic_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbl_topics
    ADD CONSTRAINT tbl_topics_topic_name_key UNIQUE (topic_name);


--
-- Name: tbl_books tbl_books_b_topic_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tbl_books
    ADD CONSTRAINT tbl_books_b_topic_fkey FOREIGN KEY (b_topic) REFERENCES public.tbl_topics(topic_id);


--
-- PostgreSQL database dump complete
--

