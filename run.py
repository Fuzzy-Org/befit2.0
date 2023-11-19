import random
import model
import t2_mandani_inference
import streamlit as st
import pandas as pd
import t2_fuzzifier
import t2_plot
import t2_model_of_words
from model import input_lvs


def main():
    st.sidebar.title("Запитання")

    gender = st.sidebar.selectbox("1. Яка у вас стать?", ("Чоловіча", "Жіноча"))
    age = st.sidebar.number_input(
        "2. Скільки вам років?", min_value=18, max_value=150, step=1, value=30
    )
    height = st.sidebar.number_input(
        "3. Який у вас зріст? (у см)", min_value=110, max_value=220, step=1, value=180
    )
    weight = st.sidebar.number_input(
        "4. Яка у вас вага?", min_value=40, max_value=120, step=1, value=70
    )
    metric = st.sidebar.selectbox(
        "Метрика для обрахунку?", ("cog", "fom", "lov", "mom")
    )

    gender = 1 if gender == "Чоловіча" else 0
    age = min(10, t2_fuzzifier.__normalization(age, (18, 100, 1)))
    height = min(10, t2_fuzzifier.__normalization(height, (110, 220, 1)))
    weight = min(10, t2_fuzzifier.__normalization(weight, (40, 120, 1)))

    if not "U" in model.input_lvs[0].keys():
        t2_mandani_inference.preprocessing(model.input_lvs, model.output_lv)

    val, word, x, fp1, EK4 = t2_mandani_inference.process(
        model.input_lvs,
        model.output_lv,
        model.rule_base,
        [age, weight, height],
        metric,
    )

    title = f"Ваш індекс ваги: {val:.2f}"
    if word == "Underweight":
        title += ", ви занадто худий"
    elif word == "Normal":
        title += ", у вас нормальна вага 😎"
    elif word == "Overweight":
        title += ", у вас є зайва вага"
    elif word == "Obese":
        title += ", у вас ожиріння"

    st.title(title)
    col1, col2 = st.columns(2)
    with col1:
        t2_plot.draw_t2_fuzzy_set(x, *EK4)
    with col2:
        t2_plot.draw_t_1_fuzzy_area(x, fp1)

    t2_plot.draw_words_model(model.output_lv)
    t2_plot.draw_words_model(model.input_lvs[0])


if __name__ == "__main__":
    main()
