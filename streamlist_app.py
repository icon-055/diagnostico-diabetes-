import streamlit as st
import pickle

# Função para carregar o modelo
def load_model():
    with open('trained_model.sav', 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title("Classificação de Diabetes")

    # Carregar o modelo
    model = load_model()

    # Campos de entrada para o usuário
    gravidezes = st.number_input("Número de vezes grávida", min_value=0, max_value=20, value=0)
    glicose = st.number_input("Concentração de glicose", min_value=0, max_value=200, value=0)
    pressao_sanguinea = st.number_input("Pressão sanguínea", min_value=0, max_value=150, value=0)
    espessura_pele = st.number_input("Espessura da pele", min_value=0, max_value=100, value=0)
    insulina = st.number_input("Insulina", min_value=0, max_value=1000, value=0)
    imc = st.number_input("IMC", min_value=0.0, max_value=50.0, value=0.0)
    pedigree_diabetes = st.number_input("Função de pedigree de diabetes", min_value=0.0, max_value=2.5, value=0.0)
    idade = st.number_input("Idade", min_value=0, max_value=120, value=0)

    # Botão para fazer a previsão
    if st.button("Prever"):
        # Preparar os dados de entrada
        input_data = np.array([[gravidezes, glicose, pressao_sanguinea, espessura_pele, insulina, imc, pedigree_diabetes, idade]])
        prediction = model.predict(input_data)

        # Exibir o resultado
        if prediction[0] == 1:
            st.success("A pessoa é portadora de diabetes.")
        else:
            st.success("A pessoa não é portadora de diabetes.")

if __name__ == '__main__':
    main()
