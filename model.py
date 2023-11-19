var_use = {
    "male": [(18, 100, 1), (50, 120, 1), (120, 220, 1)],  # вік, вага, ріст
    "female": [(18, 100, 1), (40, 100, 1), (110, 210, 1)],
}

input_lvs = [
    {
        "X": (0, 10.1, 0.1),
        "name": "Age",
        "terms": {
            "young": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "adult": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "middle": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "senior": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
    {
        "X": (0, 10.1, 0.1),
        "name": "Weight",
        "terms": {
            "light": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "avarage": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "heavy": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "hefty": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
    {
        "X": (0, 10.1, 0.1),
        "name": "Height",
        "terms": {
            "short": {
                "umf": ("trapmf", 0, 0, 0.55, 4.61),
                "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
            },
            "average": {
                "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
                "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
            },
            "tall": {
                "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
                "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
            },
            "stature": {
                "umf": ("trapmf", 7.37, 9.36, 10, 10),
                "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
            },
        },
    },
]


output_lv = {
    "X": (0, 10.01, 0.01),
    "terms": {
        "Underweight": {
            "umf": ("trapmf", 0, 0, 0.55, 4.61),
            "lmf": ("trapmf", 0, 0, 0.09, 1.15, 1),
        },
        "Normal": {
            "umf": ("trapmf", 0.42, 2.25, 4.00, 5.41),
            "lmf": ("trapmf", 2.79, 3.21, 3.21, 0.34, 3.71),
        },
        "Overweight": {
            "umf": ("trapmf", 3.38, 5.50, 7.25, 9.02),
            "lmf": ("trapmf", 5.79, 6.28, 6.28, 0.33, 6.67),
        },
        "Obese": {
            "umf": ("trapmf", 7.37, 9.36, 10, 10),
            "lmf": ("trapmf", 8.68, 9.91, 10, 10, 1),
        },
    },
}

rule_base = [
    (("young", "light", "short"), "Normal"),
    (("young", "light", "average"), "Normal"),
    (("young", "light", "tall"), "Normal"),
    (("young", "light", "stature"), "Underweight"),
    (("young", "average", "short"), "Overweight"),
    (("young", "average", "average"), "Overweight"),
    (("young", "average", "tall"), "Normal"),
    (("young", "average", "stature"), "Underweight"),
    (("young", "heavy", "short"), "Obese"),
    (("young", "heavy", "average"), "Overweight"),
    (("young", "heavy", "tall"), "Overweight"),
    (("young", "heavy", "stature"), "Normal"),
    (("young", "hefty", "short"), "Obese"),
    (("young", "hefty", "average"), "Obese"),
    (("young", "hefty", "tall"), "Obese"),
    (("young", "hefty", "stature"), "Overweight"),
    (("adult", "light", "short"), "Normal"),
    (("adult", "light", "average"), "Normal"),
    (("adult", "light", "tall"), "Underweight"),
    (("adult", "light", "stature"), "Underweight"),
    (("adult", "average", "short"), "Overweight"),
    (("adult", "average", "average"), "Normal"),
    (("adult", "average", "tall"), "Normal"),
    (("adult", "average", "stature"), "Underweight"),
    (("adult", "heavy", "short"), "Overweight"),
    (("adult", "heavy", "average"), "Overweight"),
    (("adult", "heavy", "tall"), "Overweight"),
    (("adult", "heavy", "stature"), "Normal"),
    (("adult", "hefty", "short"), "Obese"),
    (("adult", "hefty", "average"), "Obese"),
    (("adult", "hefty", "tall"), "Overweight"),
    (("adult", "hefty", "stature"), "Overweight"),
    (("middle", "light", "short"), "Normal"),
    (("middle", "light", "average"), "Underweight"),
    (("middle", "light", "tall"), "Underweight"),
    (("middle", "light", "stature"), "Underweight"),
    (("middle", "average", "short"), "Normal"),
    (("middle", "average", "average"), "Normal"),
    (("middle", "average", "tall"), "Normal"),
    (("middle", "average", "stature"), "Underweight"),
    (("middle", "heavy", "short"), "Overweight"),
    (("middle", "heavy", "average"), "Overweight"),
    (("middle", "heavy", "tall"), "Normal"),
    (("middle", "heavy", "stature"), "Normal"),
    (("middle", "hefty", "short"), "Obese"),
    (("middle", "hefty", "average"), "Overweight"),
    (("middle", "hefty", "tall"), "Overweight"),
    (("middle", "hefty", "stature"), "Overweight"),
    (("senior", "light", "short"), "Underweight"),
    (("senior", "light", "average"), "Underweight"),
    (("senior", "light", "tall"), "Underweight"),
    (("senior", "light", "stature"), "Underweight"),
    (("senior", "average", "short"), "Normal"),
    (("senior", "average", "average"), "Normal"),
    (("senior", "average", "tall"), "Underweight"),
    (("senior", "average", "stature"), "Underweight"),
    (("senior", "heavy", "short"), "Overweight"),
    (("senior", "heavy", "average"), "Overweight"),
    (("senior", "heavy", "tall"), "Normal"),
    (("senior", "heavy", "stature"), "Normal"),
    (("senior", "hefty", "short"), "Obese"),
    (("senior", "hefty", "average"), "Overweight"),
    (("senior", "hefty", "tall"), "Overweight"),
    (("senior", "hefty", "stature"), "Overweight"),
]
