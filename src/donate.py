import streamlit as st
import pandas as pd
import numpy as np
import emoji

# set MaMa price
mama_price = 2

def main():
    st.title(emoji.emojize('MaMa Bağışı :hearts:'))
    st.write('Mamamatikler hayvanlarını beslemek için alt kısmında mama ve su kabı bulunan, temelde para ya da atık şişe, teneke kutu, plastik şişe atıldığında mama ve/veya su veren otomat makineleridir. MaMatikler sayesinde bağışlarınızla sokak hayvanlarına yardımcı olabilirsiniz. ')
    num_of_mama = st.number_input('Kaç sokak canlısına mama bağışlamak istersiniz ?', min_value=1, step=1, )

    st.write('Toplam MaMa maliyeti {} TL'.format(num_of_mama * mama_price))
    
    # In implementation, there will be a payment system.
    # We assumed that transaction is successful whenever the user presses the button.
    is_confirmed  = st.button('İşlemi Tamamla')

    if is_confirmed:
        st.success('İşleminiz başarı ile tamamlanmıştır')
        st.image('https://artcorgi.com/wp-content/uploads/2013/12/thankyou300px.png')
        
        st.header(emoji.emojize(':hearts: Bağışladığın MaMa sokak hayvanlarına yardımcı yardımcı oldu :hearts:'))
        st.write('Bağışının yapıldığı MaMamatik konumunu aşağıda görebilirsin.')
        df = pd.DataFrame(
            np.array([[0, 0]]) + [41.089566, 29.095647],
            columns=['lat', 'lon'])

        st.map(df)
