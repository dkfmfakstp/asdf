import streamlit as st

# 음식 데이터
foods = [
    {
        "name": "돈까스",
        "category": "일식",
        "ingredients": ["돼지고기", "튀김"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "김밥",
        "category": "한식",
        "ingredients": ["밥", "고기", "채소"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "갈비",
        "category": "한식",
        "ingredients": ["고기", "간장", "고춧가루", "고추장"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "까르보나라 스파게티",
        "category": "양식",
        "ingredients": ["해물", "면", "크림소스"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "라멘",
        "category": "일식",
        "ingredients": ["돼지고기", "면", "채소"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "우동",
        "category": "일식",
        "ingredients": ["가쓰오부시", "면", "어묵"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "탕수육",
        "category": "중식",
        "ingredients": ["돼지고기", "튀김", "설탕"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "국밥",
        "category": "한식",
        "ingredients": ["밥", "국물", "고기", "채소"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "한식",
        "category": "족발",
        "ingredients": ["고기"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "피자",
        "category": "양식",
        "ingredients": ["치즈", "고기", "토마토","빵"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "치킨",
        "category": "한식",
        "ingredients": ["닭고기", "튀김"],
        "description": "설명.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "짬뽕",
        "category": "중식",
        "ingredients": ["해물", "면", "고춧가루", "고기"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "초밥",
        "category": "일식",
        "ingredients": ["생선", "밥", "와사비"],
        "description": "설명.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "햄버거",
        "category": "양식",
        "ingredients": ["고기", "채소", "빵",'치즈'],
        "description": "설명.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "제육볶음",
        "category": "한식",
        "ingredients": ["볶음", "돼지고기", "고추장"],
        "description": "돼지고기를 매콤하게 볶아만든 한국 고기 요리입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "김치찌개",
        "category": "한식",
        "ingredients": ["김치", "돼지고기", "두부"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "토마토 스파게티",
        "category": "양식",
        "ingredients": ["파스타", "고기", "토마토"],
        "description": "진한 토마토 소스가 매력적인 이탈리아 대표 요리입니다.",
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
category = st.selectbox("음식 종류를 선택하세요", options=["전체", "한식", "양식", "중식","일식"])

# 재료 입력
ingredient = st.text_input("정보를 입력하세요 (선택)", "")

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
            st.write(f"**정보:** {', '.join(food['ingredients'])}")
            st.write(food["description"])
            st.markdown("---")
    else:
        st.write("조건에 맞는 음식이 없습니다. 다른 조건으로 시도해보세요!")
