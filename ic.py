import streamlit as st
import pandas as pd
import io
import openpyxl

st.set_page_config(page_title="Avaliação de Projetos IC", layout="centered")

st.title("📝 Avaliação de Projetos de IC 2025/2026")

st.header("1. Desempenho Acadêmico do Estudante")

st.header("Michel-Crosato E; Braga MM")

nome = st.text_input("Nome do Aluno")
orientador = st.text_input("Orientador")

media = st.number_input("Média Ponderada (0 a 10)", min_value=0.0, max_value=10.0, step=0.1)
ic_previa = st.radio("Iniciação Científica Prévia", options=[0.0, 0.5], horizontal=True)
apresentacoes = st.radio("Apresentações/Publicações", options=[0.0, 0.5], horizontal=True)

total1 = round(media + ic_previa + apresentacoes, 2)
st.success(f"Total 1: {total1:.2f} pontos")

st.header("inserir essa pontuação no campo: Nota Aluno")

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

st.header("inserir essa pontuação no campo: Nota Projeto")

st.markdown("---")
st.header("🔍 Resultado Final")

nota_final = round(total1 + total2, 2)
st.metric("Nota Final", f"{nota_final:.2f} / 20")

status = "✅ habilitado" if nota_final >= 5.0 else "🚫 não habilitado"
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

# Exportar para Excel 
excel_buffer = io.BytesIO()
with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
    df_resultado.to_excel(writer, index=False)
excel_buffer.seek(0)

st.download_button(
    label="⬇️ Baixar Excel",
    data=excel_buffer,
    file_name="avaliacao_ic.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


