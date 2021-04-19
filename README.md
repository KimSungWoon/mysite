# 나만의 웹사이트 만들기, Mysite

## 프로젝트 설명
Front-end, Server, Database의 데이터 흐름 설계를 통한 나만의 웹사이트 제작

## 프로젝트 구조
> ### Front-end
- 제공 서비스
  - 회원가입, 로그인
  - 방명록 - 글 작성, 본인의 글 삭제
  - 게시판 - 글 작성, 본인의 글 삭제, 답글 작성, 본인의 답글 삭제

- 사용 기술 및 관련 개념
  - Django 웹 프레임워크
  - Django의 MTV 개념, HTML, CSS 언어 공부
  - Client-Server의 관계, HTTP 프로토콜의 종류 (GET, POST) 공부
  - Client의 Request의 종류, Response (Rendering, Redirect) 공부

> ### Server
- 역할
  - Client-Server 간의 통신
  - Server-Database 간의 데이터 교류

- 사용 기술 및 관련 개념
  - Linux (Ubuntu)
  - Linux 서버 환경 구축 및 보안 설정
  - 세션, 쿠키를 사용하여 로그인 상태 유지

> ### Database
- 역할
  - 회원 정보 저장 (회원 고유 번호(no), Id, 이름, E-mail, 암호화된 Password, 성별, 회원가입날짜)
  - 방명록 데이터 저장 (글 작성 번호(no), 글 작성자의 Id, 글 내용, 글 작성 일시)
  - 게시판 데이터 저장 (글 작성 번호(no), 글 작성자의 Id, 글 내용, 글 작성 일시, 글의 depth, 답글의 depth)

- 사용 기술 및 관련 개념
  - MariaDB, MySQL
  - MySQL 스키마 설계
  - MariaDB 환경 구축 및 Server, Front-end와 연결
  - 데이터 처리기능 CRUD (Create, Read, Update, Delete) 공부
  - SQL query문 공부
  - 사용자 데이터 암호화

## 개발 환경
Windows10, Linux(Ubuntu), MariaDB, MySQL

## 개발 언어
Python, HTML5, CSS3

## 개발 라이브러리 및 도구
Django, Pycharm, VirtualBox, Xshell, Xftp6, Exerd

## 사용 장비
NVIDIA GPU-RTX 2070
