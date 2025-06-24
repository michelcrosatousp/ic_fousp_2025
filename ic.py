import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Avaliação de Projetos IC", layout="centered")

st.title("📝 Avaliação de Projetos de IC 2025/2026")

st.header("1. Desempenho Acadêmico do Estudante")

nome = st.text_input("Nome do Aluno")
orientador = st.text_input("Orientador")

media = st.number_input("Média Ponderada (0 a 10)", min_value=0.0, max_value=10.0, step=0.1)
ic_previa = st.radio("Iniciação Científica Prévia", options=[0.0, 0.5], horizontal=True)
apresentacoes = st.radio("Apresentações/Publicações", options=[0.0, 0.5], horizontal=True)

total1 = round(media + ic_previa + apresentacoes, 2)
st.success(f"Total 1: {total1:.2f} pontos")

st.markdown("---")
st.header("2. Avaliação do Projeto")

def criterio(texto):
    return st.radio(texto, [0, 1, 2], horizontal=True)

q1 = criterio("I. A pergunta é relevante e os objetivos estão claros?")
q2 = criterio("II. Introdução embasa a pergunta de pesquisa?")
q3 = criterio("III. Metodologia está bem descrita?")
q4 = criterio("IV. Formatação e cronograma compatíveis?")
q5 = criterio("V. Projeto compatível com IC e define função do bolsista?")

total2 = q1 + q2 + q3 + q4 + q5
st.success(f"Total 2: {total2} pontos")

st.markdown("---")
st.header("🔍 Resultado Final")

nota_final = round(total1 + total2, 2)
st.metric("Nota Final", f"{nota_final:.2f} / 20")

status = "✅ CLASSIFICADO" if nota_final >= 5.0 else "🚫 NÃO CLASSIFICADO"
st.subheader(status)

# Montar dataframe para exportação
dados = {
    "Aluno": [nome],
    "Orientador": [orientador],
    "Total 1": [total1],
    "Total 2": [total2],
    "Nota Final": [nota_final],
    "Classificação": [status]
}
df_resultado = pd.DataFrame(dados)




