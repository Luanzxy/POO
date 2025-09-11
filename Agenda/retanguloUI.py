import streamlit as st
from retanguloUI import RetanguloUI

class RetanguloUI:
    def main():
        st.header("Cálculo com Retângulo")
        base = st.text_input("Valor da base")
        altura = st.text_input("Valor da altura")
        if st.button("Calcular"):
            b = float(base)
            h = float(altura)
            r = Retangulo(b, h)
            st.write(r)
            st.write(r.calc_area())
            st.write(r.calc_diagonal())