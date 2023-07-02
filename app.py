import streamlit as st 
from PIL import Image


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Annisa Dias Oktanida"
PAGE_ICON = ":wave:"
NAME = "Annisa Dias Oktanida, S.MIK"
DESCRIPTION = """
Health Coding Analyst, bidang analisis dan diagnosa kode penyakit serta coding BPJS.
"""
EMAIL = "oktanidannisa@gmail.com"
SOCIAL_MEDIA = {
	'YouTube': 'https://youtube.com/@av00cadeo',
	'Twitter': 'https://twitter.com/sforstrawberry',
	'Instagram': 'https://instagram.com/_oissa',
	'Telegram': 'https://t.me/dainosolisthere'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
	image = Image.open('picture.png')
	st.image(image, width=190)

with col2:
	st.title(NAME)
	st.write(EMAIL)
	st.write(DESCRIPTION)

# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")

#####################
# Header
st.markdown('## Kualifikasi Profil', unsafe_allow_html=True)
st.info('''
Saya seorang Sarjana Informasi Kesehatan lulusan Universitas Nasional Karangturi Semarang jurusan Manajemen Informasi Kesehatan yang mendapat gelar Dengan Pujian. Saya antusias dengan hal baru serta mampu bekerja secara individu maupun dalam tim. Memiliki pengalaman praktik tentang coding kesehatan dalam bidang penyakit. Memiliki keterampilan dalam administrasi rumah sakit, pengkodean tindakan, serta pengkodean penyakit.
''')

####################
# Biodata
st.markdown('''
## Tentang Saya
''')

st.markdown('Nama 					: Annisa Dias Oktanida')
st.markdown('Tempat, Tanggal Lahir 	: Kendal, 01 Oktober 2004')
st.markdown('Agama 					: Islam')
st.markdown('Jenis Kelamin 			: Perempuan')
st.markdown('Alamat 				: Jl. Mlatiharo 1, 431 A, Mlatibaru, Semarang Timur')

######################
# Custom function for printing text
def txt(a, b):
	col1, col2 = st.columns([4,1])
	with col1:
		st.markdown(a)
	with col2:
		st.markdown(b)

def txt2(a,b):
	col1, col2 = st.columns([1,4])
	with col1:
		st.markdown(f'`{a}`')
	with col2:
		st.markdown(b)

def txt3(a,b):
	col1, col2 = st.columns([1,2])
	with col1:
		st.markdown(a)
	with col2:
		st.markdown(b)

def txt4(a, b, c):
	col1, col2, col3 = st.columns([1,5,2,2])
	with col1:
		st.markdown(f'`{a}`')
	with col2:
		st.markdown(b)
	with col3:
		st.markdown(c)

#########################
st.markdown('''
## Pendidikan
''')

st.markdown('**Analisis Koding Penyakit** (Manajemen Informasi Kesehatan), Universitas Nasional Karangturi, Semarang, 2022-2025')
st.markdown('''
- GPA : `3.89`
- Menerima penghargaan dalam Program Kreativitas Mahasiswa bidang Karsa Cipta (PKM-KC)
- Menerima penghargaan dalam lomba poster digital dengan tema kesehatan
- Menerima penghargaan dalam jurnal ilmiah oleh Perhimpunan Profesional Perekam Medis dan Informasi Kesehatan Indonesia (PORMIKI)
''')

########################
st.markdown('''
## Pengalaman
''')

st.markdown('''
- Program Magang Bersertifikat dari MBKM - Klinik Mitrakita
	- Pengelola data kesehatan pasien
- Praktik Kerja Lapangan (PKL) - RSND Diponegoro
	- Divisi rekam medis
- Himpunan Mahasiswa 
- Volunteer 
''')

#########################
st.markdown('''
## Keterampilan
''')

st.markdown('''
- Digital drawing 
- Bilingual
- Writting skills
- Problem solving
- Time management
- Analisis data
- Design
''')

#######################
st.markdown('''
## Sosial Media
''')
txt2('YouTube', 'https://youtube.com/@av00cadeo')
txt2('Twitter', 'https://twitter.com/sforstrawberry')
txt2('Instagram', 'https://instagram.com/_oissa')
txt2('Telegram', 'https://t.me/dainosolisthere')
########################


