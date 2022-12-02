
#----------------------------------------------LIBRERIAS----------------------------------------------------------------------
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns



#----------------------------------------------CONFIGURACIÓN DE PÁGINA ----------------------------------------------------------------------

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Mercado de Segunda Mano", layout="centered") # después establecer el título de página, su layout e icono 

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)
   

#---------------------------------------------- COSAS QUE PODEMOS USAR EN TODA NUESTRA APP----------------------------------------------------------------------

df = pd.read_csv("coches.csv")
df.drop(['price_financed','color','photos','phone','power','doors'], axis=1, inplace=True)
moda_fuel=df['fuel'].mode
moda_shift=df['shift'].mode
df['fuel'].fillna(0, inplace=True)
df['shift'].fillna(0, inplace=True)
df['fuel'].replace(0, moda_fuel)
df['shift'].replace(0, moda_shift)
#---------------------------------------------- EMPIEZA LA APP ----------------------------------------------------------------------


st.image ('https://www.spoticar.es/sites/spoticar.es/files/2022-10/BodegonSpoticarDsktp_0.jpg') # llamado a imágenes

st.title('Coches de segunda mano') #st.title nos va a permitir mandar un titulo


#---------------------------------------------- TABLAS QUE COMPONENEN LA APP ----------------------------------------------------------------------

tabs = st.tabs(["Marcas y caracteristicas", "Distribucion de precios segun caracteristicas", "Modelo","Conclusion"]) # establecer tabs

tab_plots= tabs[0] #nombres de cada tab, recordar que nuestra primera tab, es la posición cero para python
with tab_plots: # utilizar "with" como "context manager" lo que va a permitir insertar lo que queramos 
    st.title("En el mercado de segunda mano nos encontramos una gran variedad de coches asi representadas:") # lo que queremos insertar
    uno=px.histogram(df, x='make', title='cantidad de coches por marca', labels={'make':'Marcas'},color= 'make').update_xaxes(categoryorder='total descending')
    st.plotly_chart(uno, use_container_width=True)
    st.write('Nos encontramos que las marcas mas representativas en el mercado son las alemanas seguida de las francesas')
    st.title("Los cuales los podemos dividir de la sigiente manera :")
    color = ["Red", "Blue", "white"] 
    sns.set_palette(color) 
    c = sns.countplot(x='shift', data=df)
    c.set(title = 'tipo de caja de cambio') 
    st.pyplot()
    st.write("Observamos la gran diferencia que hay entre los tipos de cajas de cambios en la que predomina la manual")
    sns.set(rc = {'figure.figsize':(10,5)})
    f = sns.countplot(x='fuel', data=df)
    f.set(title = 'tipos de combustible')
    st.pyplot()
    st.write("En cuanto al combustible podemos observar que la gran mayoria son Diésel esto se debe a la nueva normativa medioambiental y al precio que ha adquirido en los ultimos años este combustible")
    tres=px.histogram(df, x='year', title='coches por año de fabrcacion en venta', labels={'year':'Años'},color= 'year')
    st.plotly_chart(tres, use_container_width=True)
    st.write("En la distribucion de los coches a la venta segun el año de fabrcacion, observamos que en los ultimos años ha tenido un incremeto considerable respecto a los años anteriores esto se puede deber a la modernizacion y las prestaciones que han adquirido")
    st.title('Variedad de marcas segun su combustible')
    dos=px.histogram(df, x='fuel', title='marca de coches en venta segun su combustible', labels={'make':'Marcas'},color= 'make')
    st.plotly_chart(dos, use_container_width=True)
    st.write('Podemos observar que a dia de hoy todas las marcas han ido ampliando los tipos de combustibles siendo todavia minoritarias en este mercado algunas de ellas')
    st.title('Aumento de los tipos de combustible segun los años')
    once=px.histogram(df, x='fuel', title='Distribucion de combultible por años ', labels={'make':'Marcas'},color= 'year')
    st.plotly_chart(once, use_container_width=True)
    st.write('Segun han ido pasando los años han ido apareciendo diferentes combustibles que ampliando este mercado')
    st.title("Distribucion de los coches por provincia")        
    cuatro=px.histogram(df, x='province', title='cantidad de coches por provincia', labels={'province':'Provincias'}).update_xaxes(categoryorder='total descending')
    st.plotly_chart(cuatro, use_container_width=True)
    st.write('En esta grafica podemos ver que la cantidad de coches que tenemos en venta por provincia siendo madrid la que mas aglutina con bastante diferencia respecto a las demas')
tab_plots= tabs[1] #segunda tab siempre sería tabs[1] 
with tab_plots:
    st.title('Precios del mercado')
    cinco=px.violin(df, y="price")
    st.plotly_chart(cinco, use_container_width=True)
    st.write('La mayoria de precios estan concentrados entre los 300 euros y los 42k euros estando el precio medio en 11,5k euros ')
    
    seis=px.scatter(df,x='make', y='price', title='precio segun marcas',color='make') 
    st.plotly_chart(seis, use_container_width=True)
    st.write("podemos observar que solo las marcas de alta gama salen de lo mormal y las demas tienen algun modelo más caro ")
    siete=px.scatter(df, x='price', y='year', color='price',title='precio segun el año de fabrcacion')
    st.plotly_chart(siete, use_container_width=True)
    st.write("Sacamos en claro que cuanto mas nuevo su precio aumenta, aunque tenemos algunos outlayers en coches mas antiguos a los que podriamos considerarlos como clasiscos")
    ocho=px.scatter(df, x='price', y='fuel', color='price',title='precio segun combustible')
    st.plotly_chart(ocho, use_container_width=True)
    st.write("Los nuevos combustibles tienen un valor minimo mas elvado que los tradicionales, aunque como se puede ver en gasolina podemos ver coches con un gran valor dado que suelen ser los de mayor potencia")
    nueve=px.scatter(df, x='price', y='kms', color='price',title='precio segun kilometros')
    st.plotly_chart(nueve, use_container_width=True)
    st.write("Podemos ver que a cuantos menos km mayor es su precio")
    diez=px.pie(df, values='price', names='shift', title='precio segun caja de cambios')
    st.plotly_chart(diez, use_container_width=True)
    st.write("Obsevamos que el porcentaje total de precios esta muy a la par segun la caja de cambios que utiliza, aunque como hemos podido ver antes en el grafico de tipos de cajas de cambios hay menos de la mitad de automaticos que de manuales, por lo cual un coche automatico siempre tiene un coste superior")
tab_plots= tabs[2] #tercera tab 
with tab_plots:       
    st.title("Comprativa de modelos")
    st.image('Proyecto_Final\mercado_coches_segunda_mano\modelos.png')
    st.write("Me decidi por LightGBM ya que es el que mejor rendimiento ha dado como se puede ver, ademas de que sus principales ventajas son la mayor velocidad de entrenamiento y eficacia, menos uso de memoria, mayor precision y gran capacidad de manejo de datos a gran escala.")
    st.image('Proyecto_Final\mercado_coches_segunda_mano\Peso varibles.png')
    st.write('En este grafico podemos ver el peso que reciben las variables a la hora de tomarlas encuenta para predecir')
   
tab_plots= tabs[3] #cuarta tab 
with tab_plots:  
    st.title('Conclusón')
    st.write("El mercado de coches de segunda mano cada vez es mas amplio dando cientos opciones para todo tipo de gustos, con precios que se ajustan a cualquier bolsillo, cubriendo asi necesidades del mercado del automovil que cada vez esta siendo mas recurrido por los usurios dada la actual crisis de los microchips,lo que ha conseguido que este mercado este al alza.")
    st.image('https://admin.idaoffice.org/wp-content/uploads/2018/12/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F-8-1140x550.jpg')

    
#----------------------------------------------EMPIEZA EL SIDEBAR----------------------------------------------------------------

#ocultar errores
st.set_option('deprecation.showPyplotGlobalUse', False) 

st.sidebar.title('Este es un sidebar') #st.sidebar van los elementos de interfaz como sidebar
st.sidebar.image ('https://www.spoticar.es/sites/spoticar.es/files/2022-10/BodegonSpoticarDsktp_0.jpg') # imagen como un logo en la barrita
st.sidebar.write("Hola, este es mi sidebar c:") #menu lateral 
st.sidebar.write("---") #guion, separador, hecho para estética
st.sidebar.write("Botón para mostrar DF")
if st.sidebar.button("clik here"): #Aplicando esto también tendremos un botón en nuestra sidebar
        st.dataframe(df) #el botón nos mostrará el código



