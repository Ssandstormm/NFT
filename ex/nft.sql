-- 
-- PostgreSQL database dump 
-- 
 
-- Dumped from database version 13.8 
-- Dumped by pg_dump version 13.8 
 
-- Started on 2022-10-16 13:58:40 
 
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
 
SET default_tablespace = ''; 
 
SET default_table_access_method = heap; 
 
-- 
-- TOC entry 201 (class 1259 OID 17503) 
-- Name: nfts; Type: TABLE; Schema: public; Owner: postgres 
-- 
 
CREATE TABLE public.nfts ( 
    nft_address character varying, 
    nft_metadata character varying 
); 
 
 
ALTER TABLE public.nfts OWNER TO postgres; 
 
-- 
-- TOC entry 200 (class 1259 OID 17494) 
-- Name: testvalues; Type: TABLE; Schema: public; Owner: postgres 
-- 
 
CREATE TABLE public.testvalues ( 
    randomstring character varying(50) 
); 
 
 
ALTER TABLE public.testvalues OWNER TO postgres; 
 
-- 
-- TOC entry 2984 (class 0 OID 17503) 
-- Dependencies: 201 
-- Data for Name: nfts; Type: TABLE DATA; Schema: public; Owner: postgres 
-- 
 
COPY public.nfts (nft_address, nft_metadata) FROM stdin; 
3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU {"mint":"3LZ9ezL5BkCtvdVGLkrw1q633EgfeYDpgGtBgWDgmaSU","standard":"metaplex","name":"Baby Yetis #257","symbol":"","metaplex":{"metadataUri":"https://arweave.net/4PtHGFuAw2U-T4nrIWVRxJ0EpVIivRWi4xjreBkmMVg","updateAuthority":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","sellerFeeBasisPoints":500,"primarySaleHappened":0,"owners":[{"address":"64eiSEPv2KRKNkPAX6d4BZQ3b12PcFqZP2yPoNAZw9po","verified":0,"share":100},{"address":"yeT3ik5jX5RuK8JF8P3RRHrr9g6ox6RMWbRMh3r9FxQ","verified":1,"share":0}],"isMutable":true,"masterEdition":false}} 
\. 
 
 
-- 
-- TOC entry 2983 (class 0 OID 17494) 
-- Dependencies: 200 
-- Data for Name: testvalues; Type: TABLE DATA; Schema: public; Owner: postgres 
-- 
 
COPY public.testvalues (randomstring) FROM stdin; 
asedfg 
vft 
nasgdfhhtndfhb 
w nebgrtt 
hello world 
\.