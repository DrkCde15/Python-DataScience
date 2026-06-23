# Scikit-Learn - Aprendizado de Máquina

Notebooks e exercícios de **aprendizado de máquina** usando a biblioteca Scikit-Learn.

## Estrutura

```
scikit-learn/
├── aula_01/              # Classificação com KNN (Iris dataset)
├── aula_02/              # Pré-processamento (imputação, encoding, scaling)
├── aula_03/              # Engenharia de features (polynomial, seleção, transformação)
├── aula_04/              # Métricas de regressão e regularização (Ridge/Lasso)
├── aula_05/              # (vazio)
├── aula_06/              # (vazio)
└── ml_exercices/         # Exercícios práticos
    ├── train_test_split.ipynb
    ├── regressao_linear.ipynb
    ├── regressao_logistica.ipynb
    ├── regressao_ride.ipynb
    ├── knn.ipynb
    ├── metrica_binaria.ipynb
    ├── curva_ROC.ipynb
    └── datasets/
        └── ReducaoOxigenio.xlsx
```

## Conteúdo

### Aulas

| Aula | Tópico | Descrição |
|------|--------|-----------|
| 01 | KNN Classifier | Classificação no dataset Iris; split treino/teste; acurácia |
| 02 | Pré-processamento | `SimpleImputer`, `KNNImputer`, `OneHotEncoder`, `LabelEncoder`, `StandardScaler` |
| 03 | Feature Engineering | `PolynomialFeatures`, `SelectKBest`, `RFE`, `PowerTransformer` |
| 04 | Regressão | MAE/MSE/RMSE/MAPE/R²; overfitting; Ridge e Lasso regularization |

### Exercícios

| Exercício | Descrição |
|-----------|-----------|
| `train_test_split` | Split simples no dataset Iris |
| `regressao_linear` | Regressão linear manual e com scikit-learn (Redução de Oxigênio) |
| `regressao_logistica` | Regressão logística no Iris com matriz de confusão |
| `regressao_ride` | Ridge regression no Boston Housing |
| `knn` | KNN para classificação (Wine) e regressão (Diabetes) |
| `metrica_binaria` | Acurácia, precisão, recall, F1-score, classification report |
| `curva_ROC` | Curva ROC e AUC com MLPClassifier |
