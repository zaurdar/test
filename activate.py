import streamlit as st
import subprocess
def main():
    st.title("Page de connexion")

    # Champ de saisie pour le nom d'utilisateur
    username = st.text_input("Nom d'utilisateur")

    # Champ de saisie pour le mot de passe
    password = st.text_input("Mot de passe", type="password")

    # Bouton de connexion
    if st.button("Se connecter"):
        if username == "moi" and password == "malice":
            st.success("Connexion réussie !")
            subprocess.run("streamlit run app.py")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")

if __name__ == "__main__":
    main()
