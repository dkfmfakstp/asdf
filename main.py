import streamlit as st

# 음식 데이터 (일부 예시만 맛, 온도 추가)
foods = [
    {"name": "김치찌개", "category": "한식", "ingredients": ["김치", "돼지고기", "두부", "양파", "대파", "마늘", "고춧가루"], "flavor": "매운것", "temperature": "뜨거운것"},
    {"name": "비빔밥", "category": "한식", "ingredients": ["밥", "나물", "고추장", "계란", "참기름", "김"], "flavor": "짠것", "temperature": "뜨거운것"},
    {"name": "떡볶이", "category": "한식", "ingredients": ["떡", "고추장", "어묵", "설탕", "물엿", "양파", "대파"], "flavor": "매운것", "temperature": "뜨거운것"},
    {"name": "초밥", "category": "일식", "ingredients": ["생선", "밥", "와사비"], "flavor": "짠것", "temperature": "차가운것"},
    {"name": "아이스크림", "category": "양식", "ingredients": ["우유", "설탕", "크림"], "flavor": "단것", "temperature": "차가운것"},
    {"name": "제육볶음", "category": "한식", "ingredients": ["볶음", "돼지고기", "고추장", "고기"], "flavor": "매운것", "temperature": "뜨거운것"},
    # ... 기존 음식들 계속
]

st.title("🍱 음식 추천 웹앱")

# 음식 종류 선택
category = st.selectbox("🍽️ 음식 종류를 선택하세요", options=["전체", "한식", "양식", "중식", "일식"])

# 재료 입력
ingredient = st.text_input("🧂 오늘 끌리는 재료를 말해주세요!", "")

# 맛 선택
flavor = st.selectbox("😋 어떤 맛이 당기시나요?", options=["전체", "단것", "짠것", "매운것"])

# 온도 선택
temperature = st.selectbox("🌡️ 음식 온도를 선택하세요", options=["전체", "뜨거운것", "차가운것"])

# 추천 버튼
if st.button("추천받기"):
    recommended = []
    for food in foods:
        # 카테고리 조건
        category_match = category == "전체" or food["category"] == category
        # 재료 조건
        ingredient_match = ingredient == "" or ingredient in food["ingredients"]
        # 맛 조건
        flavor_match = flavor == "전체" or food.get("flavor") == flavor
        # 온도 조건
        temp_match = temperature == "전체" or food.get("temperature") == temperature

        if category_match and ingredient_match and flavor_match and temp_match:
            recommended.append(food)

    if recommended:
        for food in recommended:
            st.subheader(food["name"])
            st.write(f"**종류:** {food['category']}")
            st.write(f"**맛:** {food.get('flavor', '정보 없음')}")
            st.write(f"**온도:** {food.get('temperature', '정보 없음')}")
            st.image(food.get("image", "https://via.placeholder.com/300"), width=300)
            st.markdown("---")
    else:
        st.warning("조건에 맞는 음식이 없습니다. 다른 조건으로 시도해보세요!")
