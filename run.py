from arrow import get
import model
import streamlit as st
import t2_plot
from utils import get_fuzzy_index


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

    val, word, x, fp1, EK4 = get_fuzzy_index(gender, age, height, weight, metric)

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
