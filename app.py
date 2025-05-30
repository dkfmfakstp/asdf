import streamlit as st

# 음식 데이터
foods = [
    {
        "name": "김치찌개",
        "category": "한식",
        "ingredients": ["김치", "돼지고기", "두부"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "스파게티 볼로네제",
        "category": "양식",
        "ingredients": ["파스타", "소고기", "토마토"],
        "description": "진한 고기 소스가 매력적인 이탈리아 대표 요리입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/12/09/08/18/spaghetti-3007395_1280.jpg"
    },
    {
        "name": "짜장면",
        "category": "중식",
        "ingredients": ["면", "돼지고기", "짜장소스"],
        "description": "달콤 짭조름한 춘장 소스를 곁들인 중국식 면 요리입니다.",
        "image": "https://cdn.pixabay.com/photo/2016/11/18/16/04/jajangmyeon-1839017_1280.jpg"
    }
]

st.title("음식 추천 웹앱")

# 음식 종류 선택
category = st.selectbox("음식 종류를 선택하세요", options=["전체", "한식", "양식", "중식"])

# 재료 입력
ingredient = st.text_input("재료를 입력하세요 (선택)", "")

# 추천 버튼
if st.button("추천받기"):
    recommended = []
    for food in foods:
        if (category == "전체" or food["category"] == category) and \
           (ingredient == "" or ingredient in food["ingredients"]):
            recommended.append(food)

    if recommended:
        for food in recommended:
            st.subheader(food["name"])
            st.image(food["image"], width=300)
            st.write(f"**종류:** {food['category']}")
            st.write(f"**재료:** {', '.join(food['ingredients'])}")
            st.write(food["description"])
            st.markdown("---")
    else:
        st.write("조건에 맞는 음식이 없습니다. 다른 조건으로 시도해보세요!")
