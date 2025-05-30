import streamlit as st

# 음식 데이터
foods = [
    {
        "name": "국수",
        "category": "한식",
        "ingredients": ["육수", "면", "야채"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "data:image/jpeg;base64,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"
    },
    {
        "name": "돈까스",
        "category": "일식",
        "ingredients": ["돼지고기", "튀김", "고기"],
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
        "ingredients": ["고기", "간장", "소고기", "돼지고기" ],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "까르보나라 스파게티",
        "category": "양식",
        "ingredients": ["해물", "면", "크림소스", "베이컨", "고기"],
        "description": "매콤하고 깊은 맛의 한국 전통 찌개입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "라멘",
        "category": "일식",
        "ingredients": ["돼지고기", "면", "채소", "고기"],
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
        "ingredients": ["돼지고기", "튀김", "설탕", "고기"],
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
        "ingredients": ["고기", "돼지고기"],
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
        "ingredients": ["닭고기", "튀김", "고기"],
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
        "ingredients": ["볶음", "돼지고기", "고추장", "고기"],
        "description": "돼지고기를 매콤하게 볶아만든 한국 고기 요리입니다.",
        "image": "https://cdn.pixabay.com/photo/2017/06/22/18/38/korean-food-2432252_1280.jpg"
    },
    {
        "name": "김치찌개",
        "category": "한식",
        "ingredients": ["김치", "돼지고기", "두부", "고기"],
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
