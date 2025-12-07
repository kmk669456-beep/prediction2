%%writefile app.py
import streamlit as st
import pickle
import numpy as np

# ==============================
# 1) 모델 불러오기
# ==============================
model = pickle.load(open("model.pkl", "rb"))

st.title("올림픽공원 입장객 예측 서비스 (날씨 + 이벤트 + 검색량 기반)")

st.write("아래 변수들을 입력하면, 해당 시점의 올림픽공원 예상 입장객 수를 예측합니다.")

# ==============================
# 2) 사용자 입력값
# ==============================

show_cnt = st.number_input("공연 건수", 0, 50, 0)
max_temp = st.number_input("최고기온(℃)", -20.0, 45.0, 20.0)
wind_avg = st.number_input("평균풍속(m/s)", 0.0, 50.0, 2.0)
temp_max_avg = st.number_input("평균최고기온(℃)", -20.0, 45.0, 15.0)
temp_avg = st.number_input("평균기온(℃)", -20.0, 40.0, 10.0)
temp_min_avg = st.number_input("평균최저기온(℃)", -30.0, 35.0, 5.0)
wind_max = st.number_input("최대풍속(m/s)", 0.0, 60.0, 5.0)
temp_min = st.number_input("최저기온(℃)", -30.0, 35.0, 0.0)
holiday = st.number_input("공휴일 수", 0, 10, 0)
search_vol = st.number_input("검색량", 0, 500000, 0)

# ==============================
# 3) 예측 실행
# ==============================

if st.button("예측하기"):

    # 입력 순서 = 모델 학습 순서와 완전히 동일해야 함
    features = np.array([[
        show_cnt,      # 공연수
        max_temp,      # 최고기온
        wind_avg,      # 평균풍속
        temp_max_avg,  # 평균최고기온
        temp_avg,      # 평균기온
        temp_min_avg,  # 평균최저기온
        wind_max,      # 최대풍속
        temp_min,      # 최저기온
        holiday,       # 공휴일 수
        search_vol     # 검색량 
    ]])

    result = model.predict(features)
    pred_value = int(result[0])

    st.success(f"예측된 올림픽공원 입장객 수: **{pred_value:,}명**")
