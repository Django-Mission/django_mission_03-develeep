# 3주차 미션
## Basic
### 미션 내용 : 고객센터 관리자 페이지 구성하기

- 고객센터 앱의 모델을 관리자페이지에 등록 구성

### 목표

- Models 기반으로 Admin 페이지 구성

### 요구사항

- 고객센터(`support`) 앱의 자주묻는질문(`Faq`), 1:1문의(`Inquiry`), 답변(`Answer`) 관리자 페이지 등록
    - 자주묻는질문(`Faq`)
        - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
        - 검색 필드 : 제목
        - 필터 필드 : 카테고리
    - 1:1문의(`Inquiry`)
        - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
        - 검색 필드 : 제목, 이메일, 전화번호
        - 필터 필드 : 카테고리
        - 인라인모델 : 답변(`Answer`)
    - 답변(`Answer`)
        - 1:1문의 모델에 인라인모델로 추가

### 코드

![basic_admin](https://user-images.githubusercontent.com/83402978/166269191-1bb8608c-fbb3-4f58-8a35-12a3e308c932.png)

### 구동 화면
#### FAQ
![basic_faq_img](https://user-images.githubusercontent.com/83402978/166269364-6e0e55d9-e992-4b32-b23d-3b0dfc0749bc.png)
#### Inquiry
![basic_Inquery_img](https://user-images.githubusercontent.com/83402978/166269458-05f701ae-f4a3-4bd0-9357-1ac5e3393fa6.png)
#### Answer
![basic_Answer_inline](https://user-images.githubusercontent.com/83402978/166269502-b2f08d21-ab98-4cf5-be97-7349216548fc.png)

## Challenge
### 미션 내용 : 기본 관리자 페이지의 사용성 개선 및 답변 상태 관리 기능 추가

### 목표

- 고객센터 담당자 업무 효율을 위한 사용성 개선
- 1:1문의 상태관리를 통한 고객응대 효율 향상

### 요구사항

- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력
        
        ※ action을 추가 학습을 위한 목적으로 실제 문자, 메일은 발송하지 않습니다.
    
### 코드
#### 상태 모델 추가
![advanced_model_update](https://user-images.githubusercontent.com/83402978/166269653-abc64fac-6592-4a36-be93-d0538d07a196.png)
#### 어드민 추가
![advanced_inquery_update](https://user-images.githubusercontent.com/83402978/166269722-c2ea0cf9-cbd4-49c1-b0af-c850fc7d0244.png)
### 구동화면
![Advanced_inquery_web](https://user-images.githubusercontent.com/83402978/166269801-3819782c-d06b-4d51-9206-2b606d927130.png)
#### 액션 구동화면
![advanced_action](https://user-images.githubusercontent.com/83402978/166269836-e7ddd8b4-ff36-49a4-8560-0d99aa79b750.png)


