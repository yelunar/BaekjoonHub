-- 코드를 입력하세요
SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS, to_char(B.CREATED_DATE, 'yyyy-mm-dd') created_date 
-- 5. 게시물 제목, 게시글ID, 댓글ID, 댓글 작성자ID, 댓글 내용, 댓글 작성일('yyyy-mm-dd'형식)을 조회
from USED_GOODS_BOARD A, USED_GOODS_REPLY B
-- 1. A(USED_GOODS_BOARD) 테이블과 B(USED_GOODS_REPLY)에서
where A.BOARD_ID = B.BOARD_ID
-- 2. A.BOARD_ID(게시글ID)와 B.BOARD_ID가 같고,
and A.CREATED_DATE
-- 3. A.CREATED_DATE(게시글 작성일)가
between to_date('2022-10-01', 'yyyy-mm-dd') and to_date('2022-10-31', 'yyyy-mm-dd')
-- 2022-10-01부터 2022-10-31 사이이고,
order by B.CREATED_DATE asc, A.TITLE asc
-- 4. B.CREATED_DATE(댓글 작성일)과 A.TITLE(게시글 제목) 순으로 나열한 테이블에서