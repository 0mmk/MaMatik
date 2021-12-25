import streamlit as st
import donate
import find_my_pet
import credits


def main():
    

    st.sidebar.title('MaMamaik Menüsü')


    operations = ['Mama Bağışı', 'Can Dostumu Bul', 'İletişim']
    st.sidebar.subheader('İşlemler')
    selected_opeartion = st.sidebar.selectbox('', operations)


    if selected_opeartion == 'Mama Bağışı':
        donate.main()
    elif selected_opeartion == 'Can Dostumu Bul':
        find_my_pet.main()
    if selected_opeartion == 'İletişim':
        credits.main()

        
if __name__ == "__main__":
    main()