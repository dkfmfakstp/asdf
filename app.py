import streamlit as st

# 음식 데이터
foods = [
    {"name": "김치찌개", "category": "한식", "ingredients": ["김치", "돼지고기", "두부", "양파", "대파", "마늘"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "비빔밥", "category": "한식", "ingredients": ["밥", "나물", "계란", "참기름", "김"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "불고기", "category": "한식", "ingredients": ["소고기", "간장", "마늘", "참기름", "후추", "양파"], "taste": "단것", "temperature": "뜨거운것"},
    {"name": "된장찌개", "category": "한식", "ingredients": ["된장", "두부", "애호박", "감자", "양파", "대파", "마늘", "고추"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "잡채", "category": "한식", "ingredients": ["당면", "소고기", "시금치", "당근", "양파", "간장", "참기름", "깨"], "taste": "단것", "temperature": "뜨거운것"},
    {"name": "떡볶이", "category": "한식", "ingredients": ["떡", "어묵", "물엿", "양파", "대파"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "순두부찌개", "category": "한식", "ingredients": ["순두부", "조개류", "고추가루", "마늘", "계란", "대파", "간장"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "삼계탕", "category": "한식", "ingredients": ["닭", "인삼", "찹쌀", "대추", "마늘", "생강"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "갈비찜", "category": "한식", "ingredients": ["소갈비", "간장", "마늘", "배", "대파", "당근", "밤"], "taste": "단것", "temperature": "뜨거운것"},
    {"name": "국수", "category": "한식", "ingredients": ["간장", "면", "다시마", "계란","김"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "김밥", "category": "한식", "ingredients": ["밥", "김", "단무지", "햄", "계란", "시금치", "당근"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "갈비", "category": "한식", "ingredients": ["고기", "간장", "소고기", "돼지고기"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "국밥", "category": "한식", "ingredients": ["밥", "국물", "소고기", "마늘", "양파", "돼지고기", "대파"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "족발", "category": "한식", "ingredients": ["간장", "돼지고기", "된장"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "치킨", "category": "한식", "ingredients": ["닭고기", "계란", "밀가루"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "제육볶음", "category": "한식", "ingredients": ["간장", "돼지고기", "대파", "양파"], "taste": "매운것", "temperature": "뜨거운것"}

    {"name": "짜장면", "category": "중식", "ingredients": ["면", "돼지고기", "춘장", "양파", "감자", "호박"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "짬뽕", "category": "중식", "ingredients": ["면", "오징어", "홍합", "배추", "양파", "마늘", "대파"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "탕수육", "category": "중식", "ingredients": ["돼지고기", "튀김가루", "전분", "파인애플", "당근", "피망", "식초"], "taste": "단것", "temperature": "뜨거운것"},
    {"name": "마파두부", "category": "중식", "ingredients": ["두부", "돼지고기", "두반장", "마늘", "대파"], "taste": "매운것", "temperature": "뜨거운것"},
    {"name": "볶음밥", "category": "중식", "ingredients": ["밥", "계란", "양파", "당근", "대파", "완두콩", "간장"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "양장피", "category": "중식", "ingredients": ["해파리", "오이", "피망", "돼지고기", "간장", "식초"], "taste": "단것", "temperature": "차가운것"},
    {"name": "고추잡채", "category": "중식", "ingredients": ["돼지고기", "피망", "양파", "목이버섯", "간장"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "군만두", "category": "중식", "ingredients": ["만두피", "돼지고기", "양배추", "부추", "마늘", "간장"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "계란볶음밥", "category": "중식", "ingredients": ["밥", "계란", "대파", "당근", "완두콩"], "taste": "짠것", "temperature": "뜨거운것"}

    {"name": "토마토 스파게티", "category": "양식", "ingredients": ["면", "소고기", "토마토 소스", "양파", "마늘", "올리브오일", "허브"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "피자", "category": "양식", "ingredients": ["피자 도우", "토마토", "치즈", "바질", "올리브오일"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "햄버거", "category": "양식", "ingredients": ["빵", "소고기", "치즈", "양상추", "토마토", "양파", "케첩"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "카프레제 샐러드", "category": "양식", "ingredients": ["토마토", "치즈", "바질", "올리브오일", "발사믹 식초"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "리조또", "category": "양식", "ingredients": ["밥", "치킨 육수", "치즈", "양파", "버터"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "라자냐", "category": "양식", "ingredients": ["파스타 시트", "소고기", "토마토 소스", "베샤멜 소스", "모짜렐라 치즈"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "치킨 파르메산", "category": "양식", "ingredients": ["닭가슴살", "토마토 소스", "치즈", "빵가루"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "시저 샐러드", "category": "양식", "ingredients": ["상추", "크루통", "치즈", "시저 드레싱"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "프렌치 프라이", "category": "양식", "ingredients": ["감자", "식용유",], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "스테이크", "category": "양식", "ingredients": ["소고기", "후추", "버터", "마늘"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "까르보나라 스파게티", "category": "양식", "ingredients": ["해물", "면", "크림소스", "베이컨", "고기"], "taste": "짠것", "temperature": "뜨거운것"}

    {"name": "스시", "category": "일식", "ingredients": ["밥", "생선회", "김", "와사비", "간장"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "라멘", "category": "일식", "ingredients": ["면", "돼지고기", "차슈", "계란", "대파", "김"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "돈카츠", "category": "일식", "ingredients": ["돼지고기", "빵가루", "밀가루", "계란", "소스"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "가츠동", "category": "일식", "ingredients": ["돼지고기", "계란", "양파", "밥", "간장"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "우동", "category": "일식", "ingredients": ["면", "가쓰오부시", "파", "유부"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "타코야키", "category": "일식", "ingredients": ["밀가루", "오징어", "파"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "야키소바", "category": "일식", "ingredients": ["면", "돼지고기", "양배추", "당근", "소스"], "taste": "짠것", "temperature": "뜨거운것"},
    {"name": "오니기리", "category": "일식", "ingredients": ["밥", "김", "연어", "매실"], "taste": "짠것", "temperature": "차가운것"},
    {"name": "모찌", "category": "일식", "ingredients": ["찹쌀가루", "팥"], "taste": "단것", "temperature": "차가운것"}

]

st.title("음식 추천 웹앱")

# 음식 종류 선택
category = st.selectbox("음식 종류를 선택하세요", options=["전체", "한식", "양식", "중식","일식"])

# 재료 입력
ingredient = st.text_input("오늘 끌리는 음식을 알기 위해 원하는 재료를 말해주세요!", "")

# 추천 버튼
if st.button("추천받기"):
    recommended = []
    for food in foods:
        if (category == "전체" or food["category"] == category) and \
           (ingredient == "" or any(ingredient in ing for ing in food["ingredients"])):
            recommended.append(food)

    if recommended:
        for food in recommended:
            st.subheader(food["name"])
            st.write(f"**종류:** {food['category']}")
            st.write(f"**맛:** {food['taste']} / **온도:** {food['temperature']}")
            st.markdown("---")
    else:
        st.write("조건에 맞는 음식이 없습니다. 다른 조건으로 시도해보세요!")

