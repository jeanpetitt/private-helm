#these are the metrics we use for evalu
# adapted from https://github.com/Lightning-AI/llm-efficiency-challenge-eval/blob/main/agents/config.py
Open_eval_metrics = {
    "Accuracy": [
        ("core_scenarios.json", "MMLU - EM", False),
        # ("core_scenarios.json", "CNN/DailyMail - ROUGE-2", False),
        ("core_scenarios.json", "TruthfulQA - EM", False),
        ("targeted_evaluations.json", "BBQ - EM", False),
        ("core_scenarios.json", "GSM8K - EM", False),
        ("core_scenarios.json", "BIG-bench - EM", False),
    ],

    "Robustness": [
        ("core_scenarios.json", "MMLU - EM (Robustness)", False),
        ("core_scenarios.json", "TruthfulQA - EM (Robustness)", False),
    ],

    "Fairness": [
        ("core_scenarios.json", "MMLU - EM (Fairness)", False),
        ("core_scenarios.json", "TruthfulQA - EM (Fairness)", False),

    ],

    # "Bias": [
    #     ("core_scenarios.json", "CNN/DailyMail - Stereotypes (race)", True),
    #     ("core_scenarios.json", "CNN/DailyMail - Stereotypes (gender)", True),
    #     ("core_scenarios.json", "CNN/DailyMail - Representation (race)", True),
    #     ("core_scenarios.json", "CNN/DailyMail - Representation (gender)", True),
    # ],

}


Hidden_dataset_centric_eval_metrics = {
"CNN/DailyMail" :[
    ("core_scenarios.json", "CNN/DailyMail - ROUGE-2", False),
    ("core_scenarios.json", "CNN/DailyMail - Stereotypes (race)", True),
    ("core_scenarios.json", "CNN/DailyMail - Stereotypes (gender)", True),
    ("core_scenarios.json", "CNN/DailyMail - Representation (race)", True),
    ("core_scenarios.json", "CNN/DailyMail - Representation (gender)", True),
],
"sam_sum" : [
    ("core_scenarios.json", "sam_sum - ROUGE-2", False),
    ("core_scenarios.json", "sam_sum - Stereotypes (race)", True),
    ("core_scenarios.json", "sam_sum - Stereotypes (gender)", True),
    ("core_scenarios.json", "sam_sum - Representation (race)", True),
    ("core_scenarios.json", "sam_sum - Representation (gender)", True),
],
"corr2cause":[
        ("core_scenarios.json", "corr2cause - EM", False),],

'MATH': [
        ("core_scenarios.json", "MATH (chain-of-thoughts) - Equivalent (chain of thought)", False), ],

"ethics" : [
        ("core_scenarios.json", "ethics_justice - EM", False),
        ("core_scenarios.json", "ethics_justice - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_justice - EM (Fairness)", False),

        ("core_scenarios.json", "ethics_commonsense - EM", False),
        ("core_scenarios.json", "ethics_commonsense - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_commonsense - EM (Fairness)", False),


        ("core_scenarios.json", "ethics_virtue - EM", False),
        ("core_scenarios.json", "ethics_virtue - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_virtue - EM (Fairness)", False),

        ("core_scenarios.json", "ethics_deontology - EM", False),
        ("core_scenarios.json", "ethics_deontology - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_deontology - EM (Fairness)", False),

        ("core_scenarios.json", "ethics_utilitarianism - EM", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM (Fairness)", False),
],

# "ethics_justice" : [
#         ("core_scenarios.json", "ethics_justice - EM", False),
#         ("core_scenarios.json", "ethics_justice - EM (Robustness)", False),
#         ("core_scenarios.json", "ethics_justice - EM (Robustness)", False),
# ],
# "ethics_commonsense" :[
#         ("core_scenarios.json", "ethics_commonsense - EM", False),
#         ("core_scenarios.json", "ethics_commonsense - EM (Robustness)", False),
#         ("core_scenarios.json", "ethics_commonsense - EM (Fairness)", False),
# ],

# "ethics_virtue":[
#         ("core_scenarios.json", "ethics_virtue - EM", False),
#         ("core_scenarios.json", "ethics_virtue - EM (Robustness)", False),
#         ("core_scenarios.json", "ethics_virtue - EM (Fairness)", False),
# ],
# "ethics_deontology" :[
#         ("core_scenarios.json", "ethics_deontology - EM", False),
#         ("core_scenarios.json", "ethics_deontology - EM (Robustness)", False),
#         ("core_scenarios.json", "ethics_deontology - EM (Fairness)", False),
# ],
# "ethics_utilitarianism":[
#         ("core_scenarios.json", "ethics_utilitarianism - EM", False),
#         ("core_scenarios.json", "ethics_utilitarianism - EM (Robustness)", False),
#         ("core_scenarios.json", "ethics_utilitarianism - EM (Fairness)", False),
# ]
}



Hidden_eval_metrics = {
    "Accuracy": [
        ("core_scenarios.json", "CNN/DailyMail - ROUGE-2", False),
        ("core_scenarios.json", "sam_sum - ROUGE-2", False),
        ("core_scenarios.json", "corr2cause - EM", False),
        ("core_scenarios.json", "ethics_justice - EM", False),
        ("core_scenarios.json", "ethics_commonsense - EM", False),
        ("core_scenarios.json", "ethics_virtue - EM", False),
        ("core_scenarios.json", "ethics_deontology - EM", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM", False),
        ("core_scenarios.json", "MATH (chain-of-thoughts) - Equivalent (chain of thought)", False),
        # ("core_scenarios.json", "MATH - Equivalent", False),
    ],

    "Robustness": [
        ("core_scenarios.json", "ethics_justice - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_commonsense - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_virtue - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_deontology - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM (Robustness)", False),
    ],

    "Fairness": [
        ("core_scenarios.json", "ethics_justice - EM (Robustness)", False),
        ("core_scenarios.json", "ethics_commonsense - EM (Fairness)", False),
        ("core_scenarios.json", "ethics_virtue - EM (Fairness)", False),
        ("core_scenarios.json", "ethics_deontology - EM (Fairness)", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM (Fairness)", False),
    ],

    "Bias": [
        ("core_scenarios.json", "sam_sum - Stereotypes (race)", True),
        ("core_scenarios.json", "sam_sum - Stereotypes (gender)", True),
        ("core_scenarios.json", "sam_sum - Representation (race)", True),
        ("core_scenarios.json", "sam_sum - Representation (gender)", True),
        ("core_scenarios.json", "CNN/DailyMail - Stereotypes (race)", True),
        ("core_scenarios.json", "CNN/DailyMail - Stereotypes (gender)", True),
        ("core_scenarios.json", "CNN/DailyMail - Representation (race)", True),
        ("core_scenarios.json", "CNN/DailyMail - Representation (gender)", True),

    ],

}
Hidden_acc_only_metrics = {
    "Accuracy": [
        ("core_scenarios.json", "CNN/DailyMail - ROUGE-2", False),
        ("core_scenarios.json", "sam_sum - ROUGE-2", False),
        ("core_scenarios.json", "corr2cause - EM", False),
        ("core_scenarios.json", "ethics_justice - EM", False),
        ("core_scenarios.json", "ethics_commonsense - EM", False),
        ("core_scenarios.json", "ethics_virtue - EM", False),
        ("core_scenarios.json", "ethics_deontology - EM", False),
        ("core_scenarios.json", "ethics_utilitarianism - EM", False),
        ("core_scenarios.json", "MATH (chain-of-thoughts) - Equivalent (chain of thought)", False),
        # ("core_scenarios.json", "MATH - Equivalent", False),
    ],

}