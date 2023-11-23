import model
import t2_mandani_inference
import t2_fuzzifier
from model import input_lvs


def get_fuzzy_index(gender, age, height, weight, metric):
    gender = 1 if gender == "Чоловіча" else 0
    age = min(10, t2_fuzzifier.__normalization(age, (18, 100, 1)))
    height = min(10, t2_fuzzifier.__normalization(height, (150, 220, 1)))
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

    return val, word, x, fp1, EK4
